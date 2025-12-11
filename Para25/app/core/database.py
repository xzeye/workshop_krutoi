from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

DATABASE_ASYNC = 'sqlite+aiosqlite:///./product.db'
DATABASE_SYNC = 'sqlite:///./product.db'

engine = create_async_engine(url=DATABASE_ASYNC, echo=False)
AsyncSessionLocal = async_sessionmaker(bind=engine, expire_on_commit=False)