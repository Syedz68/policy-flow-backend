from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base
from app.utils.enums import FormCode, Status

class Form(Base):
    __tablename__ = "forms"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    form_code = Column(Enum(FormCode, native_enum=False), nullable=False)
    description = Column(String, nullable=True)
    status = Column(Enum(Status, native_enum=False), default=Status.DRAFT, nullable=False)
    created_by = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    user = relationship("User", back_populates="form")
    version = relationship("FormVersion", back_populates="form", cascade="all, delete-orphan")
    policy = relationship("Policy", back_populates="form", cascade="all, delete-orphan")
    workflow = relationship("WorkFlow", back_populates="form", cascade="all, delete-orphan")
    submission = relationship("Submission", back_populates="form", cascade="all, delete-orphan")


class FormVersion(Base):
    __tablename__ = "form_versions"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    version_number = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    form = relationship("Form", back_populates="version")
    form_field = relationship("FormField", back_populates="version", cascade="all, delete-orphan")
    submission = relationship("Submission", back_populates="form_version", cascade="all, delete-orphan")