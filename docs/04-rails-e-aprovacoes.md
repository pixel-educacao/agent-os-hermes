# Rails e aprovações

Autonomia boa não é deixar o agente fazer qualquer coisa.

Autonomia boa é liberdade dentro de trilhos claros.

## Três zonas

### Verde — pode fazer sozinho

- Ler contexto.
- Criar rascunho local.
- Rodar teste não destrutivo.
- Buscar documentação pública.
- Atualizar memória quando solicitado.

### Amarelo — pode preparar, mas precisa aprovação

- Email, mensagem ou post externo.
- Push para repositório público.
- Cron recorrente.
- Alteração em material que será publicado.
- Mudança que afeta outras pessoas.

### Vermelho — não fazer sem escopo explícito

- Deletar dados.
- Resetar banco/servidor.
- Mexer em billing/DNS/firewall.
- Expor segredo.
- Responder por uma pessoa em canal público.

## Regra prática

Se a ação sai do ambiente local ou representa o humano publicamente, peça aprovação.

## Como escrever rails em skills

Inclua sempre:

```md
## Limites

- Pode fazer sozinho:
- Precisa perguntar antes:
- Nunca fazer:
```
