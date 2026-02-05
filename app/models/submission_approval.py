from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Enum
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.db.session import Base
from app.utils.enums import Status, ApprovalAction

class Submission(Base):
    __tablename__ = "submissions"

    id = Column(Integer, primary_key=True, index=True)
    form_id = Column(Integer, ForeignKey("forms.id"), nullable=False)
    form_version_id = Column(Integer, ForeignKey("form_versions.id"), nullable=False)
    submitted_by = Column(Integer, ForeignKey("users.id"), nullable=False)
    status = Column(Enum(Status, native_enum=False), default=Status.DRAFT, nullable=False)
    current_step_id = Column(Integer, ForeignKey("workflow_steps.id"), nullable=False)
    submitted_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    form = relationship("Form", back_populates="submission")
    form_version = relationship("FormVersion", back_populates="submission")
    user = relationship("User", back_populates="submission")
    step = relationship("WorkflowStep", back_populates="submission")
    data = relationship("SubmissionData", back_populates="submission", cascade="all, delete-orphan")
    approval = relationship("ApprovalTask", back_populates="submission", cascade="all, delete-orphan")
    approval_log = relationship("ApprovalLog", back_populates="submission", cascade="all, delete-orphan")


class SubmissionData(Base):
    __tablename__ = "submission_data"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"), nullable=False)
    data = Column(JSONB)

    submission = relationship("Submission", back_populates="data")


class ApprovalTask(Base):
    __tablename__ = "approval_tasks"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"), nullable=False)
    workflow_step_id = Column(Integer, ForeignKey("workflow_steps.id"), nullable=False)
    assigned_to_role = Column(Integer, ForeignKey("roles.id", ondelete="SET NULL"), nullable=True)
    status = Column(Enum(Status, native_enum=False), default=Status.PENDING, nullable=False)

    submission = relationship("Submission", back_populates="approval")
    step = relationship("WorkflowStep", back_populates="approval")
    role = relationship("Role", back_populates="approval")


class ApprovalLog(Base):
    __tablename__ = "approval_logs"

    id = Column(Integer, primary_key=True, index=True)
    submission_id = Column(Integer, ForeignKey("submissions.id"), nullable=False)
    workflow_step_id = Column(Integer, ForeignKey("workflow_steps.id"), nullable=False)
    action = Column(Enum(ApprovalAction, native_enum=False), nullable=False)
    action_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    comment = Column(String, nullable=True)
    action_at = Column(DateTime(timezone=True), server_default=func.now(), nullable=False)

    submission = relationship("Submission", back_populates="approval_log")
    step = relationship("WorkflowStep", back_populates="approval_log")
    user = relationship("User", back_populates="approval_log")