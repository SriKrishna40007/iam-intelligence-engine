from dataclasses import dataclass

from iam_intelligence_engine.domain.models.severity import Severity


@dataclass(frozen=True, slots=True)
class Finding:
    """
    Represents the outcome of evaluating a single security rule
    against an IAM policy.
    """

    rule_id: str
    rule_name: str
    severity: Severity
    message: str
    description: str
    resource: str
    recommendation: str
    passed: bool