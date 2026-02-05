from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import func
from app.db.session import Base
from app.utils.enums import PolicyType, PolicyAction, Priority

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    policy_type = Column(Enum(PolicyType, native_enum=False), nullable=False)
    status = Column(String, nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    form = relationship("Form", back_populates="policy")
    rule = relationship("Rule", back_populates="policy", cascade="all, delete-orphan")


class Rule(Base):
    __tablename__ = "rules"

    id = Column(Integer, primary_key=True, index=True)
    policy_id = Column(Integer, ForeignKey("policies.id"), nullable=False)
    condition_expression = Column(String, nullable=True)
    action_type = Column(Enum(PolicyAction, native_enum=False), nullable=False)
    action_value = Column(JSONB)
    priority = Column(Enum(Priority, native_enum=False), nullable=False)
    is_active = Column(Boolean, default=True)

    policy = relationship("Policy", back_populates="rule")