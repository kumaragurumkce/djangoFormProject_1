from django.db import models

# Create your models here.
class TextContent(models.Model):
    title=models.CharField(max_length=20) 
    def __str__(self):
        return self.title


class Home_card(models.Model):
    title=models.CharField(max_length=20) 
    image=models.ImageField(upload_to='images/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.home_card_title
    # def __str__(self):
    #     return self.title
        