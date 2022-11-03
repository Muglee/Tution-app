from django.urls import path
from .views import search,contact, postview,postcreate,ContactView,PostCreateView,PostListView,PostDetailView,PostEditView,PostDeleteView
from .forms import ContactFormtwo
app_name= 'tution'

urlpatterns = [
    # path('contact/', contact,name="contact"),
    path('search/', search,name="search"),
    path('contact/', ContactView.as_view(),name="contact"),
    path('contact2/', ContactView.as_view(form_class=ContactFormtwo, template_name="Contact2.html"),name="contact2"),
    path('posts/', postview,name="posts"),
    path('postlist/', PostListView.as_view(),name="postlist"),
    path('postdetail/<int:pk>/', PostDetailView.as_view(),name="postdetail"),
    path('delete/<int:pk>/', PostDeleteView.as_view(),name="delete"),
    path('edit/<int:pk>/', PostEditView.as_view(),name="edit"),
    # path('create/', postcreate,name="create"),
    path('create/', PostCreateView.as_view(),name="create"),
]
