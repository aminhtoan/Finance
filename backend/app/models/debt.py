from sqlalchemy import Column, Integer, String, Numeric, Date, Boolean, ForeignKey, Enum as SQLEnum, Float, DateTime
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import DebtType

class Debt(Base):
    __tablename__ = "debts"

    debt_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    creditor_name = Column(String(150), nullable=False)
    total_amount = Column(Numeric(15, 2), nullable=False)
    remaining_amount = Column(Numeric(15, 2), default=0)  # Derived
    type = Column(SQLEnum(DebtType), nullable=False)
    interest_rate = Column(Float, nullable=True)
    due_date = Column(Date, nullable=True)
    is_installment = Column(Boolean, default=False)

    user = relationship("User", back_populates="debts")
    repayments = relationship("DebtRepayment", back_populates="debt", cascade="all, delete-orphan")


class DebtRepayment(Base):
    __tablename__ = "debt_repayments"

    repayment_id = Column(Integer, primary_key=True, autoincrement=True)
    debt_id = Column(Integer, ForeignKey("debts.debt_id", ondelete="CASCADE"), nullable=False)

    # unique=True tạo quan hệ 1-1 với bảng transactions
    transaction_id = Column(Integer, ForeignKey("transactions.transaction_id"), nullable=False, unique=True)

    amount = Column(Numeric(15, 2), nullable=False)
    date = Column(DateTime(timezone=True), nullable=False, default=func.now())

    debt = relationship("Debt", back_populates="repayments")
    transaction = relationship("Transaction", back_populates="debt_repayment")
