from django.urls import path
from . import views


# SET THE NAMESPACE!
# app_name = 'basic_app'

# Be careful setting the name to just /login use userlogin instead!
urlpatterns=[
    path('',views.user_login,name='user_login'),
    path('register/',views.register,name='register'),
    path('index/', views.index,name='index'),
    path('logout/', views.user_logout, name='logout'),
    # path('profile/',views.ProfileUpdateView.as_view(),name='user_profile')
    # path('special/', views.special,name='special'),
    # path('admin/clearcache/', include('clearcache.urls')),
    # path('basic_app/', include('basic_app.urls')),/   
]
