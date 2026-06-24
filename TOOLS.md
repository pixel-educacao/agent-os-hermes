# TOOLS.md — ferramentas e permissões

Este arquivo define quais ferramentas o agente pode usar e com quais limites.

## Regra geral

Use ferramentas quando a resposta depender de estado real:

- arquivo;
- Git;
- terminal;
- web atual;
- API;
- cálculo;
- validação;
- deploy;
- banco de dados.

Não responda “de cabeça” quando uma ferramenta pode verificar.

## Ferramentas comuns no Hermes

| Ferramenta | Uso |
|---|---|
| `terminal` | comandos, testes, Git, scripts |
| `read_file` | ler arquivos |
| `write_file` | criar/substituir arquivos |
| `patch` | edição cirúrgica |
| `search_files` | buscar arquivos/trechos |
| `web_search` | fatos atuais e pesquisa |
| `web_extract` | ler páginas/documentos |
| `cronjob` | tarefas recorrentes |
| `delegate_task` | subagentes para trabalho paralelo |
| `image_generate` | gerar imagens, se disponível |
| `text_to_speech` | gerar áudio, se disponível |

## Ações autônomas permitidas

- Ler arquivos do workspace.
- Rodar validações locais não destrutivas.
- Criar rascunhos em `docs/`, `memory/`, `examples/` e `skills/` quando solicitado.
- Buscar documentação pública.
- Criar commits locais quando o usuário pediu versionamento.

## Ações com aprovação

- Push para GitHub.
- Publicação externa.
- Envio de mensagem/email/post.
- Alteração de agenda/CRM/billing/DNS/deploy.
- Criação de cron recorrente.
- Exclusão permanente.

## Segredos

Nunca versionar:

```text
.env
*.pem
*.key
credentials.json
auth.json
tokens.json
```

Use `.env.example` para mostrar nomes de variáveis sem valores reais.
