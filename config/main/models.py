from django.db import models

# Modelo Abstracto
class BaseModel(models.Model):
    state = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# Modelo de Artículo
class Article(BaseModel):
    NEW = 'N'
    VERIFIED = 'V'
    PUBLISHED = 'P'

    STATUS_CHOICES = [
        (NEW, 'New'),
        (VERIFIED, 'Verified'),
        (PUBLISHED, 'Published'),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=NEW)

    def __str__(self):
        return self.title
