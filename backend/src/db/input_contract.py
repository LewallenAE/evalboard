import asyncio

from ..db.session import pool, establish_db_connection
from ..schemas.data_contracts import EvalContract

contract = EvalContract()


async def main():
    async with pool:
        async with establish_db_connection() as conn:
            await conn.execute(
            "INSERT INTO eval_contracts (id, task_id, prompt, expected_output) VALUES (%s, %s, %s, %s)",(contract.id, contract.task_id, contract.prompt, contract.expected_output)
            )