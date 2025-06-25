<<<<<<< HEAD
"""
WSGI config for currency_converter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_converter.settings')

application = get_wsgi_application()

=======
"""
WSGI config for currency_converter project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'currency_converter.settings')

application = get_wsgi_application()

>>>>>>> 7b25173f83cc42e71a57b3263d2066a519c71c28
app = application