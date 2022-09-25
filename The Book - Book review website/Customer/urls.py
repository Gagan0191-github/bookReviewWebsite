from django.urls import path

from .import views

urlpatterns=[
      path('',views.home,name='home'),
      path('login',views.login,name='login'),
      path('register',views.register,name='register'),
      path('reviewers',views.reviewers,name='reviewers'),
      path('blogs',views.blogs,name='blogs'),
      path('authors',views.authors,name='authors'),
      path('contactus',views.contactus,name='contactus'),
]

