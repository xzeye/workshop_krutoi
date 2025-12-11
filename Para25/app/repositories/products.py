from sqlalchemy.ext.asyncio import AsyncSession
from app.models.products import Product, ProductCreate, ProductUpdate

async def create_product(session: AsyncSession,
    product_create: ProductCreate) -> Product:
    product_data = product_create.model_dump()
    new_product = Product(**product_data)
    session.add(new_product)
    await session.commit()
    return new_product

async def update_products(session: AsyncSession,
    product_db: Product,
    product_update: ProductUpdate) -> Product:
    product_data = product_update.model_dump(exclude_unset=True)
    for key, value in product_data.items():
        setattr(product_db, key, value)
    await session.commit()
    return product_db

async def get_product_by_id(session: AsyncSession,
    product_id: int) -> Product | None:
    return await session.get(Product, product_id)