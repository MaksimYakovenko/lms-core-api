# conftest.py — scaffolded by ai-factory.
# Adds the workspace root to sys.path so `from src.<pkg> import X` works
# in pytest regardless of the working directory at invocation time.
import pathlib
import sys

_root = str(pathlib.Path(__file__).parent)
if _root not in sys.path:
    sys.path.insert(0, _root)
