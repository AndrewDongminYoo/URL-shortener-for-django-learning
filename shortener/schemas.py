from shortener.models import Organization
from ninja import Schema
from ninja.orm import create_schema

OrganizationSchema = create_schema(Organization)


class Users(Schema):
    id: int
    full_name: str = None
    organization: OrganizationSchema = None


class TelegramUpdateSchema(Schema):
    username: str
