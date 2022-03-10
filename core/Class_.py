from core.Operation import Operation_
from core.Variables import Variable
class Class_:
    def __init__(self):
        self.class_id: str = None
        self.class_name: str = None
        self.operations: Operation_ = []
        self.instance_variables: Variable = []
        self.static_variables: Variable = []
        self.visibility: str

    def setClassId(self, class_id: str):
        self.class_id = class_id
        return self

    def setClassName(self, class_name: str):
        self.class_name = class_name
        return self

    def setClassVisibility(self, visibility: str):
        self.visibility = visibility
        return self

    def setClassOperation(self, operation: Operation_):
        self.operations.append(operation)
        return self

    def setClassInstanceVariable(self, variable: Variable):
        self.instance_variables.append(variable)
        return self


    def setClassStaticVariable(self, variable: Variable):
        self.static_variables.append(variable)
        return self


