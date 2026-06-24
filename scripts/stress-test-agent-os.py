#!/usr/bin/env python3
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path
from urllib.parse import urldefrag

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_ROOT = [
    'README.md', 'AGENTS.md', 'SOUL.md', 'USER.md', 'MAPA.md', 'MEMORY.md',
    'TOOLS.md', 'PROPAGATION.md', 'HERMES.md', 'agent-os.yaml', '.gitignore',
    '.env.example', 'LICENSE.md'
]
FORBIDDEN_TEXT = ['pixel' + '-educacao/agent-os-hermes']
SECRET_PATTERNS = [
    re.compile(r'ghp_[A-Za-z0-9_]{20,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{20,}'),
    re.compile(r'BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY'),
]
MD_LINK_RE = re.compile(r'(?<!\!)\[[^\]]+\]\(([^)]+)\)')

failures: list[str] = []
checks: list[str] = []


def ok(name: str) -> None:
    checks.append(name)
    print(f'OK  {name}')


def fail(name: str, detail: str) -> None:
    failures.append(f'{name}: {detail}')
    print(f'ERR {name}: {detail}')


def run(cmd: list[str], cwd: Path = ROOT, timeout: int = 60) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=cwd, text=True, capture_output=True, timeout=timeout)


def text_files():
    for p in ROOT.rglob('*'):
        if '.git' in p.parts or p.is_dir():
            continue
        if p.suffix.lower() in {'.md', '.yaml', '.yml', '.txt', '.py', '.sh', '.example', ''}:
            yield p


# 1. Required structure
missing = [rel for rel in REQUIRED_ROOT if not (ROOT / rel).exists()]
if missing:
    fail('required-root-files', ', '.join(missing))
else:
    ok('required-root-files')

# 2. Built-in validator
res = run([sys.executable, 'scripts/validate-agent-os.py'])
if res.returncode != 0:
    fail('validate-agent-os.py', res.stdout + res.stderr)
else:
    ok('validate-agent-os.py')

# 3. Git whitespace check when repo is initialized
if (ROOT / '.git').exists():
    res = run(['git', 'diff', '--check'])
    if res.returncode != 0:
        fail('git-diff-check', res.stdout + res.stderr)
    else:
        ok('git-diff-check')

# 4. No stale Pixel canonical URL
stale_hits = []
for p in text_files():
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for forbidden in FORBIDDEN_TEXT:
        if forbidden in txt:
            stale_hits.append(str(p.relative_to(ROOT)))
if stale_hits:
    fail('canonical-owner-okjpg', ', '.join(sorted(set(stale_hits))))
else:
    ok('canonical-owner-okjpg')

# 5. Secret-like scan
secret_hits = []
for p in text_files():
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for pat in SECRET_PATTERNS:
        if pat.search(txt):
            secret_hits.append(str(p.relative_to(ROOT)))
            break
if secret_hits:
    fail('secret-like-scan', ', '.join(secret_hits))
else:
    ok('secret-like-scan')

# 6. Skill integrity
skill_files = sorted((ROOT / 'skills').glob('**/SKILL.md'))
if len(skill_files) < 3:
    fail('skills-count', f'expected >=3, got {len(skill_files)}')
else:
    bad = []
    for p in skill_files:
        txt = p.read_text(encoding='utf-8')
        if not txt.startswith('---') or '\n---' not in txt[3:]:
            bad.append(f'{p.relative_to(ROOT)}: no frontmatter')
            continue
        fm = txt[3:txt.find('\n---', 3)]
        if not re.search(r'^name:\s*\S+', fm, re.M):
            bad.append(f'{p.relative_to(ROOT)}: missing name')
        if not re.search(r'^description:\s*.*Use quando', fm, re.M | re.I):
            bad.append(f'{p.relative_to(ROOT)}: description lacks Use quando')
    if bad:
        fail('skill-integrity', '; '.join(bad))
    else:
        ok(f'skill-integrity ({len(skill_files)} skills)')

# 7. Markdown local links
broken_links = []
for p in ROOT.rglob('*.md'):
    if '.git' in p.parts:
        continue
    txt = p.read_text(encoding='utf-8', errors='ignore')
    for raw in MD_LINK_RE.findall(txt):
        target, _frag = urldefrag(raw.strip())
        if not target or re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target):
            continue
        if target.startswith('#'):
            continue
        candidate = (p.parent / target).resolve()
        try:
            candidate.relative_to(ROOT)
        except ValueError:
            broken_links.append(f'{p.relative_to(ROOT)} -> {raw} escapes repo')
            continue
        if not candidate.exists():
            broken_links.append(f'{p.relative_to(ROOT)} -> {raw}')
if broken_links:
    fail('markdown-local-links', '; '.join(broken_links))
else:
    ok('markdown-local-links')

# 8. Install script E2E copy + validate copied workspace
with tempfile.TemporaryDirectory(prefix='agent-os-stress-') as tmp:
    target = Path(tmp) / 'installed-agent-os'
    res = run(['bash', 'scripts/install-agent-os.sh', str(target)], timeout=120)
    if res.returncode != 0:
        fail('install-script-copy', res.stdout + res.stderr)
    elif not (target / 'README.md').exists():
        fail('install-script-copy', 'README.md missing in installed copy')
    else:
        ok('install-script-copy')
        res2 = subprocess.run([sys.executable, 'scripts/validate-agent-os.py'], cwd=target, text=True, capture_output=True, timeout=60)
        if res2.returncode != 0:
            fail('installed-copy-validate', res2.stdout + res2.stderr)
        else:
            ok('installed-copy-validate')
        if (target / '.git').exists():
            fail('install-script-no-git-copy', '.git should not be copied')
        else:
            ok('install-script-no-git-copy')

# 9. README contains canonical clone URL
readme = (ROOT / 'README.md').read_text(encoding='utf-8') if (ROOT / 'README.md').exists() else ''
if 'https://github.com/okjpg/agent-os-hermes' not in readme:
    fail('readme-canonical-url', 'missing https://github.com/okjpg/agent-os-hermes')
else:
    ok('readme-canonical-url')

print('\nSUMMARY')
print(f'- checks passed: {len(checks)}')
print(f'- failures: {len(failures)}')
for item in failures:
    print(f'FAIL: {item}')

sys.exit(1 if failures else 0)
