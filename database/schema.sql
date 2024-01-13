CREATE TABLE IF NOT EXISTS files (
    file_id SERIAL PRIMARY KEY, -- maximum of 2147483648 entries
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    filename VARCHAR(255) NOT NULL,
    file_type VARCHAR(50) NOT NULL,
    size_mb DOUBLE PRECISION NOT NULL,
    username VARCHAR(32) NOT NULL, -- maximum of 32 characters as per discord api docs
    tags VARCHAR(255)[]
);
