from dataclasses import dataclass, field


@dataclass(slots=True)
class Statement:
    """
    Represents a single IAM policy statement.
    """

    effect: str
    actions: list[str] = field(default_factory=list)
    resources: list[str] = field(default_factory=list)