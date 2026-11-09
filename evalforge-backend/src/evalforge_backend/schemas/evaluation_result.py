from uuid import UUID
from pydantic import BaseModel, ConfigDict, Field

class EvaluationResult(BaseModel):
    model_config = ConfigDict(extra = "forbid")
    
    evaluation_id: UUID
    task_id: str = Field(min_length = 1)
    passed: bool = Field(strict = True)
    reward: float = Field(ge = 0.0, le = 1.0)