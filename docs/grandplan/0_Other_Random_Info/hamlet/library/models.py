from django.db import models
from TheDigitalHamlet.base_models import BaseBuilding

class Library(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    database = models.JSONField()

    def create_data_sql(self, data):
        # db.create_data_sql(data)
        pass

    def read_data_sql(self, data_id):
        # db.read_data_sql(data_id)
        pass

    def update_data_sql(self, data_id, new_data):
        # db.update_data_sql(data_id, new_data)
        pass

    def delete_data_sql(self, data_id):
        # db.delete_data_sql(data_id)
        pass
