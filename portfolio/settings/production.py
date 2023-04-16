import dj_database_url

from .base import *

if not DEBUG:
    MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

    DATABASES = {
        "default": dj_database_url.config(
            # Feel free to alter this value to suit your needs.
            default="postgresql://postgres:postgres@localhost:5432/config",
            conn_max_age=600,
        )
    }

    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

    # Turn on WhiteNoise storage backend that takes care of compressing static files
    # and creating unique names for each version so they can safely be cached forever.
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

    RENDER_EXTERNAL_HOSTNAME = os.environ.get("RENDER_EXTERNAL_HOSTNAME")
    if RENDER_EXTERNAL_HOSTNAME:
        ALLOWED_HOSTS.append(RENDER_EXTERNAL_HOSTNAME)
