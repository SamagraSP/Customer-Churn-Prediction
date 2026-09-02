"""
WSGI config for DeepChurn project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""
"""
import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application


# Add the project directory containing settings.py to sys.path
path_to_add = Path(__file__).resolve().parent
if str(path_to_add) not in sys.path:
    sys.path.append(str(path_to_add))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

application = get_wsgi_application()

# Alias for Vercel WSGI entry point
app = application
"""

import os
import sys
from pathlib import Path
from django.core.wsgi import get_wsgi_application

# Add the repository root directory (/var/task) to sys.path
# This resolves the outer DeepChurn folder so 'DeepChurn.settings' works cleanly
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.append(str(BASE_DIR))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DeepChurn.settings')

application = get_wsgi_application()

# Alias required for Vercel Python runtime
app = application
