from pydantic import BaseModel, Field
from uuid import UUID, uuid4

class EvalContract(BaseModel):
    id: UUID = Field(default_factory = uuid4)
    task_id: str
    prompt: str
    expected_output: str