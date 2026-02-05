from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.db.session import Base
from app.utils.enums import WorkflowStepType

class WorkFlow(Base):
    __tablename__ = "workflows"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    name = Column(String, nullable=False)
    version = Column(String, nullable=False)
    status = Column(String, nullable=True)

    form = relationship("Form", back_populates="workflow")
    step = relationship("WorkflowStep", back_populates="workflow", cascade="all, delete-orphan")


class WorkflowStep(Base):
    __tablename__ = "workflow_steps"

    id = Column(Integer, primary_key=True, index=True)
    workflow_id = Column(Integer, ForeignKey("workflows.id"), nullable=False)
    step_order = Column(String, nullable=True)
    step_type = Column(Enum(WorkflowStepType, native_enum=False), nullable=False)
    role_required = Column(Integer, ForeignKey("roles.id", ondelete="SET NULL"), nullable=True)
    timeout_days = Column(Integer, nullable=False)

    workflow = relationship("WorkFlow", back_populates="step")
    role = relationship("Role", back_populates="step")
    submission = relationship("Submission", back_populates="step", cascade="all, delete-orphan")
    approval = relationship("ApprovalTask", back_populates="step", cascade="all, delete-orphan")
    approval_log = relationship("ApprovalLog", back_populates="step", cascade="all, delete-orphan")


class WorkflowTransition(Base):
    __tablename__ = "workflow_transitions"

    id = Column(Integer, primary_key=True, index=True)
    from_step_id = Column(Integer, ForeignKey("workflow_steps.id"), nullable=False)
    to_step_id = Column(Integer, ForeignKey("workflow_steps.id"), nullable=False)
    condition_expression = Column(String, nullable=True)