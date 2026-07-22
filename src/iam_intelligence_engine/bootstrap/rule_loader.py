from iam_intelligence_engine.domain.rules.administrator_access import (
    AdministratorAccessRule,
)
from iam_intelligence_engine.domain.rules.full_service_access import (
    FullServiceAccessRule,
)
from iam_intelligence_engine.domain.rules.not_action import NotActionRule
from iam_intelligence_engine.domain.rules.not_resource import NotResourceRule
from iam_intelligence_engine.domain.rules.pass_role import PassRoleRule
from iam_intelligence_engine.domain.rules.registry import RuleRegistry
from iam_intelligence_engine.domain.rules.wildcard_action import (
    WildcardActionRule,
)
from iam_intelligence_engine.domain.rules.wildcard_resource import (
    WildcardResourceRule,
)


class RuleLoader:
    """
    Creates and configures the default RuleRegistry.
    """

    @staticmethod
    def load() -> RuleRegistry:
        registry = RuleRegistry()

        registry.register(WildcardActionRule())
        registry.register(WildcardResourceRule())
        registry.register(AdministratorAccessRule())
        registry.register(NotActionRule())
        registry.register(NotResourceRule())
        registry.register(FullServiceAccessRule())
        registry.register(PassRoleRule())

        return registry