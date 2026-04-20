export PYTHONPATH=$PYTHONPATH:$(pwd)/src && python3 -m uvicorn src.gui.app:app --reload
