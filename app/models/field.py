from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.utils.enums import FormFieldDataType, FieldRuleType, FieldConditionAction


class FormField(Base):
    __tablename__ = "form_fields"

    id = Column(Integer, primary_key=True, index=True)
    form_version_id = Column(Integer, ForeignKey("form_versions.id"), nullable=False)
    label = Column(String, nullable=False)
    field_key = Column(String, nullable=True)
    data_type = Column(Enum(FormFieldDataType, native_enum=False), default=FormFieldDataType.TEXT, nullable=False)
    required = Column(Boolean, default=False)
    default_value = Column(String, nullable=True)
    display_order = Column(String, nullable=True)
    is_active = Column(Boolean, default=True)

    version = relationship("FormVersion", back_populates="form_field")
    options = relationship("FieldOption", back_populates="field", cascade="all, delete-orphan")
    validations = relationship("FieldValidation", back_populates="field", cascade="all, delete-orphan")
    conditions = relationship("FieldCondition", back_populates="field", cascade="all, delete-orphan")


class FieldOption(Base):
    __tablename__ = "field_options"

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, ForeignKey("form_fields.id"), nullable=False)
    value = Column(String, nullable=False)
    label = Column(String, nullable=False)
    display_order = Column(String, nullable=True)

    field = relationship("FormField", back_populates="options")


class FieldValidation(Base):
    __tablename__ = "field_validations"

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, ForeignKey("form_fields.id"), nullable=False)
    rule_type = Column(Enum(FieldRuleType, native_enum=False), nullable=False)
    rule_value = Column(String, nullable=False)
    error_message = Column(String, nullable=True)

    field = relationship("FormField", back_populates="validations")


class FieldCondition(Base):
    __tablename__ = "field_conditions"

    id = Column(Integer, primary_key=True, index=True)
    field_id = Column(Integer, ForeignKey("form_fields.id"), nullable=False)
    condition_expression = Column(String, nullable=False)
    action = Column(Enum(FieldConditionAction, native_enum=False), nullable=False)

    field = relationship("FormField", back_populates="conditions")