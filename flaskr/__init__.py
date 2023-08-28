from .app import App


def create_app(config_name='default'):
    application = App(config_name)
    return application.get_app()
