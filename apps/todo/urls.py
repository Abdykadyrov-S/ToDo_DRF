from django.urls import path
from rest_framework.routers import DefaultRouter
from .views import TodoAPI, TodoALLDEL

router = DefaultRouter()
router.register("todo", TodoAPI, basename="todo")

urlpatterns = [
    path('api/todo/del/', TodoALLDEL.as_view(), name="all_destroy")
]
urlpatterns += router.urls 