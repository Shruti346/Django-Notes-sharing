
from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/',about,name='about'),
    path('',index,name='index'),
    path('login/',userlogin,name='login'),
    path('signup/',signup1,name='signup'),
    path('logout/',Logout,name='logout'),
    path('profile/',profile,name='profile'),
    path('edit_profile/',edit_profile,name='edit_profile'),
    path('changepassword/',changepassword,name='changepassword'),
    path('upload_notes/',upload_notes,name='upload_notes'),
    path('view_mynotes/',view_mynotes,name='view_mynotes'),
    
    path('delete_mynotes/<int:pid>', delete_mynotes,name='delete_mynotes'),
    path('view_users/',view_users,name='view_users'),
    path('delete_users/<int:pid>', delete_users,name='delete_users'),
    path('pending_notes/',pending_notes,name='pending_notes'),
    path('accepted_notes/',accepted_notes,name='accepted_notes'),
    path('rejected_notes/',rejected_notes,name='rejected_notes'),
    path('all_notes/',all_notes,name='all_notes'),
    path('assign_status/<int:pid>', assign_status,name='assign_status'),
    path('delete_notes/<int:pid>', delete_notes,name='delete_notes'),
    path('viewallnotes/',viewallnotes,name='viewallnotes'),


]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
