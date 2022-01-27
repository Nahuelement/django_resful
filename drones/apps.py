from django.apps import AppConfig
from django.contrib.admin.apps import AdminConfig


class DronesConfig(AppConfig):
    name = 'drones'

class DroneAdminConfig(AdminConfig):
    default_site = 'admin.DronesAdminSite'