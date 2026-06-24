# Como criar skills

Skill é um procedimento reutilizável.

Se uma tarefa aparece mais de uma vez, ela provavelmente merece uma skill.

## Anatomia de uma skill

```md
---
name: nome-da-skill
description: Use quando...
---

# Nome da skill

## Quando usar

## Quando não usar

## Inputs

## Passo a passo

## Verificação

## Erros comuns
```

## Escreva a descrição como gatilho

Ruim:

```yaml
description: Skill de conteúdo.
```

Bom:

```yaml
description: Use quando o usuário pedir um post de LinkedIn, thread, roteiro curto ou adaptação de ideia para conteúdo público.
```

## Skill boa é operacional

Ela não só explica. Ela guia execução.

Inclua:

- arquivos que devem ser lidos;
- comandos seguros;
- critérios de qualidade;
- quando pedir aprovação;
- como testar.

## Checklist

- [ ] Tem `name`.
- [ ] Tem `description` com gatilho.
- [ ] Diz quando usar e quando não usar.
- [ ] Tem passo a passo.
- [ ] Tem verificação.
- [ ] Não contém segredo.
- [ ] Cabe numa tarefa real.
