from django.urls import path
from django.views.generic import RedirectView
from . import views
urlpatterns=[
    path('',views.employees_view,name='all-employees'),
    path('employee-detail/<int:pk>/',views.employee_detail,name='employee-detail'),
    path('employee-detail/',RedirectView.as_view(url='/all-employees/')),
    path('confirm-delete/<int:pk>',views.delete_confirmation,name='confirm-delete'),
    path('delete-employee/<int:pk>',views.delete_employee,name='delete-employee'),
    path('create-employee/',views.create_employee,name='create-employee'),
    path('update-employee/<int:pk>/',views.update_employee,name='update-employee'),
    path('search-employees/',views.search_view,name='search-employees')
]
