from django.core.management.base import BaseCommand
import json
from django.db import models
from traits.models import Trait

class PossibleTrait(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=255)

class Command(BaseCommand):
    help = 'Populate traits data from JSON file'

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **options):
        file_path = options['file_path']
        with open(file_path, 'r') as f:
            traits_data = json.load(f)

        for trait_data in traits_data:
            Trait.objects.create(
                agent_id=trait_data['agent_id'],
                name=trait_data['name'],
                value=trait_data['value']
            )