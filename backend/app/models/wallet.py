from sqlalchemy import Column, Integer, String, Numeric, ForeignKey, Enum as SQLEnum, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import WalletType

class Wallet(Base):
    __tablename__ = "wallets"

    wallet_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    type = Column(SQLEnum(WalletType), nullable=False)
    balance = Column(Numeric(15, 2), default=0)  # Derived column
    currency = Column(String(10), default="VND")
    is_active = Column(Boolean, default=True)
    credit_limit = Column(Numeric(15, 2), default=0)

    user = relationship("User", back_populates="wallets")
    transactions = relationship("Transaction", back_populates="wallet")
    investments = relationship("Investment", back_populates="wallet")
    subscriptions = relationship("Subscription", back_populates="default_wallet")
