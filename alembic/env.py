import os
from sqlalchemy import create_engine
from sqlalchemy import pool
from alembic import context

# Получаем URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/db")

# Настройка Alembic
config = context.config

# Устанавливаем sqlalchemy.url динамически
config.set_main_option("sqlalchemy.url", DATABASE_URL)

target_metadata = None  # Укажите вашу metadata, если используется

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        config.get_main_option("sqlalchemy.url"),
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
