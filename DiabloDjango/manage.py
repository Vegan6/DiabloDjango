#!/usr/bin/env python
"""
Command-line utility for administrative tasks.
"""

import os
import sys

root_path = os.path.abspath(os.path.split(__file__)[0])
sys.path.insert(0, os.path.join(root_path, 'DiabloDjango'))
sys.path.insert(0, root_path)

if __name__ == "__main__":
    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "DiabloDjango.settings"
    )

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
