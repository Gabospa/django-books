""" Books URL's """

from django.urls import path


from . import views


app_name = 'books'

urlpatterns = [
    path('apidetail/<arg1>/', views.DetailApiView.as_view(), name='bookdetail'),
    path('list', views.BookListView.as_view(), name='booklist'),
    path('<slug:slug>', views.BookDetailView.as_view(), name='owndetail'),
    path('agregar/', views.add, name='addbook'),
]

