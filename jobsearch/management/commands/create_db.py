# coding: utf-8

from django.core.management.base import BaseCommand

from jobsearch.models import Status, StyleOfContract, TypeOfContract
from . import constant


class Command(BaseCommand):
    """
    This class fill in the database
    """
    def insert_data(self):
        for element in constant.STATUS:
            Status.objects.get_or_create(
                advanced=element
            )
        for element in constant.TYPE:
            TypeOfContract.objects.get_or_create(
                type=element
            )
        for element in constant.STYLE:
            StyleOfContract.objects.get_or_create(
                style=element
            )

    def handle(self, *args, **options):
        self.insert_data()
