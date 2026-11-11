CREATE TABLE evaluations (
    evaluation_id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    task_id TEXT NOT NULL CHECK (task_id != ''),
    passed BOOLEAN NOT NULL,
    reward DOUBLE PRECISION NOT NULL,
    CONSTRAINT valid_reward CHECK (
        reward >= 0.0 AND reward <= 1.0
    )
);