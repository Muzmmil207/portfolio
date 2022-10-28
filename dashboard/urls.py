from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('manage-projects/', views.manage_projects, name="man_pro"),

    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    # CRUD
    path('add-project/', views.add_project, name="add"),
    path('update-project/<slug:slug>', views.update_project, name="update"),
    path('delete-project/<str:pk>', views.delete_project, name="dl"),
]
