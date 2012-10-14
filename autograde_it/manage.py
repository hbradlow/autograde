#!/usr/bin/env python
import os
import sys
import os.path

DIRNAME = os.path.dirname(__file__)

from autograde_it.apps import *
from django.conf import settings

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "autograde_it.settings")

    sys.path.insert(0, os.path.join(settings.PROJECT_ROOT, "apps"))

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
