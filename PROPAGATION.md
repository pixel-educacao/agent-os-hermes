# PROPAGATION.md — protocolo de escrita

Informação que fica só no chat se perde. Este arquivo define onde salvar cada coisa.

## Regra-mãe

Mudou estado? Salve no lugar certo.

## Tabela de propagação

| Quando acontecer | Escrever em |
|---|---|
| Nova decisão | `memory/decisions.md` |
| Nova tarefa | `memory/tasks.md` |
| Nova ideia | `memory/ideas.md` |
| Novo aprendizado reutilizável | `memory/lessons.md` ou `skills/` |
| Novo procedimento recorrente | `skills/{categoria}/{nome}/SKILL.md` |
| Novo material explicativo | `docs/` |
| Exemplo prático | `examples/` |
| Modelo reutilizável | `templates/` |
| Conteúdo antigo | `archive/` |

## Regras

- Não criar arquivo solto na raiz sem motivo forte.
- Não salvar logs crus quando um resumo basta.
- Não salvar segredos.
- Não duplicar a mesma fonte de verdade.
- Se uma informação for usada por humanos e agentes, escreva em Markdown claro.

## Formato de decisão

```md
## AAAA-MM-DD — título da decisão

**Contexto:** por que isso foi decidido.
**Decisão:** o que vale agora.
**Consequência:** o que muda na prática.
**Revisar quando:** condição de revisão.
```

## Formato de tarefa

```md
- [ ] Tarefa — dono — prazo — contexto mínimo
```

## Formato de aprendizado

```md
## Aprendizado

**Sinal:** quando isso aparece.
**Regra:** o que fazer.
**Exemplo:** caso concreto.
**Virou skill?** sim/não.
```
