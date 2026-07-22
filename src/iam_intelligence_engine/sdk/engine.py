from iam_intelligence_engine.bootstrap.container import ApplicationContainer
from iam_intelligence_engine.application.dto.analysis_request import AnalysisRequest
from iam_intelligence_engine.application.dto.analysis_result import AnalysisResult


class IAMEngine:
    """
    Public SDK for the IAM Intelligence Engine.

    Consumers should interact only with this class instead of
    ApplicationContainer or AnalysisService.
    """

    def __init__(self) -> None:
        self._analysis_service = ApplicationContainer.build()

    def analyze(self, request: AnalysisRequest) -> AnalysisResult:
        """
        Analyze an IAM policy.

        Args:
            request: Analysis request.

        Returns:
            AnalysisResult
        """
        return self._analysis_service.analyze(request)