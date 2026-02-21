"""
Compatibility shim for legacy camelCase import.

This module aliases `pyDOE` ---> `pydoe`.
"""

import importlib
import sys
import warnings


warnings.warn(
    "Importing `pyDOE` is deprecated and will be removed in a future release. "
    "Please import `pydoe` instead.",
    DeprecationWarning,
    stacklevel=2,
)

# Import the real package
_real_pkg = importlib.import_module("pydoe")

# Replace this module in sys.modules with the real one
sys.modules[__name__] = _real_pkg

# Ensure submodules resolve correctly
# (critical for `import pyDOE.something`)
_real_pkg.__name__ = __name__
