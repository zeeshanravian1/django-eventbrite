from django.urls import path, URLPattern

from . import views

urlpatterns: list[URLPattern] = [
    path("organizations", views.organizations, name="organizations"),
    path("events/<int:organization_id>", views.events, name="events"),
    path(
        "event-detail/<int:event_id>",
        views.event_detail,
        name="event_details",
    ),
]
