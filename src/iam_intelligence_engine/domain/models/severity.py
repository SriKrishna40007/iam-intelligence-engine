from enum import StrEnum


class Severity(StrEnum):
    """
    Represents the severity classification of a security finding.
    """

    CRITICAL = "CRITICAL"
    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"
    INFO = "INFO"