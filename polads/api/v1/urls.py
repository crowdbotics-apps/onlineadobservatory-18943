from django.urls import path

from . import views


urlpatterns = [
    path(
        'total_spend/by_page/of_region/<slug:region_name>',
        views.ProxyPoladsView.as_view()
    )
]
