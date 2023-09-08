from django.urls import path
from .views import Signup, Login, UpdateAccount, DeleteAccount

urlpatterns = [
    path('signup/', Signup),
    path('login/', Login),
    path('update/<str:email>', UpdateAccount),
    path('delete/<str:email>', DeleteAccount),
]