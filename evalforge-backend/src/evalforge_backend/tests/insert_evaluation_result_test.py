import pytest
import psycopg
import pytest

from uuid import uuid4
from evalforge_backend.schemas.evaluation_result import EvaluationResult
from evalforge_backend.db.connection import get_db_connection
from evalforge_backend.db.repository import insert_evaluation_result


def test_insert_evaluation_result():
    test_id = uuid4()
    eval_result = EvaluationResult(
        evaluation_id = test_id,
        task_id = "task_001",
        passed = True,
        reward = 1.0,
    )
    
    eval_result_id = insert_evaluation_result(eval_result)
    assert eval_result == test_id

    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur = conn.Execute(
                "SELECT task_id, passed, reward FROM evaluations WHERE evaluation_id = %s;",
                (test_id)
            )
            row = cur.fetchone()
            assert row is not None
            assert row[0] == uuid4
            assert row[1] == "task_001"
            assert row[2] == True
            assert row[3] == 1.0
            

