from enum import Enum

class FormCode(str, Enum):
    LEAVE_REQUEST = "LEAVE_REQUEST"
    EXPENSE_FORM = "EXPENSE_FORM"


class Status(str, Enum):
    DRAFT = "DRAFT"
    ACTIVE = "ACTIVE"
    ARCHIVED = "ARCHIVED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class FormFieldDataType(str, Enum):
    TEXT = "TEXT"
    NUMBER = "NUMBER"
    DATE = "DATE"
    SELECT = "SELECT"


class FieldRuleType(str, Enum):
    MIN = "MIN"
    MAX = "MAX"
    REGEX = "REGEX"
    LENGTH = "LENGTH"

class FieldConditionAction(str, Enum):
    SHOW = "SHOW"
    HIDE = "HIDE"
    REQUIRE = "REQUIRE"
    DISABLE = "DISABLE"


class PolicyType(str, Enum):
    VALIDATION = "VALIDATION"
    WORKFLOW = "WORKFLOW"
    AUTO_ACTION = "AUTO_ACTION"


class PolicyAction(str, Enum):
    AUTO_APPROVE = "AUTO_APPROVE"
    SET_APPROVER = "SET_APPROVER"


class Priority(str, Enum):
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"


class WorkflowStepType(str, Enum):
    AUTO = "AUTO"
    APPROVAL = "APPROVAL"


class ApprovalAction(str, Enum):
    APPROVE = "APPROVE"
    REJECT = "REJECT"