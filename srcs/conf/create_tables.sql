CREATE SEQUENCE IF NOT EXISTS posts_id_seq;

CREATE TABLE IF NOT EXISTS posts (
    id SERIAL PRIMARY KEY,
    text CHAR(150000),
    rubrics CHAR(100) NOT NULL,
    created_date TIMESTAMP
);

COPY posts (text, created_date, rubrics)
FROM '/docker-entrypoint-initdb.d/posts.csv'
DELIMITER ',' CSV HEADER;
