from django.contrib import admin

# Register your models here.
# aqui você pode criar o que você quer controlar

from .models import Question

admin.site.register(Question) # você vai colocar no site