# PostgreSQL

PostgreSQL is a powerful, open-source object-relational database system.

## Basic Commands (psql)
```bash
# Connect to a database
psql -U username -d database_name

# List databases
\l

# List tables
\dt

# Quit psql
\q
```

## Useful SQL Snippets

### Group Concat Equivalent
```sql
SELECT string_agg(column_name, ', ') FROM table_name;
```

### Upsert (Insert or Update)
```sql
INSERT INTO table_name (id, name)
VALUES (1, 'New Name')
ON CONFLICT (id) DO UPDATE SET name = EXCLUDED.name;
```

### JSON Operations
PostgreSQL has excellent support for JSONB.
```sql
-- Select from JSONB column
SELECT data->>'name' FROM users WHERE data @> '{"id": 1}';
```

## Running with Docker
```bash
docker run --name postgres-db \
  -e POSTGRES_PASSWORD=mysecretpassword \
  -p 5432:5432 \
  -d postgres
```

## Primary Features
- **ACID Compliant**: Reliable transactions.
- **Extensible**: Custom types and functions.
- **Rich Indexing**: B-tree, Hash, GIST, GIN.
- **Foreign Data Wrappers**: Connect to other databases.