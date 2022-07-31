"""NITK_Site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from NITK.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
path("director", Director, name="Director"),
    path('', HomePage, name='home'),
    path('hods',Hod, name="hod"),
    path('deleteData/<str:rollNo>/', DeleteData, name="deleteData"),
    path('updateData/<str:rollNo>/', updateData, name="updateData"),
    path('Organisational_Chart',OrgChart, name="org"),
    path('facultyLogin/', FacultyLogin, name='FacultyLogin'),
    path('<str:Fid>/#', FacultyPage, name='FacultyPage'),
    path('<str:rollNo>/home/', LogoutS, name='LogoutS'),
    path('studentRegister/', StudentRegister, name='studentRegister'),
    path('studentLogin/', StudentLogin, name='StudentLogin'),
    path('<str:rollNo>/', StudentPage, name = 'StudentPage'),
    path('<str:rollNo>/RegisterSubjects/',RegisterSubjects, name = 'RegisterSubjects'),
    path('AcademicOffice', AcademicOffice, name = 'AcademicOffice'),
    path('pg_program', pgProgram, name="pgProgram"),
    path('ug_program', ugProgram, name="ugProgram"),
    path('Academic_Calender', AcadCal, name='AcadCal'),
    path('Deparment', Depart, name='Depart'),
    path('Fee', Fee, name='Fee'),
    path('Feedback', Feed, name='Feed'),
    path('Nonteach', NonTeach, name='NonTeach'),
    path('Teach', Teach, name='Teach'),
    path('Syllabus', UgPgSyllabus, name='UgPgSyllabus'),
    path('Time_Table', UgPgTt, name='UgPgTt'),

]
