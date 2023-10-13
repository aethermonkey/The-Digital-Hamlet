from ..hamlet import GeoEntity

class Library(GeoEntity):
    def __init__(self, name, location, database=None):
        super().__init__(name, location)
        self.database = database if database is not None else {}

    def create_data(self, data):
        # code to create data in the database

    def read_data(self, data_id):
        # code to read data from the database

    def update_data(self, data_id, new_data):
        # code to update data in the database

    def delete_data(self, data_id):
        # code to delete data from the database
