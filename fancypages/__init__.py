from __future__ import absolute_import

import os

__version__ = VERSION = "0.3.0"


def get_fancypages_paths(path, use_with_oscar=False):
    """ Get absolute paths for *path* relative to the project root """
    paths = []
    if use_with_oscar:
        from fancypages.contrib import oscar_fancypages
        base_dir = os.path.dirname(os.path.abspath(oscar_fancypages.__file__))
        paths.append(os.path.join(base_dir, path))
    return paths + [
        os.path.join(os.path.dirname(os.path.abspath(__file__)), path)]


def get_required_apps():
    return [
        'django_extensions',
        # used for image thumbnailing
        'sorl.thumbnail',
        # framework used for the internal API
        'rest_framework',
        # provides a convenience layer around model inheritance
        # that makes lookup of nested models easier. This is used
        # for the content block hierarchy.
        'model_utils',
        # migration handling
        'south',
    ]


def get_fancypages_apps(use_with_oscar=False):
    apps = ['fancypages.assets', 'fancypages']
    if use_with_oscar:
        apps += ['fancypages.contrib.oscar_fancypages']
    return apps
