#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import configparser

# Get the path of the .env configuration file in the same directory.
env_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), '.env')

def set_env():
    """Set up environment variables."""
    config = configparser.ConfigParser()
    config.read(env_file_path)  
    settings_module = config.get('DEFAULT', 'DJANGO_SETTINGS_MODULE')
    db_name = config.get('DEFAULT', 'SOM_DB_NAME')
    db_user = config.get('DEFAULT', 'SOM_DB_USER')
    db_password = config.get('DEFAULT', 'SOM_DB_PASSWORD')
    db_host = config.get('DEFAULT', 'SOM_DB_HOST')
    db_port = config.get('DEFAULT', 'SOM_DB_PORT')
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_module)
    os.environ.setdefault('SOM_DB_NAME', db_name)
    os.environ.setdefault('SOM_DB_USER', db_user)
    os.environ.setdefault('SOM_DB_PASSWORD', db_password)
    os.environ.setdefault('SOM_DB_HOST', db_host)
    os.environ.setdefault('SOM_DB_PORT', db_port)

def main():
    """Run administrative tasks."""
    set_env()
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
