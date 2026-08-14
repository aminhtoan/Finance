from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum, Numeric, Date
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import InvestmentType

class Investment(Base):
    __tablename__ = "investments"

    investment_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    wallet_id = Column(Integer, ForeignKey("wallets.wallet_id"), nullable=False)
    name = Column(String(150), nullable=False)
    type = Column(SQLEnum(InvestmentType), nullable=False)
    quantity = Column(Numeric(20, 8), nullable=False, default=1)
    principal_amount = Column(Numeric(15, 2), nullable=False)
    current_value = Column(Numeric(15, 2), nullable=True)
    total_passive_income = Column(Numeric(15, 2), default=0)
    start_date = Column(Date, nullable=True)

    user = relationship("User", back_populates="investments")
    wallet = relationship("Wallet", back_populates="investments")
