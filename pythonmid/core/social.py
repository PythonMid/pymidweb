__author__ = 'alex'
from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS

TEMPLATE_CONTEXT_PROCESSORS += (
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
)

AUTHENTICATION_BACKENDS = (
    'social.backends.twitter.TwitterOAuth',  # Twitter
    'django.contrib.auth.backends.ModelBackend',
)


# SOCIAL AUTH SETTINGS
SOCIAL_AUTH_TWITTER_KEY = 'KI5eZhZDJfKSHMSGGgBLmcbdp'
SOCIAL_AUTH_TWITTER_SECRET = 'tLb6LWQ4SkJW9Pmg9STPM1X6sECW7g14vkzJjc0fGZuBalPhWW'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_LOGIN_URL = '/'
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',
    # 'social.pipeline.user.user_details', Comentamos para no actualizar los datos cada que realizamos un login
    'pythonmid.apps.security.pipeline.update_user_social_data',
)
