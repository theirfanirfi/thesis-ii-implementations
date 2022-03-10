from core.utils.utils import generate_random_string

class Variable:
    def __init__(self):
        self.id = str
        self.type: str
        self.name: str
        self.default_value: str
        self.sterotypes: str
        self.visibility: str

    def perform_extraction(self, raw_data):
        self.id = generate_random_string(10)
        self.name = raw_data.attrib['Name']
        self.type = raw_data.attrib['Type']
        # self.visibility = raw_data.attrib['Visibility']
        return self
