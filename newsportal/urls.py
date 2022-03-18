from django.urls import path
from .views import PostList, NewDetail  # импортируем наше представление

urlpatterns = [
    path('', PostList.as_view()),
    path('<int:pk>', NewDetail.as_view()),
    # pk — это первичный ключ новости, который будет выводиться у нас в шаблон
    # т. к. сам по себе это класс, то нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view
]