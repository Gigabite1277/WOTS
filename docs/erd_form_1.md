# Form 1: Entity-relationship diagram

Based on `blog/migrations/0001_initial.py` (Django migration).

```mermaid
erDiagram
    AUTH_USER ||--o{ POST : "authors"

    AUTH_USER {
        bigint id PK
    }

    POST {
        bigint id PK
        varchar title UK "max 200"
        varchar slug UK "max 200"
        bigint author_id FK "not null"
    }
```

## Relationship details

- One `AUTH_USER` can author zero or many `POST` records.
- Every `POST` belongs to exactly one `AUTH_USER` through `author_id`.
- Deleting an `AUTH_USER` cascades and deletes their `POST` records.
- `POST.title` and `POST.slug` are each unique.
- `AUTH_USER` represents Django's configured `settings.AUTH_USER_MODEL`; its concrete table and fields depend on the project's authentication configuration.
