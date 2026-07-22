import json

from iam_intelligence_engine.application.correlation_engine import CorrelationEngine
from iam_intelligence_engine.application.executive_summary_engine import (
    ExecutiveSummaryEngine,
)
from iam_intelligence_engine.application.risk_score_engine import RiskScoreEngine
from iam_intelligence_engine.application.rule_engine import RuleEngine
from iam_intelligence_engine.bootstrap.rule_loader import RuleLoader
from iam_intelligence_engine.domain.models.executive_summary import ExecutiveSummary
from iam_intelligence_engine.infrastructure.parser.policy_parser import PolicyParser


class AnalysisService:
    """
    Orchestrates the complete IAM policy analysis workflow.
    """

    def __init__(self) -> None:
        self._parser = PolicyParser()

        registry = RuleLoader.load()
        self._rule_engine = RuleEngine(registry)

        self._correlation_engine = CorrelationEngine()
        self._risk_engine = RiskScoreEngine()
        self._summary_engine = ExecutiveSummaryEngine()

    def analyze(self, policy_path: str) -> ExecutiveSummary:
        with open(policy_path, encoding="utf-8") as file:
            data = json.load(file)

        policy = self._parser.parse(data)

        findings = self._rule_engine.evaluate(policy)

        correlations = self._correlation_engine.correlate(findings)

        risk_score = self._risk_engine.calculate(findings)

        return self._summary_engine.build(
            findings=findings,
            correlations=correlations,
            risk_score=risk_score,
        )