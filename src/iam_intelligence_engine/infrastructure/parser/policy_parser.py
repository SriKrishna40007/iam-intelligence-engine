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

            actions = statement_data.get("Action", [])
            not_actions = statement_data.get("NotAction", [])

            resources = statement_data.get("Resource", [])
            not_resources = statement_data.get("NotResource", [])

            if isinstance(actions, str):
                actions = [actions]

            if isinstance(not_actions, str):
                not_actions = [not_actions]

            if isinstance(resources, str):
                resources = [resources]

            if isinstance(not_resources, str):
                not_resources = [not_resources]

            statement = Statement(
                effect=statement_data["Effect"],
                actions=actions,
                not_actions=not_actions,
                resources=resources,
                not_resources=not_resources,
                conditions=statement_data.get("Condition", {}),
                sid=statement_data.get("Sid"),
            )

            statements.append(statement)

        return Policy(
            version=data["Version"],
            statements=statements,
        )
