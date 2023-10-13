from ..hamlet import GeoEntity

class Library(GeoEntity):
    def __init__(self, name, location, database=None):
        super().__init__(name, location)
        self.database = database if database is not None else {}

from ...db import db

class Library(GeoEntity):
    def __init__(self, name, location, database=None):
        super().__init__(name, location)
        self.database = database if database is not None else {}

    def create_data_sql(self, data):
        db.create_data_sql(data)

    def read_data_sql(self, data_id):
        db.read_data_sql(data_id)

    def update_data_sql(self, data_id, new_data):
        db.update_data_sql(data_id, new_data)

    def delete_data_sql(self, data_id):
        db.delete_data_sql(data_id)
