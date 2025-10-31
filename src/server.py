"""Facade module preserving public import path `src.server`.

This thin wrapper re-exports the FastAPI app and helpers from runtime.server
to maintain the existing public endpoint surface and startup commands.
"""

from .runtime.server import app, get_server_config  # noqa: F401
