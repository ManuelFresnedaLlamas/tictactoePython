from django.contrib import admin
from django.urls import path
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('new/', views.new_game, name='new_game'),
    path('move/<int:game_id>/', views.make_move, name='make_move'),
]
