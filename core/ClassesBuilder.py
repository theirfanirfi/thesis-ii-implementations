from core.Relation import Relation
from core.utils.utils import generate_random_string
from core.Class_ import Class_
class ClassesBuilder:

    def __init__(self):
        self.id: str
        self.class_: Class_
        self.intefaces : Class_ = []
        # self.inherited_classes: Class_ = []
        # self.child_classes: Class_ = []
        # self.associated_classes: Relation = []
        # self.generalizations: Relation = []
        self.relations: Relation = []


    def setClass(self, class_: Class_):
        self.class_  = class_
        return self

    def setInterface(self, interface_: Class_):
        self.class_.append(interface_)
        return self

    # def setChildClass(self, class_: Class_):
    #     self.child_classes.append(class_)
    #     return self
    #
    # def setInheritedClass(self, class_: Class_):
    #     self.inherited_classes.append(class_)
    #     return self
    #
    # def setAssociatedClass(self, relation: Relation):
    #     self.associated_classes.append(relation)
    #     return self
    #
    # def setGeneralization(self, relation: Relation):
    #     self.generalizations.append(relation)
    #     return self

    def setRelation(self, relation: Relation):
        self.relations.append(relation)
        return self

