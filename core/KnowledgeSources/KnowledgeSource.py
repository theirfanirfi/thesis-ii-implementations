from abc import ABC, abstractmethod
from jinja2 import Template
from core.ClassesBuilder import ClassesBuilder


class KnowledgeSource(ABC):
    def select_template(self, target_language, target_framework, template_type):
        file = open("targets/"+target_language+"/"+target_framework+"/"+template_type)
        template = Template(file.read())
        return template

    @abstractmethod
    def generate(self, language, framework, classesBuilder: ClassesBuilder, files_extension):
        raise NotImplementedError("Implement generate error")

