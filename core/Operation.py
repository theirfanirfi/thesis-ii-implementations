from core.utils.utils import generate_random_string
from core.Variables import Variable
class Operation_:
#{'Abstract': 'false', 'BacklogActivityId': '0', 'BodyCondition_IsNull': 'true', 'ConnectToCodeModel': '1', 'Documentation_plain': '', 'Id': 'joqSBP6FYEB2uQXn', 'Leaf': 'false', 'Lower_IsNull': 'true', 'Name': 'setTitle', 'Ordered': 'false', 'PmAuthor': 'Visual Paradigm', 'PmCreateDateTime': '2017-08-24T09:28:52.921', 'PmLastModified': '2022-02-22T12:15:50.909', 'QualityReason_IsNull': 'true', 'QualityScore': '-1', 'Query': 'false', 'ReturnTypeDocumentation_plain': '', 'Scope': 'instance', 'Static': 'false', 'TypeModifier': '', 'Unique': 'true', 'Upper_IsNull': 'true', 'UserIDLastNumericValue': '0', 'UserID_IsNull': 'true', 'Visibility': 'public', 'Visible': 'true'}

    def __init__(self):
        self.id: str
        self.name: str
        self.return_type: str
        self.scope: str
        self.visibility: str
        self.parameters: Variable = []
        self._raw_operation: dict

    def perform_extraction(self, raw_operation: dict):
        self._raw_operation = raw_operation
        self.id = generate_random_string(10)
        self.name = self._raw_operation.attrib['Name']
        self.return_type = self._raw_operation.attrib['ReturnType'] if 'ReturnType' in \
                                                                       self._raw_operation.attrib \
            else self._raw_operation.attrib['ReturnTypeDocumentation_plain']
        self.scope = self._raw_operation.attrib['Scope']
        self.visibility = self._raw_operation.attrib['Visibility']
        return self

    def setParameter(self, variable: Variable):
        self.parameters.append(variable)
        return self

