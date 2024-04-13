from data_access.db_context.config.database import engine
from core.models.category import Category
from core.models.product import Product
from core.models.product_feature import ProductFeature


def create_tables():
    """
    Creates all database tables defined in the application.
    """
    Category.metadata.create_all(bind=engine)
    Product.metadata.create_all(bind=engine)
    ProductFeature.metadata.create_all(bind=engine)
