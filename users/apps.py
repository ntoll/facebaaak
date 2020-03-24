from django.apps import AppConfig


class UsersConfig(AppConfig):
    """
    Configures the users app on application start.
    """
    name = "users"

    def ready(self):
        import users.signals
