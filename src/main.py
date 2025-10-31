"""Facade module preserving public import path `src.main`.

Delegates to runtime.main to keep the same entry point.
"""

from .runtime.main import main  # noqa: F401

if __name__ == "__main__":
    main()
