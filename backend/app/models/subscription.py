from sqlalchemy import Column, Integer, String, ForeignKey, Enum as SQLEnum, Numeric, Date, Boolean
from sqlalchemy.orm import relationship
from app.db.database import Base
from app.models.enums import FrequencyType

class Subscription(Base):
    __tablename__ = "subscriptions"

    subscription_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.user_id", ondelete="CASCADE"), nullable=False)
    default_wallet_id = Column(Integer, ForeignKey("wallets.wallet_id"), nullable=False)
    category_id = Column(Integer, ForeignKey("categories.category_id"), nullable=False)
    name = Column(String(150), nullable=False)
    amount = Column(Numeric(15, 2), nullable=False)
    frequency = Column(SQLEnum(FrequencyType), nullable=False)
    next_due_date = Column(Date, nullable=True)
    is_active = Column(Boolean, default=True)

    user = relationship("User", back_populates="subscriptions")
    default_wallet = relationship("Wallet", back_populates="subscriptions")
    category = relationship("Category", back_populates="subscriptions")
