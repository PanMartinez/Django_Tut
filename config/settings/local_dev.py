#Local settings for core project.

LOCAL_SETTINGS = True
from config.settings.base import *

DEBUG = True
#TEMPLATE_DEBUG = True
WEASYPRINT_BASE_STATIC_URL = "http://localhost:8000"  # No trailing slash


########## ROBOTS CONFIG
ROBOTS_ENABLED = False
########## END ROBOTS CONFIG


# ########## DJANGO DEBUG TOOLBAR CONFIGURATION
# INSTALLED_APPS = INSTALLED_APPS + ('debug_toolbar',)
# MIDDLEWARE_CLASSES = MIDDLEWARE_CLASSES + ('debug_toolbar.middleware.DebugToolbarMiddleware', )
# INTERNAL_IPS = ('127.0.0.1',)

# Add in the template timing toolbar
# INSTALLED_APPS = INSTALLED_APPS + ('template_timings_panel',)
# DEBUG_TOOLBAR_PANELS = [
#     'debug_toolbar.panels.versions.VersionsPanel',
#     'debug_toolbar.panels.timer.TimerPanel',
#     'debug_toolbar.panels.settings.SettingsPanel',
#     'debug_toolbar.panels.headers.HeadersPanel',
#     'debug_toolbar.panels.request.RequestPanel',
#     'debug_toolbar.panels.sql.SQLPanel',
#     'debug_toolbar.panels.staticfiles.StaticFilesPanel',
#     'debug_toolbar.panels.templates.TemplatesPanel',
#     'debug_toolbar.panels.cache.CachePanel',
#     'debug_toolbar.panels.signals.SignalsPanel',
#     'debug_toolbar.panels.logging.LoggingPanel',
#     'debug_toolbar.panels.profiling.ProfilingPanel',
#     'template_timings_panel.panels.TemplateTimings.TemplateTimings',
#     'debug_toolbar.panels.redirects.RedirectsPanel',
# ]
########## END DJANGO DEBUG TOOLBAR CONFIGURATION


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_tutbase',
        'USER': 'Sanchez',
        'PASSWORD': 'get.get',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# For storage locally. Dont want to have to run collect static while in dev.
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.StaticFilesStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}
