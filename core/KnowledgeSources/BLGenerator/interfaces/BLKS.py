from abc import ABC, abstractmethod
import os
from core.ClassesBuilder import ClassesBuilder
class BLKS(ABC):

    def create_source(self, template, class_name): pass

    @abstractmethod
    def generate(self, language, framework, classesBuilder: ClassesBuilder, files_extension):
        raise NotImplementedError("Implement generate error")


