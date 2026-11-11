#!/usr/bin/env python3
"""
Evaluation Result insertion into SQL Database
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------
from typing import Optional

# ---------- Third Party Imports ----------
from psycopg.rows import dict_row
from uuid import UUID

# ---------- Project Level Imports ----------
from evalforge_backend.db.connection import get_db_connection
from evalforge_backend.schemas.evaluation_result import EvaluationResult

# ---------- Begin File ----------

def insert_evaluation_result(evaluationresult: EvaluationResult) -> UUID:
    """
    Inserts the evaluationresult into the evaluations table and returns the generated database UUID
    """
    
    query = """
        INSERT INTO evaluations (
            evaluation_id,
            task_id,
            passed,
            reward
        )
        VALUES( %s, %s, %s, %s)
        RETURNING evaluation_id;
    """
    params = (
        evaluationresult.evaluation_id,
        evaluationresult.task_id,
        evaluationresult.passed,
        evaluationresult.reward
    )
    
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(query, params)
            row = cur.fetchone()
            assert row is not None
            return row[0]
        
        
def get_evaluation_by_id(evaluation_id: UUID) -> Optional[EvaluationResult]:
    """
    Retrieves an evaluation record by its PRIMARY KEY UUID
    Returns NONE if no matching record is found.
    """
    
    query = """
        SELECT evaluation_id, task_id, passed, reward
        FROM evaluations
        WHERE evaluation_id = %s;
    """
    with get_db_connection() as conn:
        with conn.cursor(row_factory = dict_row) as cur:
            cur.execute(query, (evaluation_id,))
            row = cur.fetchone()
            if row is None:
                return None
            return EvaluationResult(**row)
        

    