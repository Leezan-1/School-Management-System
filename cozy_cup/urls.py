from django.shortcuts import render
from django.conf import settings
from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static


from . import views, Hod_views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('base/', views.Base, name='base'),
  path('login/', views.Login, name='login'),
  path('doLogin/', views.doLogin, name='doLogin'),
  path('logout/', views.Logout, name='logout'),
  # profile update
  path('profile/', views.profile, name='profile'),
  path('profile/update/', views.profile_update, name='profile_update'),
  # this is hod pannel
  path('hod/home/', Hod_views.Home, name='Hod_home'),

  path('hod/add/student', Hod_views.Add_student, name='Add_student'),
  path('hod/view_student/', Hod_views.View_student, name='View_student'),
  path('hod/edit_student/<str:id>', Hod_views.Edit_student, name='Edit_student'),
  path('hod/update_student/', Hod_views.Update_student, name='Update_student'),
  path('hod/delete_student/<str:admin>/',
        Hod_views.Delete_student, name='Delete_student'),
  path('hod/add_session/', Hod_views.Add_session, name='Add_session'),
  path('hod/add_course/', Hod_views.Add_course, name='Add_course'),
  path('hod/view_course/', Hod_views.View_course, name='View_course'),
  path('hod/edit_course/<str:id>', Hod_views.Edit_course, name='Edit_course'),
  path('hod/update_course/', Hod_views.Update_course, name='Update_course'),
  path('hod/add_staff/', Hod_views.Add_staff, name='Add_staff'),
  path('hod/view_staff/', Hod_views.View_staff, name='View_staff'),
  path('hod/edit_staff/<str:id>', Hod_views.Edit_staff, name='Edit_staff'),
  path('hod/update_staff/', Hod_views.Update_staff, name='Update_staff'),
  path('hod/delete_staff/<str:admin>/',
        Hod_views.Delete_staff, name='Delete_staff'),
  path('hod/add/subject', Hod_views.Add_subject, name='Add_subject'),
  path('hod/view/subject', Hod_views.View_subject, name='View_subject'),
  path('hod/edit_subject/<str:id>', Hod_views.Edit_subject, name='Edit_subject'),
  path('hod/update_subject/', Hod_views.Update_subject, name='Update_srubject'),
  path('hod/delete/subject/<str:id>',
        Hod_views.Delete_subject, name='Delete_subject'),
  path('hod/add/session', Hod_views.Add_session, name='Add_session'),
  path('hod/view/session', Hod_views.View_session, name='View_session'),
  path('hod/edit_session/<str:id>', Hod_views.Edit_session, name='Edit_session'),
  path('hod/staff/send_notification', Hod_views.Staff_send_notification,
        name='Staff_send_notification'),
  path('hod/staff/apply_leave', Hod_views.Staff_apply_leave,
        name='Staff_apply_leave')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
