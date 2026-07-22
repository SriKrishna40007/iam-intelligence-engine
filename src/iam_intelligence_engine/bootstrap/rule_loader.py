from iam_intelligence_engine.domain.rules.registry import RuleRegistry
from iam_intelligence_engine.domain.rules.wildcard_action import WildcardActionRule
from iam_intelligence_engine.domain.rules.wildcard_resource import WildcardResourceRule
from iam_intelligence_engine.domain.rules.administrator_access import AdministratorAccessRule
from iam_intelligence_engine.domain.rules.not_action import NotActionRule
class RuleLoader:
    """
    Creates and configures the default RuleRegistry.
    """

    @staticmethod
    def load() -> RuleRegistry:
        registry = RuleRegistry()

        registry.register(WildcardActionRule())
        registry.register(WildcardActionRule())
        registry.register(WildcardResourceRule())
        registry.register(WildcardActionRule())
        registry.register(WildcardResourceRule())
        registry.register(AdministratorAccessRule())
        registry.register(NotActionRule())

        return registry
