from core.ClassesBuilder import ClassesBuilder
from core.KnowledgeSources.KnowledgeSource import KnowledgeSource
import os
from core.KnowledgeSources.RoutesGenerator.interfaces.RoutesKS import RoutesKS


class Routes_KSource(KnowledgeSource, RoutesKS):

    def generate(self, language, framework, classesBuilder: ClassesBuilder, files_extension):
        os.mkdir("output/new1/Routes")
        template = self.select_template(language, framework, "routes")
        for cls in classesBuilder:
            output = template.render(cls=cls)
            self.create_source(output, cls.class_.class_name, files_extension)


    def create_source(self, output, class_name, files_extension):
        file = open("output/new1/Routes/"+class_name+"."+files_extension,'w')
        file.write(output)
        file.close()
        return

