# Agent OS para Hermes

> Um sistema operacional mínimo para transformar um agente Hermes em um **executor com contexto, critérios, skills e trilhos** — não só um chatbot com personalidade.

Este repositório é um material prático para alunos e operadores que querem sair do “prompt perfeito” e montar um **sistema de trabalho com IA**.

A tese:

> O futuro não é prompt engineering.
> É **work-system design**.

Prompt bom ajuda. Um Agent OS bem montado cria contexto, organiza memória, carrega skills certas, respeita limites, executa tarefas com ferramentas e verifica resultado.

---

## Para quem é

Este material é para você se quer:

- criar um agente pessoal ou de negócio no Hermes;
- organizar os arquivos raiz que definem identidade, contexto e operação;
- ensinar o agente a saber **quando usar cada skill**;
- reduzir prompt repetido;
- transformar tarefas recorrentes em processos reutilizáveis;
- ter um repositório-base para adaptar para alunos, clientes ou empresa.

Não é um pacote mágico. É um esqueleto operacional.

---

## O que vem aqui

```text
.
├── AGENTS.md                         # contrato operacional lido pelo agente
├── SOUL.md                           # identidade/persona do agente
├── USER.md                           # perfil do humano/cliente atendido
├── MAPA.md                           # mapa de navegação do repositório
├── MEMORY.md                         # memória longa curada, sem segredos
├── TOOLS.md                          # ferramentas e integrações permitidas
├── PROPAGATION.md                    # onde salvar cada tipo de informação
├── HERMES.md                         # como usar este Agent OS dentro do Hermes
├── agent-os.yaml                     # manifesto legível por humanos e agentes
├── docs/                             # guias completos para aluno/operador
├── skills/                           # skills exemplo no formato SKILL.md
├── templates/                        # modelos para criar seu próprio Agent OS
├── examples/                         # exemplos práticos preenchidos
└── scripts/                          # validação local e instalação opcional
```

---

## Instalação rápida no Hermes

### Opção A — usar como referência

```bash
git clone https://github.com/okjpg/agent-os-hermes.git
cd agent-os-hermes
```

Depois copie o que fizer sentido para o repositório do seu agente.

### Opção B — copiar para um workspace novo

```bash
git clone https://github.com/okjpg/agent-os-hermes.git meu-agent-os
cd meu-agent-os
python3 scripts/validate-agent-os.py
```

Depois personalize:

1. `USER.md` — quem o agente atende.
2. `SOUL.md` — quem o agente é.
3. `TOOLS.md` — o que ele pode usar.
4. `PROPAGATION.md` — onde ele deve salvar cada coisa.
5. `skills/` — processos recorrentes.

### Opção C — pedir para o próprio Hermes instalar/adaptar

Abra o Hermes no terminal ou Telegram e cole:

```text
Você é um agente Hermes. Use este repositório como base de Agent OS:
https://github.com/okjpg/agent-os-hermes

Tarefa:
1. Leia README.md, HERMES.md, AGENTS.md e MAPA.md.
2. Faça perguntas só sobre o que for necessário para personalizar.
3. Adapte USER.md, SOUL.md, TOOLS.md e PROPAGATION.md para o meu caso.
4. Crie 3 skills iniciais para minhas tarefas recorrentes.
5. Rode scripts/validate-agent-os.py.
6. Mostre um resumo do que ficou pronto e quais arquivos eu devo revisar.
```

---

## Como o Hermes usa isso

Rode uma sessão dentro da pasta do projeto:

```bash
cd meu-agent-os
hermes
```

Ou em uma pergunta única:

```bash
cd meu-agent-os
hermes chat -q "Leia AGENTS.md e me ajude a personalizar este Agent OS"
```

A lógica principal é:

1. **Arquivos raiz** dão identidade e roteamento.
2. **Skills** dão procedimentos reutilizáveis.
3. **Memória** guarda continuidade curada.
4. **Docs** explicam para humanos e agentes como operar.
5. **Scripts** verificam se a estrutura está íntegra.

---

## A regra mais importante

> Arquivo raiz não é depósito de tudo.
> Arquivo raiz é bootloader.

O agente não precisa carregar o mundo inteiro sempre. Ele precisa saber:

- quem ele é;
- quem ele serve;
- onde procurar contexto;
- quando chamar uma skill;
- quais ações exigem aprovação;
- onde salvar cada tipo de informação.

---

## Como criar uma skill útil

Uma skill boa responde quatro coisas:

1. **Quando usar** — gatilhos claros.
2. **O que fazer** — passos objetivos.
3. **Como verificar** — evidência real, não “parece certo”.
4. **Quando parar/perguntar** — limites e riscos.

Exemplo mínimo:

```yaml
---
name: pesquisa-rapida
description: Use quando o usuário pedir uma pesquisa objetiva sobre tema atual, ferramenta, concorrente ou tecnologia.
---
```

Depois o corpo explica o procedimento.

Veja exemplos em [`skills/`](skills/).

---

## Ordem recomendada para personalizar

1. Leia [`docs/01-manifesto.md`](docs/01-manifesto.md).
2. Preencha [`USER.md`](USER.md).
3. Ajuste [`SOUL.md`](SOUL.md).
4. Defina regras em [`TOOLS.md`](TOOLS.md).
5. Defina propagação em [`PROPAGATION.md`](PROPAGATION.md).
6. Rode:

```bash
python3 scripts/validate-agent-os.py
python3 scripts/stress-test-agent-os.py
```

7. Crie suas primeiras skills com [`templates/SKILL-TEMPLATE.md`](templates/SKILL-TEMPLATE.md).

---

## O que este repo NÃO é

Não é:

- “100 prompts para ChatGPT”;
- resumo acadêmico de paper;
- persona bonitinha sem operação;
- framework abstrato demais;
- material que só humano entende.

O diferencial aqui é:

> Humano entende.
> IA consegue ler.
> Aluno consegue aplicar.

---

## Checklist de pronto

Antes de usar com alunos/clientes:

- [ ] `USER.md` não contém dados privados sensíveis.
- [ ] `MEMORY.md` não contém senha, token, chave ou segredo.
- [ ] `TOOLS.md` separa ações autônomas de ações com aprovação.
- [ ] `PROPAGATION.md` diz onde salvar ideias, decisões, tarefas e aprendizados.
- [ ] Cada skill tem `name` e `description` no frontmatter.
- [ ] `python3 scripts/validate-agent-os.py` passa.
- [ ] O agente consegue explicar quando usaria cada skill.

---

## Licença e uso

Material educacional criado pela Amora/Bruno Okamoto. Você pode estudar, adaptar e usar como base para seu próprio agente. Não redistribua como produto pago sem autorização.
