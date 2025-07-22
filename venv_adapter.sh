#!/bin/bash

# Check argument
if [ "$1" = "a" ]; then
  echo "🔄 Activating virtual environment..."
  source venv/bin/activate
elif [ "$1" = "d" ]; then
  echo "🛑 Deactivating virtual environment..."
  deactivate
else
  echo "❌ Usage: ./venv_control.sh [a|d]"
  echo "a = activate, d = deactivate"
fi
