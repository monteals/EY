from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.urls import path

from emails import views as emails_views
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('home/', emails_views.home, name='home'),
    path('home/filter', emails_views.filter_user, name='filter_user'),
    path('home/add', emails_views.add_user, name='add_user'),
    path('home/modify', emails_views.modify_user, name='modify_user'),
    path('home/modify/save', emails_views.modify_user_save, name='modify_user_save'),
    path('home/remove', emails_views.remove_user, name='remove_user'),
    
    path('home/emails', emails_views.emails_user, name='emails_user'),
    path('home/emails/add', emails_views.emails_add, name='emails_add'),
    path('home/emails/modify', emails_views.emails_modify, name='emails_modify'),
    path('home/emails/modify/save', emails_views.emails_modify_save, name='emails_modify_save'),
    path('home/emails/remove', emails_views.emails_remove, name='emails_remove'),
    
    path('users/login/', users_views.login_view, name='login'),
    path('users/logout/', users_views.logout_view, name='logout'),
    path('users/signup/', users_views.signup_view, name='signup'),

    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
