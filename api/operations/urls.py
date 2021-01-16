from django.urls import path

from .views import OperationsView, ListOperations, ListLatestOperations

urlpatterns = [
    path('operations/', OperationsView.as_view()),
    path('operations/<int:id>/remove/', OperationsView.as_view()),
    path('operations/<int:id>/', OperationsView.as_view()),
    path('operations/all/', ListOperations.as_view()),
    path('operations/latest/', ListLatestOperations.as_view())
]

#path('operations/<int:id>/change/', OperationsView.as_view()),