from iam_intelligence_engine.application.dto.analysis_request import AnalysisRequest
from iam_intelligence_engine.application.dto.analysis_result import AnalysisResult
from iam_intelligence_engine.config.logging import get_logger


logger = get_logger(__name__)


class AnalysisService:
    """
    Orchestrates the IAM policy analysis pipeline.

    All dependencies are injected by the ApplicationContainer.
    """

    def __init__(
        self,
        parser,
        rule_engine,
        correlation_engine,
        risk_engine,
        summary_engine,
    ) -> None:
        self._parser = parser
        self._rule_engine = rule_engine
        self._correlation_engine = correlation_engine
        self._risk_engine = risk_engine
        self._summary_engine = summary_engine

    def analyze(
        self,
        request: AnalysisRequest,
    ) -> AnalysisResult:
        logger.info("Parsing IAM policy")

        policy = self._parser.parse(request.policy_data)

        logger.info("Executing security rules")

        findings = self._rule_engine.evaluate(policy)

        logger.info("Detected %d findings", len(findings))

        correlations = self._correlation_engine.correlate(findings)

        risk_score = self._risk_engine.calculate(findings)

        logger.info(
            "Calculated overall risk score: %d",
            risk_score,
        )

        summary = self._summary_engine.build(
            findings=findings,
            correlations=correlations,
            risk_score=risk_score,
        )

        logger.info("Analysis completed")

        return AnalysisResult(summary=summary)
