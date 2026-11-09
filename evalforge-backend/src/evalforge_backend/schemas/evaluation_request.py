from pydantic import BaseModel, ConfigDict, Field


class EvaluationRequest(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    
    task_id: str = Field(min_length = 1)
    prompt: str = Field(min_length = 1)
    candidate_output: str 
    expected_output: str 
    
    