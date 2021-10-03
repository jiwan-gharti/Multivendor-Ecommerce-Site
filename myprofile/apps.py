from django.apps import AppConfig


class MyprofileConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'myprofile'

class MyProfileConfig(AppConfig):
    name = 'myprofile'
    verbose_name = "Customer Profile"
