#!/usr/bin/env python3
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_ROOT = [
    'AGENTS.md', 'SOUL.md', 'USER.md', 'MAPA.md', 'MEMORY.md',
    'TOOLS.md', 'PROPAGATION.md', 'HERMES.md', 'README.md', 'agent-os.yaml'
]
SECRET_PATTERNS = [
    re.compile(r'ghp_[A-Za-z0-9_]{20,}'),
    re.compile(r'github_pat_[A-Za-z0-9_]{20,}'),
    re.compile(r'sk-[A-Za-z0-9_-]{20,}'),
    re.compile(r'(?i)(api[_-]?key|password|secret|token)\s*[:=]\s*["\']?[A-Za-z0-9_./+=-]{12,}'),
    re.compile(r'BEGIN (RSA |OPENSSH |EC |DSA )?PRIVATE KEY'),
]

errors: list[str] = []
warnings: list[str] = []

for rel in REQUIRED_ROOT:
    if not (ROOT / rel).exists():
        errors.append(f'arquivo obrigatório ausente: {rel}')

skill_files = sorted((ROOT / 'skills').glob('**/SKILL.md'))
if not skill_files:
    errors.append('nenhuma skill encontrada em skills/**/SKILL.md')

for skill in skill_files:
    text = skill.read_text(encoding='utf-8')
    if not text.startswith('---'):
        errors.append(f'{skill.relative_to(ROOT)} sem frontmatter YAML')
        continue
    end = text.find('\n---', 3)
    if end == -1:
        errors.append(f'{skill.relative_to(ROOT)} frontmatter não fechado')
        continue
    fm = text[3:end]
    if not re.search(r'^name:\s*\S+', fm, re.M):
        errors.append(f'{skill.relative_to(ROOT)} sem name no frontmatter')
    desc = re.search(r'^description:\s*(.+)', fm, re.M)
    if not desc:
        errors.append(f'{skill.relative_to(ROOT)} sem description no frontmatter')
    elif not re.search(r'Use quando|Use when', desc.group(1), re.I):
        warnings.append(f'{skill.relative_to(ROOT)} description deveria começar com gatilho "Use quando"')

for path in ROOT.glob('**/*'):
    if '.git' in path.parts or path.is_dir():
        continue
    if path.suffix.lower() not in {'.md', '.yaml', '.yml', '.txt', '.py', '.sh', '.example'}:
        continue
    text = path.read_text(encoding='utf-8', errors='ignore')
    for pat in SECRET_PATTERNS:
        if pat.search(text):
            errors.append(f'possível segredo em {path.relative_to(ROOT)}')
            break

print('Agent OS validation')
print(f'- root: {ROOT}')
print(f'- skills: {len(skill_files)}')
print(f'- errors: {len(errors)}')
print(f'- warnings: {len(warnings)}')

for item in warnings:
    print(f'WARN: {item}')
for item in errors:
    print(f'ERROR: {item}')

if errors:
    sys.exit(1)
print('OK')
