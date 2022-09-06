from django.urls import path
from .views import StudentGenericView
urlpatterns = [
    path('student/<int:id>/',StudentGenericView.as_view())
]
