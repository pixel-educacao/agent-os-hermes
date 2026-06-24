# MAPA.md — mapa de navegação do Agent OS

Este arquivo diz onde encontrar cada tipo de contexto.

## Arquivos raiz

| Arquivo | Função |
|---|---|
| `AGENTS.md` | Contrato operacional do agente |
| `SOUL.md` | Identidade, tom e limites |
| `USER.md` | Perfil do humano/cliente |
| `MAPA.md` | Este mapa de navegação |
| `MEMORY.md` | Memória longa curada |
| `TOOLS.md` | Ferramentas, integrações e permissões |
| `PROPAGATION.md` | Regras de escrita e persistência |
| `HERMES.md` | Instruções específicas para Hermes |
| `agent-os.yaml` | Manifesto estruturado |

## Pastas

```text
docs/       Guias para humanos e agentes
skills/     Procedimentos reutilizáveis
memory/     Continuidade curada
examples/   Exemplos preenchidos
templates/  Modelos para copiar
scripts/    Validações e automações locais
archive/    Conteúdo antigo, preservado
```

## Onde salvar cada coisa

| Tipo de informação | Destino |
|---|---|
| Ideia solta | `memory/ideas.md` |
| Decisão | `memory/decisions.md` |
| Pendência | `memory/tasks.md` |
| Aprendizado reutilizável | `memory/lessons.md` ou nova skill |
| Procedimento recorrente | `skills/{categoria}/{nome}/SKILL.md` |
| Material explicativo | `docs/` |
| Exemplo concreto | `examples/` |
| Modelo reutilizável | `templates/` |

## Como o agente deve navegar

1. Leia root files para entender o sistema.
2. Use `MAPA.md` para localizar contexto.
3. Carregue docs apenas quando a tarefa pedir.
4. Carregue skills quando houver gatilho claro.
5. Escreva no destino certo; não crie arquivos soltos na raiz.
