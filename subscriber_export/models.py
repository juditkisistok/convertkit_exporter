from django.db import models
import uuid

class Tag(models.Model):
    name = models.CharField(max_length=200)
    tagid = models.IntegerField(unique=True)
    retrieved = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name

class API(models.Model):
    email = models.CharField(max_length=200, primary_key=True, unique=True)
    ck_api = models.CharField(max_length=200)
    ck_secret = models.CharField(max_length=200)

    def __str__(self):
        return self.email