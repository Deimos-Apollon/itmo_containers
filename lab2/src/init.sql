CREATE TABLE IF NOT EXISTS jupyter_logs (
    id SERIAL PRIMARY KEY,
    event_time TIMESTAMP NOT NULL DEFAULT NOW(),
    event_type VARCHAR(50) NOT NULL
);

INSERT INTO jupyter_logs (event_type) VALUES ('system_initialized');