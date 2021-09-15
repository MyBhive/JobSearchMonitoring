# coding: utf-8
from django.db import models
from useraccount.models import CustomUser


class Categories(models.Model):
    """
    Class to create a table for the categories of job research
    """
    name_category = models.CharField(max_length=150, unique=True)
    user = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name_category


class JobOffer(models.Model):
    """
    Class to create a table for jobs sheets
    """
    title = models.CharField(max_length=100)
    company_name = models.CharField(max_length=150, null=False)
    url = models.URLField(max_length=500, null=False, blank=False)
    date = models.DateField(null=False, blank=False)
    salary = models.DecimalField(max_digits=19, decimal_places=3, null=False, blank=False)
    comments = models.CharField(max_length=800, null=True, blank=True)
    category_id = models.ForeignKey(
        Categories, on_delete=models.CASCADE
    )
    user_id = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title


class InfoUpload(models.Model):
    """
    Class to create a table to upload
    cv and motivation letter depending of the job offer saved
    """
    motiv_letter = models.BinaryField(null=True, blank=True)
    cv = models.BinaryField(null=True, blank=True)

    def __str__(self):
        return self.cv


class Status(models.Model):
    """
    Class to create a table to save the status of a research
    """
    advanced = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.advanced


class StatusConnect(models.Model):
    status_id = models.ForeignKey(
        Status, on_delete=models.CASCADE
    )
    user_ref = models.ForeignKey(
        CustomUser, on_delete=models.CASCADE
    )
    job_ref = models.ForeignKey(
        JobOffer, on_delete=models.CASCADE
    )


class InterviewDate(models.Model):
    """
    Class to create a table to save a job interview appointment
    """
    interview_date = models.DateTimeField(null=False)
    status_id = models.ForeignKey(
        Status, on_delete=models.CASCADE
    )

    def __str__(self):
        return self.interview_date


class StyleOfContract(models.Model):
    """
    Class to create a table to define the style of contract is saved
    """
    style = models.CharField(max_length=20, unique=True, null=False)

    def __str__(self):
        return self.style


class JobStyleConnect(models.Model):
    """
    Class to create a table to join the job offer
    to the style of contract
    """
    style_id = models.ForeignKey(
        StyleOfContract, on_delete=models.CASCADE
    )
    job = models.ForeignKey(
        JobOffer, on_delete=models.CASCADE
    )


class TypeOfContract(models.Model):
    """
    Class to create a table to define the type of contract is saved
    """
    type = models.CharField(max_length=30, unique=True, null=False)

    def __str__(self):
        return self.type


class JobTypeConnect(models.Model):
    """
    Class to create a table to join the job offer
    to the style of contract
    """
    type_id = models.ForeignKey(
        TypeOfContract, on_delete=models.CASCADE
    )
    job_id = models.ForeignKey(
        JobOffer, on_delete=models.CASCADE
    )
