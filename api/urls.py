from django.urls import path
from api.views import ClassifyNumberView

urlpatterns = [
    path('classify-number', ClassifyNumberView.as_view(), name="classify-number")
]