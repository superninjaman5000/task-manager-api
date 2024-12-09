from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "postgresql+asyncpg://taskuser:taskpassword@db:5432/taskdb"

# Asynchronous engine for database connection
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# Sessionmaker for async sessions
async_session = sessionmaker(engine, expire_on_commit=False, class_=AsyncSession)

# Function to initialize the database
async def init_db():
    async with engine.begin() as conn:
        # Create all tables defined in models
        await conn.run_sync(Base.metadata.create_all)
