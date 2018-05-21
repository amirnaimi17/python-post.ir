from __future__ import absolute_import, unicode_literals

# This will make sure the app is always imported when
# Django starts so that shared_task will use this app.

__all__ = []


def register_api(_api):

    from . import views

    _api.register(r'static_types', views.StaticTypesViewSet, base_name='StaticTypes')