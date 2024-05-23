from django.contrib import admin
from .models import Test, Question

# Register your models here.

admin.site.register(Test)

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('content',)}