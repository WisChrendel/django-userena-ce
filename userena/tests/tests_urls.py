from django.test import TestCase
try:
    # django.VERSION < 2.0
    from django.core.urlresolvers import reverse, NoReverseMatch
except ImportError:
    from django.urls import reverse, NoReverseMatch

class UserenaUrlsTests(TestCase):
    """ Test url resolve """

    def test_resolve_email_with_plus_url(self):
        username = 'foo+bar@example.com'
        test_urls = [
            'userena_signup_complete',
            'userena_email_change',
            'userena_email_change_complete',
            'userena_email_confirm_complete',
            'userena_disabled',
            'userena_password_change',
            'userena_password_change_complete',
            'userena_profile_edit',
            'userena_profile_detail',
        ]
        for url_name in test_urls:
            try:
                reverse(url_name, kwargs={'username': username})
            except NoReverseMatch as ex:
                self.failed(ex)
