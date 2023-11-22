class GeoEntity:
    def __init__(self, name, location):
        self.name = name
        self.location = location

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

class Hamlet(GeoEntity):
    def __init__(self, name, location, entities=None):
        super().__init__(name, location)
        self.entities = entities if entities is not None else []

    def add_entity(self, entity):
        self.entities.append(entity)

    def remove_entity(self, entity):
        self.entities.remove(entity)

    def get_entities(self):
        return self.entities
