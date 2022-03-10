class Relation:

    def __init__(self):
        self.id: str
        self.relation_type: str
        self.from_class: str
        self.to_class: str

    def perform_extraction(self, raw_data, relation_type):
        self.relation_type = relation_type
        if "Association" in relation_type:
            self.perform_association(raw_data)
        elif "Generalization" in relation_type:
            self.perform_generalization(raw_data)
        return self


    def perform_association(self, raw_data):
        self.from_class = raw_data['EndRelationshipFromMetaModelElement']
        self.to_class = raw_data['EndRelationshipToMetaModelElement']
        self.id = raw_data['Id']
        return self

    def perform_generalization(self, raw_data):
        self.from_class = raw_data['From']
        self.to_class = raw_data['To']
        self.id = raw_data['Id']
        return self

