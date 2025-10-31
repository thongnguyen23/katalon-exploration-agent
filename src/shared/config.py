"""Shared configuration utilities for Katalon Knowledge Agent."""

import os
from typing import Optional

from dotenv import load_dotenv


def load_config() -> None:
    """Load configuration from .env files.
    
    Loads defaults from .env.defaults first, then overrides from .env.
    """
    # Load defaults first
    if os.path.exists(".env.defaults"):
        load_dotenv(".env.defaults")
    
    # Override with user config
    if os.path.exists(".env"):
        load_dotenv(".env", override=True)


def get_env(key: str, default: Optional[str] = None) -> str:
    """Get environment variable value.
    
    Args:
        key: Environment variable name
        default: Default value if not set (raises if None and not found)
        
    Returns:
        Environment variable value
        
    Raises:
        ValueError: If variable not found and no default provided
    """
    value = os.getenv(key, default)
    if value is None:
        raise ValueError(f"Required environment variable {key} not set")
    return value


def get_env_int(key: str, default: Optional[int] = None) -> int:
    """Get environment variable as integer.
    
    Args:
        key: Environment variable name
        default: Default value if not set
        
    Returns:
        Environment variable value as integer
    """
    value = os.getenv(key)
    if value is None:
        if default is None:
            raise ValueError(f"Required environment variable {key} not set")
        return default
    return int(value)


def get_env_bool(key: str, default: bool = False) -> bool:
    """Get environment variable as boolean.
    
    Args:
        key: Environment variable name
        default: Default value if not set
        
    Returns:
        Environment variable value as boolean
    """
    value = os.getenv(key)
    if value is None:
        return default
    return value.lower() in ("true", "1", "yes", "on")
