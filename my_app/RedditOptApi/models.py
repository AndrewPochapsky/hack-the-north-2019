from django.db import models

# Create your models here.
class ListField(models.TextField):
    """
    A custom Django field to represent lists as comma separated strings
    https://stackoverflow.com/questions/22340258/django-list-field-in-model
    """

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
        super().__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super().deconstruct()
        kwargs['token'] = self.token
        return name, path, args, kwargs

    def to_python(self, value):

        class SubList(list):
            def __init__(self, token, *args):
                self.token = token
                super().__init__(*args)

            def __str__(self):
                return self.token.join(self)

        if isinstance(value, list):
            return value
        if value is None:
            return SubList(self.token)
        return SubList(self.token, value.split(self.token))

    def from_db_value(self, value, expression, connection):
        return self.to_python(value)

    def get_prep_value(self, value):
        if not value:
            return
        assert(isinstance(value, Iterable))
        return self.token.join(value)

    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)

class InputBox(models.Model):
    return_number = models.PositiveSmallIntegerField()
    title = models.CharField(max_length=255)
    body = models.TextField(blank=False)

    def __str__(self):
        return self.title

class Output(models.Model):
    subreddits = ListField()
