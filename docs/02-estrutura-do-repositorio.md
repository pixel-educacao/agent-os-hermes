# Estrutura do repositório

Este repo foi desenhado para ser lido por humanos e agentes.

## Camada 1 — Root files

Root files ficam na raiz porque são o bootloader do agente.

- `AGENTS.md`: contrato operacional.
- `SOUL.md`: identidade.
- `USER.md`: humano atendido.
- `MAPA.md`: navegação.
- `MEMORY.md`: memória longa.
- `TOOLS.md`: ferramentas e permissões.
- `PROPAGATION.md`: onde escrever cada coisa.
- `HERMES.md`: instruções específicas para Hermes.

## Camada 2 — Docs

`docs/` explica o sistema para humanos e agentes.

Use para guias, decisões arquiteturais e material de aluno.

## Camada 3 — Skills

`skills/` contém procedimentos executáveis.

Padrão:

```text
skills/{categoria}/{nome}/SKILL.md
```

Cada skill deve ensinar:

- quando usar;
- quando não usar;
- inputs necessários;
- passo a passo;
- verificação;
- erros comuns.

## Camada 4 — Memory

`memory/` guarda continuidade curada.

Não é dump de conversa. É contexto que vale preservar.

## Camada 5 — Templates e examples

- `templates/`: modelos em branco.
- `examples/`: exemplos preenchidos.

## Camada 6 — Scripts

Scripts ajudam a validar e operar.

O principal é:

```bash
python3 scripts/validate-agent-os.py
```
