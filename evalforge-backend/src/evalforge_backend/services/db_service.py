#!/usr/bin/env python3
"""
Database Service File
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------


# ---------- Project Level Imports ----------
from evalforge_backend.db.connection import get_db_connection

# ---------- Begin File ----------


def verify_db_service_active() -> bool:
    
    with get_db_connection() as conn:
        
        is_active = not conn.closed
        return is_active