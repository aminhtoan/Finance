from sqlalchemy import Column, Integer, ForeignKey, Enum as SQLEnum, Numeric, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import BudgetPeriod

class Budget(Base):
    __tablename__ = "budgets"

    budget_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    amount_limit = Column(Numeric(15, 2), nullable=False)
    period = Column(SQLEnum(BudgetPeriod), nullable=False)
    is_rollover = Column(Boolean, default=False)
    start_date = Column(Date, nullable=True)
    end_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="budgets")
    category = relationship("Category", back_populates="budgets")
