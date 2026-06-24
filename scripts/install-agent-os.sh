#!/usr/bin/env bash
set -euo pipefail

TARGET="${1:-}"
if [[ -z "$TARGET" ]]; then
  echo "Uso: scripts/install-agent-os.sh /caminho/do/novo-agent-os"
  exit 1
fi

mkdir -p "$TARGET"
rsync -av \
  --exclude '.git/' \
  --exclude '.env' \
  --exclude '__pycache__/' \
  ./ "$TARGET"/

echo "Agent OS copiado para: $TARGET"
echo "Próximo passo: cd $TARGET && python3 scripts/validate-agent-os.py"
