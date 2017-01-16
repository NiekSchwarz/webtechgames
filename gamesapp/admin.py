from django.contrib import admin
from .models import Game
from .models import HighScore


admin.site.register(Game)
admin.site.register(HighScore)