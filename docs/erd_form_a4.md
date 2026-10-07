# form_a4: Entity-relationship diagram

Based on `blog/migrations/0004_post_featured_image.py` (Django migration),
including the existing `POST`, `COMMENT`, and configured `AUTH_USER` entities.

```mermaid
erDiagram
    AUTH_USER ||--o{ POST : "authors"
    AUTH_USER ||--o{ COMMENT : "writes"
    POST ||--o{ COMMENT : "has"

    AUTH_USER {
        bigint id PK
    }

    POST {
        bigint id PK
        varchar title UK "max 200"
        varchar slug UK "max 200"
        bigint author_id FK "not null"
        varchar featured_image "max 255; default placeholder"
        text content "not null"
        datetime created_on "not null; auto-created"
        integer status "not null; 0 Draft, 1 Published"
        text excerpt "nullable"
        datetime updated_on "not null; auto-updated"
    }

    COMMENT {
        bigint id PK
        text body
        boolean approved "default false"
        datetime created_on "not null; auto-created"
        bigint author_id FK "not null"
        bigint post_id FK "not null"
    }
```

## Relationship details

- One `AUTH_USER` can author zero or many `POST` records.
- One `AUTH_USER` can write zero or many `COMMENT` records.
- One `POST` can have zero or many `COMMENT` records.
- Every `POST` belongs to exactly one `AUTH_USER` through `author_id`.
- Every `COMMENT` belongs to exactly one `AUTH_USER` through `author_id`.
- Every `COMMENT` belongs to exactly one `POST` through `post_id`.
- Deleting an `AUTH_USER` cascades and deletes their `POST` and `COMMENT` records.
- Deleting a `POST` cascades and deletes its `COMMENT` records.
- `POST.featured_image` stores the Cloudinary image value, allows up to 255 characters,
  and defaults to `placeholder`.
- `AUTH_USER` represents Django's configured `settings.AUTH_USER_MODEL`; its concrete table and fields depend on the project's authentication configuration.
