from sqlalchemy import Table, Column, Integer, String, ForeignKey
from database.db import metadata

subscription = Table(
    "subscription",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, unique=True),
    Column("price", int),
    Column("model_id", Integer, ForeignKey("model.id")),  # Chave estrangeira da model
    Column("active", bool),
)