import os

from core.telemetry import setup_telemetry


def post_fork(server, worker):
    if not os.getenv('DJANGO_SETTINGS_MODULE'):
        print('WARNING: DJANGO_SETTINGS_MODULE is not set')
        return
    setup_telemetry()
