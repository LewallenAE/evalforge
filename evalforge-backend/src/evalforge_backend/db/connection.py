#!/usr/bin/env python3
"""
Database Connection Manager
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------


# ---------- Third Party Imports ----------
import os
import psycopg
from dotenv import load_dotenv


# ---------- Project Level Imports ----------


# ---------- Begin File ----------

load_dotenv()

def get_db_connection() -> psycopg.Connection:
    """
    Returns an open psycopg.Connection for warehouse operations.
    The caller is responsible for managing transaction and closure via 'with 
    """
    db_url = os.getenv("DB_URL")
    if not db_url:
        raise ValueError("DB_URL is not set or empty.")
    # Returns an open, un-entered connection
    return psycopg.connect(db_url)
    