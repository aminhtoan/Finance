from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import CategoryType

class Category(Base):
    __tablename__ = "categories"

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=True)  # Null = System Default
    parent_id = Column(Integer, ForeignKey("categories.category_id", ondelete="CASCADE"), nullable=True)
    name = Column(String(100), nullable=False)
    type = Column(SQLEnum(CategoryType), nullable=False)
    icon = Column(String(255), nullable=True)

    user = relationship("User", back_populates="categories")
    transactions = relationship("Transaction", back_populates="category")
    subscriptions = relationship("Subscription", back_populates="category")
    budgets = relationship("Budget", back_populates="category")

    # Self-referential relationship (Đệ quy danh mục Cha - Con)
    parent = relationship("Category", remote_side=[category_id], back_populates="subcategories")
    subcategories = relationship("Category", back_populates="parent")
