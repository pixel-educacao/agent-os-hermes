# Personalização passo a passo

Use este guia para transformar o template em seu próprio Agent OS.

## Passo 1 — Defina o humano

Edite `USER.md`.

O agente precisa saber:

- quem você é;
- quais projetos importam;
- como você prefere resposta;
- quais tarefas se repetem;
- quais limites são inegociáveis.

## Passo 2 — Defina o agente

Edite `SOUL.md`.

Escolha:

- papel;
- tom;
- nível de proatividade;
- limites;
- estilo de decisão.

## Passo 3 — Defina ferramentas

Edite `TOOLS.md`.

Separe:

- ferramentas disponíveis;
- ações autônomas;
- ações com aprovação;
- segredos nunca versionados.

## Passo 4 — Defina propagação

Edite `PROPAGATION.md`.

Sem isso, o agente não sabe onde salvar ideias, decisões e tarefas.

## Passo 5 — Crie 3 skills iniciais

Sugestão:

1. Rotina diária.
2. Pesquisa rápida.
3. Criar conteúdo.

Use `templates/SKILL-TEMPLATE.md`.

## Passo 6 — Valide

```bash
python3 scripts/validate-agent-os.py
```

Corrija erros antes de usar em produção.

## Passo 7 — Rode uma sessão de teste

```bash
hermes chat -q "Leia este Agent OS e me diga como você operaria uma rotina diária amanhã"
```

O agente deve citar arquivos e skills relevantes.
