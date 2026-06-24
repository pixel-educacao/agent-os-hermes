# HERMES.md — como usar este Agent OS no Hermes

Este arquivo explica como um agente Hermes deve operar este repositório.

## Início rápido

```bash
git clone https://github.com/okjpg/agent-os-hermes.git
cd agent-os-hermes
hermes
```

Dentro do Hermes, peça:

```text
Leia AGENTS.md, SOUL.md, USER.md, MAPA.md e me ajude a personalizar este Agent OS para meu negócio.
```

## Como o Hermes encontra contexto

O Hermes inclui contexto do workspace atual na sessão. Por isso, rode o agente dentro da pasta do seu Agent OS:

```bash
cd meu-agent-os
hermes
```

Para uma tarefa única:

```bash
hermes chat -q "Use este Agent OS e crie uma skill de rotina diária"
```

## Como instalar skills localmente

Skills deste repositório são exemplos. Para instalar uma skill real no Hermes, copie a pasta da skill para:

```text
~/.hermes/skills/{categoria}/{nome}/SKILL.md
```

Exemplo:

```bash
mkdir -p ~/.hermes/skills/operations
cp -R skills/operations/rotina-diaria ~/.hermes/skills/operations/
hermes skills list
```

Em uma sessão já aberta, reinicie ou recarregue skills quando disponível.

## Como o agente sabe quando usar uma skill

Cada `SKILL.md` tem frontmatter:

```yaml
---
name: rotina-diaria
description: Use quando o usuário pedir planejamento do dia, priorização, agenda ou top 3 tarefas.
---
```

A `description` é o gatilho. Escreva como se estivesse instruindo outro agente:

- “Use quando...”
- “Não use quando...”
- “Antes de executar, leia...”
- “Verifique com...”

## Comandos úteis do Hermes

```bash
hermes --version
hermes status --all
hermes doctor
hermes tools list
hermes skills list
hermes config path
hermes config env-path
```

## Slash commands úteis

Dentro de sessões Hermes/gateway, alguns comandos comuns são:

```text
/help          mostra ajuda
/status        status da sessão/gateway
/tools         gerencia ferramentas
/skill nome    carrega skill
/restart       reinicia gateway quando necessário
/update        atualiza Hermes quando disponível
```

A lista muda com o Hermes. Use `/help` como fonte viva.

## Padrão recomendado de sessão

1. Usuário pede algo.
2. Agente verifica se existe skill relevante.
3. Agente lê arquivos necessários.
4. Agente executa com ferramentas.
5. Agente valida.
6. Agente salva estado quando necessário.
7. Agente responde com resultado e evidência.

## Prompt de personalização

```text
Você está dentro do repo Agent OS.

Objetivo:
Criar um Agent OS para [meu negócio/projeto].

Contexto:
- Eu sou [perfil].
- Meu objetivo principal é [objetivo].
- Minhas tarefas recorrentes são [tarefas].
- O agente pode fazer sozinho [permissões].
- O agente deve perguntar antes de [limites].

Tarefa:
1. Atualize USER.md e SOUL.md.
2. Ajuste TOOLS.md e PROPAGATION.md.
3. Crie 3 skills iniciais.
4. Rode scripts/validate-agent-os.py.
5. Me entregue o resumo e os próximos passos.
```
