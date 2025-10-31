"""Main entry point for Katalon Knowledge Agent."""

import uvicorn

from .server import app, get_server_config


def main() -> None:
    """Run the Katalon Knowledge Agent server."""
    config = get_server_config()
    uvicorn.run(
        app,
        host=config["host"],
        port=config["port"],
    )


if __name__ == "__main__":
    main()

