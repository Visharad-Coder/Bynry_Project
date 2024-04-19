from django.contrib import admin
from django.urls import path
from utilities import views
from django.conf import settings
from django.conf.urls.static import static
from .views import register, profile, user_login,submit_service_request,view_service_requests,update_service_request_status,support_dashboard,view_service_request

urlpatterns = [
    path('', views.index, name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('submit-service-request/', views.submit_service_request, name='submit_service_request'),
    path('view-service-requests/', views.view_service_requests, name='view_service_requests'),
    path('support_dashboard/', views.support_dashboard, name='support_dashboard'),
    path('view-service-request/<int:request_id>/', views.view_service_request, name='view_service_request'),
    path('update-service-request-status/<int:request_id>/', views.update_service_request_status, name='update_service_request_status'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
