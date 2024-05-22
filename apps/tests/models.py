from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Test(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='authors_tests', null=False)
    topic = models.CharField(max_length=20)
    description = models.TextField(max_length=255, blank=True, null=True)
    
    created_at = models.DateTimeField(default=timezone.now, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.topic
    
    class Meta:
        ordering=['-created_at']
    
    
class Registration(models.Model):
    test = models.ForeignKey(Test, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    
    def __str__(self):
        return f'Реєстрація на тест {self.test.topic} {self.user.username}'
    
    class Meta:
        verbose_name='Реєстрація',
        verbose_name_plural='Реєстрації'