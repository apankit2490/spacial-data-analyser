from django.contrib.gis.db import models
from django.core.exceptions import ValidationError


class WorldCountry(models.Model):
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=50)
    geometry = models.GeometryField(null=False, blank=False)

    def clean(self):
        """
        Override clean method to check either name or code is specified
        """
        cleaned_data = super().clean()
        if not cleaned_data.get('name') and not cleaned_data.get('code'):
            raise ValidationError({'name': 'Even one of name or code should have a value.'})

    class Meta:
        db_table = 'worldcountry'
        verbose_name = 'WorldCountry'
        verbose_name_plural = 'WorldCountries'

    def __str__(self):
        return f'{self.name}'
