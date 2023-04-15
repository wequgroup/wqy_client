CREATE TABLE alembic_version (
    version_num VARCHAR(32) NOT NULL, 
    CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num)
);

-- Running upgrade  -> 3f87b73f28d4

CREATE TABLE device (
    device_id VARCHAR NOT NULL, 
    device_password VARCHAR DEFAULT '' NOT NULL, 
    device_name VARCHAR DEFAULT '' NOT NULL,
    auto_online VARCHAR DEFAULT 'off' NOT NULL,
    PRIMARY KEY (device_id)
);

CREATE TABLE record (
    record_id VARCHAR NOT NULL, 
    record_content VARCHAR DEFAULT '' NOT NULL, 
    record_name VARCHAR DEFAULT '' NOT NULL, 
    PRIMARY KEY (record_id)
);

CREATE TABLE storage_var (
    id INTEGER NOT NULL, 
    "key" VARCHAR NOT NULL, 
    value VARCHAR DEFAULT '' NOT NULL, 
    remark VARCHAR DEFAULT '' NOT NULL, 
    created_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
    updated_at DATETIME DEFAULT (CURRENT_TIMESTAMP), 
    PRIMARY KEY (id)
);

CREATE INDEX ix_storage_var_key ON storage_var ("key");

INSERT INTO alembic_version (version_num) VALUES ('3f87b73f28d4') RETURNING version_num;

