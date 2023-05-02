from django.urls import path
from . import views

urlpatterns = [
    # path('', views.DocAttachedList.as_view()),
    path('', views.categories),
    path('<str:slug>/', views.per_category),
]