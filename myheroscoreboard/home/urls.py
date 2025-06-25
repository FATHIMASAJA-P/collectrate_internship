

#from django.urls import path,include
#from . import views
#from django.contrib.auth.views import homeview
#urlpatterns = [
    
 #   path('',views.index, name='index'),
  #  path('accounts/', include('django.contrib.auth.urls')),  # This includes login, logout, password change, etc.
    # path('accounts/signup/', views.signup, name='signup'),  # Uncomment if you have a signup view
    # path('accounts/profile/', views.profile, name='profile'),  # Uncomment if you have a profile view
   #  path('accounts/logout/', views.homeview, name='logout'),  # Uncomment if you have a custom logout view
    # path('accounts/login/', views.login_view, name='login'),  # Uncomment if you have a custom login view
    # path('accounts/password_change/', views.password_change, name='password_change'),  # Uncomment if you have a custom password change view
#]


from django.urls import path
from . import views  # Import your app's views
from django.contrib.auth.views import LogoutView  # Correct import for logout

urlpatterns = [
    path('', views.index, name='home'),  # Your home page view
    
]