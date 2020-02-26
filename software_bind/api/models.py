from django.db import models

# Create your models here.
class BaseModel(models.Model):
    user = models.CharField(max_length = 200)
    email = models.EmailField()
    api_key = models.CharField(max_length = 200)
    created = models.DateTimeField(auto_now_add=True, blank=False)

class InventoryModel(BaseModel):
    limit = models.IntegerField(default = 100)
    usage = models.IntegerField(default = 0)
    user_type = models.BooleanField(default = False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return  self.user
