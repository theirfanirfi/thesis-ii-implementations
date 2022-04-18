from core.ClassesBuilder import ClassesBuilder
from core.KnowledgeSources.KnowledgeSource import KnowledgeSource
from core.KnowledgeSources.BLGenerator.interfaces.BLKS import BLKS
import os

class BLSource(KnowledgeSource, BLKS):

    def generate(self, language, framework, classesBuilder: ClassesBuilder, files_extension):
        os.mkdir("output/new1")
        os.mkdir("output/new1/BusinessLogic")
        template = self.select_template(language, framework, "bl")
        for cls in classesBuilder:
            output = template.render(cls=cls)
            self.create_source(output, cls.class_.class_name, files_extension)


    def create_source(self, output, class_name, files_extension):
        file = open("output/new1/BusinessLogic/"+class_name+"BL."+files_extension,'w')
        file.write(output)
        file.close()
        return

