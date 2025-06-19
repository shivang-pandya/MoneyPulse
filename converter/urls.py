from django.urls import path
from .views import convert_index,live_updates,update_profile,news_view

urlpatterns = [
    path('', convert_index, name='convert_index'),
    path('live/', live_updates, name='live_updates'),
    path('profile/', update_profile, name='update_profile'),
    path('news/', news_view, name='news'),

]
