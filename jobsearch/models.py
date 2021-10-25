# coding: utf-8
from django.db import models
from useraccount.models import CustomUser
from django.urls import reverse


class Categories(models.Model):
    """
    Class to create a table
    for the categories of job research
    """
    name_category = models.CharField(
        max_length=150,
        unique=True
    )
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_category


class Status(models.Model):
    """
    Class to create a table
    to save the status of a research
    """
    advanced = models.CharField(
        max_length=20,
        unique=True
    )

    def __str__(self):
        return self.advanced


class StyleOfContract(models.Model):
    """
    Class to create a table
    to define the style of contract is saved
    """
    style = models.CharField(
        max_length=20,
        unique=True,
        null=False
    )

    def __str__(self):
        return self.style


class TypeOfContract(models.Model):
    """
    Class to create a table
    to define the type of contract is saved
    """
    type = models.CharField(
        max_length=30,
        unique=True,
        null=False
    )

    def __str__(self):
        return self.type


class JobOffer(models.Model):
    """
    Class to create a table for jobs sheets
    """
    title = models.CharField(
        max_length=100, verbose_name='Job'
    )
    company_name = models.CharField(
        max_length=150,
        null=False
    )
    url = models.URLField(
        max_length=500,
        null=False,
        blank=False
    )
    date = models.DateField(
        auto_now_add=True
    )
    salary = models.DecimalField(
        max_digits=19,
        decimal_places=3,
        null=False,
        blank=False
    )
    comments = models.TextField(
        max_length=800,
        null=True,
        blank=True
    )
    motiv_letter = models.FileField(
        null=True,
        blank=True,
        upload_to='files/', verbose_name='Letter of Motivation'
    )
    cv = models.FileField(
        null=True,
        blank=True,
        upload_to='files/', verbose_name='CV'
    )
    category_id = models.ForeignKey(
        Categories,
        on_delete=models.CASCADE, verbose_name='Category'
    )
    user_id = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    status_id = models.ForeignKey(
        Status,
        on_delete=models.CASCADE, verbose_name='Job Status'
    )
    style_id = models.ForeignKey(
        StyleOfContract,
        on_delete=models.CASCADE, verbose_name='Job style'
    )
    type_id = models.ForeignKey(
        TypeOfContract,
        on_delete=models.CASCADE, verbose_name='Job type'
    )

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse(
            'job_detail',
            kwargs={"pk": self.pk}
        )


def creating_db_setup():
    Status.objects.create(advanced='CV sent')
    Status.objects.create(advanced='To apply')
    Status.objects.create(advanced='Positive answer')
    Status.objects.create(advanced='Negative answer')
    Status.objects.create(advanced='Job interview')
    TypeOfContract.objects.create(type='Permanent')
    TypeOfContract.objects.create(type='Fixed-term')
    TypeOfContract.objects.create(type='Permanent')
    TypeOfContract.objects.create(type='Working student')
    TypeOfContract.objects.create(type='Internship')
    TypeOfContract.objects.create(type='Freelance')
    TypeOfContract.objects.create(type='Casual')
    TypeOfContract.objects.create(type='Others')
    StyleOfContract.objects.create(style='Full time')
    StyleOfContract.objects.create(style='Part time')
    StyleOfContract.objects.create(style='Casual')
    StyleOfContract.objects.create(style='Others')



