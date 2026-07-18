from collections.abc import Iterable

from iam_intelligence_engine.domain.rules.base import BaseRule


class RuleRegistry:
    """
    Stores and provides access to all registered security rules.
    """

    def __init__(self) -> None:
        self._rules: list[BaseRule] = []

    def register(self, rule: BaseRule) -> None:
        self._rules.append(rule)

    def all(self) -> list[BaseRule]:
        return list(self._rules)

    def __iter__(self) -> Iterable[BaseRule]:
        return iter(self._rules)

    def __len__(self) -> int:
        return len(self._rules)
