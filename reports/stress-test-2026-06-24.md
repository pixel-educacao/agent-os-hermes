# Stress test — Agent OS para Hermes

Data: 2026-06-24 09:19 BRT
Repo canônico: https://github.com/okjpg/agent-os-hermes
Commit testado: ver histórico do GitHub; este report acompanha o commit de release.

## Resultado

Status: **APROVADO para soltar para alunos**.

## Bateria executada

| Camada | Teste | Resultado |
|---|---|---:|
| Estrutura | root files obrigatórios existem | ✅ |
| Validador | `python3 scripts/validate-agent-os.py` | ✅ `OK` |
| Stress local | `python3 scripts/stress-test-agent-os.py` | ✅ 11 checks / 0 failures |
| Python | `py_compile` dos scripts | ✅ |
| Git hygiene | `git diff --check` | ✅ |
| Canonical owner | busca por URL antiga da org Pixel | ✅ sem hits |
| Secrets | scan local de padrões tipo token/private key | ✅ sem hits |
| Skills | 6 `SKILL.md` com frontmatter e gatilho `Use quando` | ✅ |
| Links internos | links Markdown locais resolvem | ✅ |
| Instalação | `scripts/install-agent-os.sh` copia para temp | ✅ |
| Cópia instalada | validação da cópia instalada | ✅ |
| Git leakage | `.git` não é copiado pela instalação | ✅ |
| Clone remoto | clone fresh de `okjpg/agent-os-hermes` | ✅ |
| Stress remoto | stress test no clone remoto | ✅ 11 checks / 0 failures |
| Smoke Hermes | `hermes chat -q 'Responda exatamente: OK_AGENT_OS_REMOTE' --toolsets safe -Q` | ✅ |

## Observação operacional

O repo nasceu por engano na organização Pixel, mas foi canonizado em `okjpg/agent-os-hermes`. A cópia Pixel recebeu o commit com links apontando para o repo canônico, mas a URL para divulgar é:

https://github.com/okjpg/agent-os-hermes
