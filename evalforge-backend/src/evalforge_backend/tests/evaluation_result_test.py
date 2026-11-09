#!/usr/bin/env python3
"""
Pytest file for Evaluation_Result Pydantic BaseModel Class

Pydantic BaseModel:

class EvaluationResult(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    
    evaluation_id: UUID
    task_id: str = Field(min_length = 1)
    passed: bool = Field(strict = True)
    reward: float = Field(ge = 0.0, le = 1.0)
"""

# ---------- Future Import ----------
from __future__ import annotations

# ---------- Standard Library Imports ----------
from uuid import UUID, uuid4

# ---------- Third Party Imports ----------
import pytest
from pydantic import ValidationError

# ---------- Project Level Imports ----------
from evalforge_backend.schemas.evaluation_result import EvaluationResult

# ---------- Begin File ----------

test_id = uuid4()


def test_valid_eval_result():
    valid_evaluation_result = EvaluationResult(
        evaluation_id = test_id, 
        task_id = "pre_model_task - 001", 
        passed = True, reward = 1.0
        )
    
    assert valid_evaluation_result.evaluation_id == test_id
    assert valid_evaluation_result.task_id == "pre_model_task - 001"
    assert valid_evaluation_result.passed == True
    assert valid_evaluation_result.reward == 1.0
    
    
def test_evaluation_result_missing_evaluation_id():
    with pytest.raises(ValidationError):
        EvaluationResult(
            task_id = "pre_model_task - 001", 
            passed = True, 
            reward = 1.0
            )
        
def test_evaluation_result_invalid_UUID():
    with pytest.raises(ValidationError):
        EvaluationResult(evaluation_id = "twenty 1", task_id = "string", passed = False, reward = 1.0)
        
def test_evaluation_result_empty_task_id():
    with pytest.raises(ValidationError):
        EvaluationResult(evaluation_id = test_id, task_id = "", passed = True, reward = 1.0)
            
def test_evaluation_result_missing_task_id():
    with pytest.raises(ValidationError):
        EvaluationResult(
            evaluation_id = test_id, 
            passed = True, 
            reward = 1
            )
    
    
def test_evaluation_result_passed_is_string_instead_of_bool():
    with pytest.raises(ValidationError):
        EvaluationResult(
            evaluation_id = test_id, 
            task_id = "GPT is being a fickle 001", 
            passed = "True", 
            reward = 1
            )
    
    
def test_evaluation_result_reward_outside_boundary_positive():
    with pytest.raises(ValidationError):
        EvaluationResult(
            evaluation_id = test_id, 
            task_id = "mrph", 
            passed = True, 
            reward = 1.5
            )

def test_evaluation_result_reward_outside_boundary_negative():
    with pytest.raises(ValidationError):
        EvaluationResult(
            evaluation_id = test_id, 
            task_id = "mrph", 
            passed = True, 
            reward = -0.5
            )
    
def test_evaluation_result_unexpected_field_rejected():
    with pytest.raises(ValidationError):
        EvaluationResult(
            evaluation_id = test_id, 
            task_id = "mrph", 
            passed = True, 
            reward = 0.5,
            model_task_id = "model_task_id = 001"
            )
    
    



    