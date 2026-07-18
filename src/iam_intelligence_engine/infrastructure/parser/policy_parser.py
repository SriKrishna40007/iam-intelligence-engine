from iam_intelligence_engine.domain.models.policy import Policy
from iam_intelligence_engine.domain.models.statement import Statement


class PolicyParser:
    """
    Converts IAM policy dictionaries into domain objects.
    """

    def parse(self, data: dict) -> Policy:
        """
        Convert a Python dictionary into a Policy domain object.
        """

        statements: list[Statement] = []

        for statement_data in data.get("Statement", []):

            action = statement_data.get("Action", [])
            resource = statement_data.get("Resource", [])

            if isinstance(action, str):
                action = [action]

            if isinstance(resource, str):
                resource = [resource]

            statement = Statement(
                effect=statement_data["Effect"],
                actions=action,
                resources=resource,
            )

            statements.append(statement)

        return Policy(
            version=data["Version"],
            statements=statements,
        )