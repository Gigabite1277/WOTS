# form_a5: Entity-relationship diagram

Based on `blog/migrations/0005_commentvote.py` (Django migration), including
the existing `POST`, `COMMENT`, and configured `AUTH_USER` entities.

```mermaid
erDiagram
    AUTH_USER ||--o{ POST : "authors"
    AUTH_USER ||--o{ COMMENT : "writes"
    AUTH_USER ||--o{ COMMENT_VOTE : "casts"
    POST ||--o{ COMMENT : "has"
    COMMENT ||--o{ COMMENT_VOTE : "receives"

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

    COMMENT_VOTE {
        bigint id PK
        smallint value "1 Upvote, -1 Downvote"
        datetime created_on "not null; auto-created"
        bigint comment_id FK "not null"
        bigint user_id FK "not null"
    }
```

## Relationship details

- One `AUTH_USER` can cast zero or many `COMMENT_VOTE` records.
- One `COMMENT` can receive zero or many `COMMENT_VOTE` records.
- Every `COMMENT_VOTE` belongs to exactly one `AUTH_USER` through `user_id`.
- Every `COMMENT_VOTE` belongs to exactly one `COMMENT` through `comment_id`.
- A user can have at most one vote for a given comment, enforced by the
  `unique_comment_vote` constraint on `(comment_id, user_id)`.
- `COMMENT_VOTE.value` must be `1` (`Upvote`) or `-1` (`Downvote`).
- `COMMENT_VOTE.created_on` is set automatically when a vote is created.
- Deleting an `AUTH_USER` cascades and deletes their votes.
- Deleting a `COMMENT` cascades and deletes its votes.
- `AUTH_USER` represents Django's configured `settings.AUTH_USER_MODEL`; its concrete table and fields depend on the project's authentication configuration.
