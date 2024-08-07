# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Clubs(models.Model):
    id = models.IntegerField(primary_key=True, blank=True, null=False)
    team_id = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    short_code = models.CharField(max_length=5, blank=True, null=True)
    common_name = models.CharField(max_length=30, blank=True, null=True)
    logo = models.CharField(max_length=255, blank=True, null=True)
    country_id = models.IntegerField(blank=True, null=True)
    country_name = models.CharField(max_length=125, blank=True, null=True)
    country_code = models.CharField(max_length=5, blank=True, null=True)
    continent = models.CharField(max_length=30, blank=True, null=True)
    country_flag = models.CharField(max_length=255, blank=True, null=True)
    league_id = models.IntegerField(blank=True, null=True)
    # This field type is a guess.
    season = models.JSONField(blank=True, null=True)
    standing = models.JSONField(blank=True, null=True)
    # This field type is a guess.
    matches = models.JSONField(blank=True, null=True)
    biography = models.CharField(max_length=65651, blank=True, null=True)
    # This field type is a guess.
    trophies = models.JSONField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Clubs'


class AlembicVersion(models.Model):
    version_num = models.CharField(primary_key=True, max_length=32)

    class Meta:
        managed = False
        db_table = 'alembic_version'
