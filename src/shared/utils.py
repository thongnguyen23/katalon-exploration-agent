"""Shared utilities for Katalon Knowledge Agent."""

import logging
from typing import Any

logger = logging.getLogger(__name__)


def sanitize_log_data(data: Any) -> str:
    """Sanitize data for safe logging.
    
    Args:
        data: Data to sanitize
        
    Returns:
        Sanitized string representation
    """
    if isinstance(data, (dict, list)):
        return str(data)[:500]  # Truncate large objects
    return str(data)
