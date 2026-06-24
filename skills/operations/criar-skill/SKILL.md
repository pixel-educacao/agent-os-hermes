---
name: criar-skill
description: Use quando o usuário pedir para criar uma skill, transformar processo em procedimento reutilizável ou quando uma tarefa recorrente aparecer 2 ou mais vezes.
---

# Criar skill

## Quando usar

Use quando houver processo repetível.

## Passo a passo

1. Definir gatilho: quando a skill deve ser usada.
2. Definir limites: quando não usar.
3. Listar inputs necessários.
4. Escrever passo a passo.
5. Definir verificação.
6. Salvar em `skills/{categoria}/{nome}/SKILL.md`.
7. Rodar `python3 scripts/validate-agent-os.py`.

## Critério de boa skill

Uma skill boa permite que outro agente execute o processo sem perguntar tudo de novo.

## Verificação

- [ ] `name` e `description` existem.
- [ ] A description contém “Use quando”.
- [ ] Existe passo a passo.
- [ ] Existe verificação.
- [ ] Não contém segredo.
