from iam_intelligence_engine.application.analysis_service import AnalysisService
from iam_intelligence_engine.application.correlation_engine import CorrelationEngine
from iam_intelligence_engine.application.executive_summary_engine import (
    ExecutiveSummaryEngine,
)
from iam_intelligence_engine.application.risk_score_engine import (
    RiskScoreEngine,
)
from iam_intelligence_engine.application.rule_engine import RuleEngine
from iam_intelligence_engine.bootstrap.rule_loader import RuleLoader
from iam_intelligence_engine.infrastructure.parser.policy_parser import (
    PolicyParser,
)


class ApplicationContainer:
    """
    Composes the application's dependency graph.
    """

    @staticmethod
    def build() -> AnalysisService:
        registry = RuleLoader.load()

        parser = PolicyParser()

        rule_engine = RuleEngine(registry)

        correlation_engine = CorrelationEngine()

        risk_engine = RiskScoreEngine()

        summary_engine = ExecutiveSummaryEngine()

        return AnalysisService(
            parser=parser,
            rule_engine=rule_engine,
            correlation_engine=correlation_engine,
            risk_engine=risk_engine,
            summary_engine=summary_engine,
        )
