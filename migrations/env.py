from logging.config import fileConfig
from sqlalchemy import engine_from_config, pool
from alembic import context
# Import the Base class that your models inherit from
from lib.models import Base, User, Post  # Adjust the import based on your project structure

# Alembic Config object, which provides access to the values within the .ini file
config = context.config

# Set up logging
fileConfig(config.config_file_name)

# Point to the metadata of your Base class
target_metadata = Base.metadata

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
    connectable = engine_from_config(
        config.get_section(config.config_ini_section),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
