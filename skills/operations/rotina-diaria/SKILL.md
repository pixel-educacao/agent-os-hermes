---
name: rotina-diaria
description: Use quando o usuário pedir planejamento do dia, priorização, top 3 tarefas, revisão de agenda, foco do dia ou organização de pendências.
---

# Rotina diária

## Quando usar

Use quando o usuário pedir:

- “planeja meu dia”;
- “quais são minhas prioridades?”;
- “faz minha rotina”;
- “organiza minhas pendências”;
- “top 3 de hoje”.

## Quando não usar

Não use para planejamento estratégico longo ou revisão semanal completa. Nesses casos, crie ou use uma skill específica.

## Passo a passo

1. Ler `memory/tasks.md`.
2. Ler `memory/decisions.md` se houver decisões recentes relevantes.
3. Identificar tarefas com prazo, impacto e bloqueio.
4. Separar em:
   - Top 3;
   - agenda/blocos;
   - pendências rápidas;
   - riscos.
5. Sugerir o menor plano executável do dia.

## Formato de resposta

```md
## Top 3
1. ...
2. ...
3. ...

## Blocos sugeridos
- Manhã:
- Tarde:
- Fechamento:

## Riscos
- ...
```

## Verificação

- [ ] O plano cabe no dia?
- [ ] Existe prioridade clara?
- [ ] Algo precisa de aprovação ou informação externa?
