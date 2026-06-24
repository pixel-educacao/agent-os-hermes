# Prompt de instalação/adaptação

Cole este prompt em uma sessão Hermes aberta dentro deste repositório.

```text
Você está dentro de um repositório Agent OS para Hermes.

Objetivo:
Adaptar este Agent OS para meu uso real.

Antes de agir:
1. Leia AGENTS.md, SOUL.md, USER.md, MAPA.md, TOOLS.md e PROPAGATION.md.
2. Leia docs/02-estrutura-do-repositorio.md e docs/03-como-criar-skills.md.
3. Não invente acesso, ferramenta ou credencial.
4. Não salve segredo em arquivo versionado.

Meu contexto:
- Nome:
- Projeto/negócio:
- Objetivo principal:
- Tarefas recorrentes:
- Ferramentas que uso:
- O agente pode fazer sozinho:
- O agente deve pedir aprovação antes de:

Tarefas:
1. Atualize USER.md com meu contexto.
2. Ajuste SOUL.md para o tipo de agente que preciso.
3. Ajuste TOOLS.md e PROPAGATION.md.
4. Crie 3 skills iniciais em skills/.
5. Crie uma rotina de verificação em memory/tasks.md.
6. Rode python3 scripts/validate-agent-os.py.
7. Me entregue um resumo do que foi alterado e o que falta configurar.
```
