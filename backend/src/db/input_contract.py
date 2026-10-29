from pathlib import Path

from db.session import pool, establish_db_connection
from schemas.data_contracts import EvalContract

BASE_DIR = Path(__file__).resolve().parent.parent


async def main():
    contract = EvalContract(
        task_id = input("Task ID: "),
        prompt = input("Prompt: "),
        expected_output = input("Expected output: ")
    )
    async with pool:
        async with establish_db_connection() as conn:
            await conn.execute(
            "INSERT INTO eval_contracts (id, task_id, prompt, expected_output) VALUES (%s, %s, %s, %s)",(contract.id, contract.task_id, contract.prompt, contract.expected_output)
            )