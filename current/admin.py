from django.contrib import admin
from .models import Profile,Business,NeighbourHood,Post

# Register your models here.
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Business)
admin.site.register(NeighbourHood)
