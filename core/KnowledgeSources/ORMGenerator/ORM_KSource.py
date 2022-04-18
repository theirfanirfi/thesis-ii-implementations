from core.ClassesBuilder import ClassesBuilder
from core.KnowledgeSources.KnowledgeSource import KnowledgeSource
import os
from core.KnowledgeSources.ORMGenerator.interfaces.ORMKS import ORMKS


class ORM_KSource(KnowledgeSource, ORMKS):

    def generate(self, language, framework, classesBuilder: ClassesBuilder, files_extension):
        os.mkdir("output/new1/Models")
        template = self.select_template(language, framework, "model")
        for cls in classesBuilder:
            output = template.render(cls=cls)
            self.create_source(output, cls.class_.class_name, files_extension)


    def create_source(self, output, class_name, files_extension):
        file = open("output/new1/Models/"+class_name+"."+files_extension,'w')
        file.write(output)
        file.close()
        return

