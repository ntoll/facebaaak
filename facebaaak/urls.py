"""
Facebaaak URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as users_views
from bleet import views as bleets_views
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


api_router = DefaultRouter()
api_router.register(r"users", users_views.UserViewSet, basename="user")
api_router.register(r"bleets", bleets_views.BleetViewSet, basename="bleet")


schema_view = get_schema_view(
   openapi.Info(
      title="Facebaaak API",
      default_version='v1',
      description="The simple Facebaaak API.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@facebaaak.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(api_router.urls)),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="users/login.html"),
        name="login",
    ),
    path(
        "logout/",
        auth_views.LogoutView.as_view(template_name="users/logout.html"),
        name="logout",
    ),
    path(
        "password-reset/",
        auth_views.PasswordResetView.as_view(template_name="users/password_reset.html"),
        name="password-reset",
    ),
    path(
        "password-reset/done",
        auth_views.PasswordResetDoneView.as_view(
            template_name="users/password_reset_done.html"
        ),
        name="password-reset-done",
    ),
    path(
        "password-reset/confirm/<uidb64>/<token>/",
        auth_views.PasswordResetConfirmView.as_view(
            template_name="users/password_reset_confirm.html"
        ),
        name="password-reset-done",
    ),
    path("register/", users_views.register, name="register-users"),
    path("profile/", users_views.profile, name="profile"),
    path("", include("bleet.urls")),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
