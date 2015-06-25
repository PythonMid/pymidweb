from urllib2 import urlopen
from django.core.files.base import ContentFile
from social.backends.twitter import TwitterOAuth
from pythonmid.apps.community.models import UserProfile
__author__ = 'alex'

def update_user_social_data(strategy, *args, **kwargs):
    """Set the name and avatar for a user only if is new.
    """
    print 'update_user_social_data ::', strategy
    if not kwargs['is_new']:
        return
    else:
        backend = kwargs['backend']
        user = kwargs['user']
        print(kwargs)
        print(kwargs['user'])
        if isinstance(backend, TwitterOAuth):
            if kwargs['response'].get('profile_image_url'):
                image_name = 'tw_avatar_%s.jpg' % user.username
                image_url = kwargs['response'].get('profile_image_url')
                user.first_name = kwargs['details'].get('first_name')
                user.last_name = kwargs['details'].get('last_name')
                user.save()
                image_stream = urlopen(image_url)
                user_profile = UserProfile()
                user_profile.user = user
                user_profile.image.save(image_name, ContentFile(image_stream.read()))
                user_profile.save()