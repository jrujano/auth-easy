# Import all the models, so that Base has them before being
# imported by Alembic
from app.db.base_class import Base
from app.models.animal import Animal
from fishauth.models.organization import Organization
from fishauth.models.user import User
