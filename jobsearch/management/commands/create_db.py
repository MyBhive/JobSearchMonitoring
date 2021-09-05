# coding: utf-8
from django.core.management.base import BaseCommand

from jobsearch.models import Status, StyleOfContract, TypeOfContract
import jobsearch.management.commands.constant as cons


class Command(BaseCommand):
    """
    This class handle status, type and style
    of job research that are saved in the app
    """
    def insert_data(self):
        """
        Method to insert the status name in the status table
        """
    for status in cons.STATUS:
        status_name = Status.objects.get_or_create(
            advanced=status
        )

    for type in cons.TYPE_OF_CONTRACT:
        type_name = TypeOfContract.objects.get_or_create(
            type=type
        )

    for style in cons.STYLE_OF_CONTRACT:
        style_name = StyleOfContract.objects.get_or_create(
            style=style
        )

    def handle(self, *args, **options):
        self.insert_data()
