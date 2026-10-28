from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class EvalContract(BaseModel):
    id: UUID = Field(default_factory = uuid4)
    task_id: str = Field(..., description = "Unique task ID")
    prompt: str = Field(..., description = "Input prompt")
    expected_output: str = Field(..., description = "expected_output")