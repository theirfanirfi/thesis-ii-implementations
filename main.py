import os.path
import xml.etree.ElementTree as ET
from pprint import pprint

from core.ClassesBuilder import ClassesBuilder
from core.Class_ import Class_
from core.KnowledgeSources.KnowledgeSource import KnowledgeSource
from core.KnowledgeSources.ORMGenerator.ORM_KSource import ORM_KSource
from core.KnowledgeSources.RoutesGenerator.Routes_KSource import Routes_KSource
from core.Operation import Operation_
from core.Relation import Relation
from core.Variables import Variable

tree = ET.parse('classdiagrams/company_project.xml')
root = tree.getroot()

models = root.find('Models')

associations = models.findall('Association')
generalizations = models.findall('Generalization')


model_children = models.find('Model').find('ModelChildren')
classes = model_children.findall('Class')
# print(classes)
classesGenerate = []
classesBuilder: ClassesBuilder = []
relations: Relation = []


def getClassById(class_id: str) -> Class_:
    for cls in classesGenerate:
        if cls.class_id == class_id:
            return cls


for assoc in associations:
    relation = Relation().perform_extraction(assoc.attrib, "Association")
    relations.append(relation)



for generalization in generalizations:
    relationG = Relation().perform_extraction(generalization.attrib, "Generalization")
    relations.append(relationG)

# for rr in relations:
#     print('rr', rr.relation_type)

def getRelationByClassId(class_id: str) -> Relation:
    for r in relations:
        if not r is None:
            if r.to_class == class_id:
                return r
    return None

for c in classes:
    # print('\n ********* ',c.attrib['Name'], c.attrib['Visibility'], ' ****** \n')
    class_ = Class_()

    class_.setClassId(c.attrib['Id'])
    class_.setClassName(c.attrib['Name'])
    class_.setClassVisibility(c.attrib['Visibility'])

    class_model_children = c.find('ModelChildren')
    if not class_model_children is None:
        class_attributes = class_model_children.findall('Attribute')
        class_operations = class_model_children.findall('Operation')

        for attr in class_attributes:
            class_.setClassInstanceVariable(Variable().perform_extraction(attr))
            # print(attr.attrib['Name'], attr.attrib['Type'], attr.attrib['Visibility'], '\n')

        for op in class_operations:
            # print(op.attrib)
            if not op is None:
                # print(op.attrib)
                operation = Operation_()
                operation.perform_extraction(op)
                # print('\n',op.attrib['Name'],
                #       op.attrib['ReturnType'] if 'ReturnType' in op.attrib else op.attrib['ReturnTypeDocumentation_plain'],
                #       attr.attrib['Scope'],
                #       op.attrib['Visibility'])
                parameters_model = op.find('ModelChildren')
                if not parameters_model is None:
                    operation_parameters = parameters_model.findall('Parameter')
                    for parameter in operation_parameters:
                        operation.setParameter(Variable().perform_extraction(parameter))
                        # print(parameter.attrib['Name'], parameter.attrib['Type'])

                class_.setClassOperation(operation)

        classesGenerate.append(class_)
        determined_relation = getRelationByClassId(class_.class_id)

        builder = ClassesBuilder()
        builder.setClass(class_)
        if not determined_relation is None:
            print('relation is not none ', relation.relation_type)
            builder = builder.setClass(class_).\
                setRelation(determined_relation)

        classesBuilder.append(builder)


# # pprint(classesBuilder)
# for g in classesBuilder:
#     print(g.class_.class_name)
#     if g.relations:
#         pprint(g.relations)
#         for x in g.relations:
#             print(x.relation_type)
#             if x.relation_type == "Association" and x.to_class == g.class_.class_id:
#                 print('Association ',g.class_.class_id, ' ', getClassById(x.from_class).class_name, ' ', x.to_class)
#             elif x.relation_type == "Generalization" and x.to_class == g.class_.class_id:
#                 print('Generalization ',g.class_.class_id, ' ', getClassById(x.from_class).class_name, ' ', x.to_class)
#
#     print('\n')



### broadcast classes

from core.KnowledgeSources.BLGenerator.BL_Source import BLSource

language = "python"
framework = "flask"
files_extension = "py"

if not os.path.isdir("targets/"+language):
    print("Do not target the language")
else:
    if not os.path.isdir("targets/"+language+"/"+framework):
        print("Do not target the framework")


knowledgesources: KnowledgeSource = [BLSource, ORM_KSource, Routes_KSource]

for ks in knowledgesources:
    ks().generate(language, framework, classesBuilder, files_extension)
