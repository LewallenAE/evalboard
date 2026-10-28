CREATE TABLE IF NOT EXISTS eval_contracts (
    id UUID PRIMARY KEY NOT NULL,
    task_id VARCHAR(255) NOT NULL,
    prompt TEXT NOT NULL,
    expected_output TEXT NOT NULL
);