import pytest
from uuid import UUID
from evalforge_backend.db.connection import get_db_connection
from evalforge_backend.schemas.evaluation_result import EvaluationResult
from evalforge_backend.db.repository import get_evaluation_by_id


def test_get_evaluation_by_id():
    
    test_id = UUID("e6fb4430-9334-4ff1-9b01-6fdcd4901090")
    with get_db_connection() as conn:
        with conn.cursor() as cur:
            cur.execute(
                "SELECT evaluation_id, task_id, passed, reward FROM evaluations WHERE evaluation_id = %s;",
                (test_id,)
            )
            row = cur.fetchone()
            
            assert row is not None
            assert row[1] == "task_001"
            assert row[2] == True
            assert row [3] == 1.0
            

def test_get_evaluation_by_id_function():
    test_id = UUID("e6fb4430-9334-4ff1-9b01-6fdcd4901090")
    eval_result = get_evaluation_by_id(test_id)
    
    assert eval_result.evaluation_id == UUID("e6fb4430-9334-4ff1-9b01-6fdcd4901090")
    assert test_id == eval_result.evaluation_id
    assert eval_result.task_id == "task_001"
    assert eval_result.passed == True
    assert eval_result.reward == 1.0