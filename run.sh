#!/bin/bash
# Optimized startup script for Linear Algebra Studio
# Reduces power consumption by disabling file watching (reload)
# and using a single worker for this lightweight application.

source ./.venv/bin/activate
export PYTHONPATH=$PYTHONPATH:$(pwd)/src

echo "Starting Linear Algebra Studio in Power-Saving Mode..."
echo "File watching (reload) is DISABLED."

# Run uvicorn without --reload for better power efficiency
python3 -m uvicorn src.gui.app:app --host 127.0.0.1 --port 8000 --workers 1 --no-access-log

# Old

# export PYTHONPATH=$PYTHONPATH:$(pwd)/src && python3 -m uvicorn src.gui.app:app --reload