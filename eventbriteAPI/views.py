"""
    Views for the eventbriteAPI app

"""

import json
from django.http import HttpResponse
import requests
from requests.models import Response

from .constants import BASE_URL, PRIVATE_TOKEN


def organizations(request) -> HttpResponse:
    """
    View for the index page

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

    headers: dict[str, str] = {
        "Authorization": f"Bearer {PRIVATE_TOKEN}",
    }

    url: str = f"{BASE_URL}/users/me/organizations/"
    response: Response = requests.get(url=url, headers=headers, timeout=20)

    if response.status_code != 200:
        return HttpResponse(f"Error: {response.json()}")

    all_organizations: list = [
        {"id": organization.get("id"), "name": organization.get("name")}
        for organization in response.json().get("organizations")
    ]

    return HttpResponse(json.dumps(all_organizations))


def events(request, organization_id: int) -> HttpResponse:
    """
    Get all events for the organization

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

    organization_id: int = 1878868997373

    headers: dict[str, str] = {
        "Authorization": f"Bearer {PRIVATE_TOKEN}",
    }

    url: str = f"{BASE_URL}/organizations/{organization_id}/events/"
    response: Response = requests.get(url=url, headers=headers, timeout=20)

    if response.status_code != 200:
        return HttpResponse(f"Error: {response.json()}")

    all_events: list = [
        {
            "id": event.get("id"),
            "name": event.get("name").get("text"),
            "description": event.get("description").get("text"),
        }
        for event in response.json().get("events")
    ]

    return HttpResponse(json.dumps(all_events))


def event_detail(request, event_id: int) -> HttpResponse:
    """
    Get event details for the event

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

    event_id: int = 751518681607

    headers: dict[str, str] = {
        "Authorization": f"Bearer {PRIVATE_TOKEN}",
    }

    url: str = f"{BASE_URL}/events/{event_id}?expand=ticket_classes,venue"
    response: Response = requests.get(url=url, headers=headers, timeout=20)

    if response.status_code != 200:
        return HttpResponse(f"Error: {response.json()}")

    event_details: dict = {
        "id": response.json().get("id"),
        "name": response.json().get("name").get("text"),
        "description": response.json().get("description").get("text"),
        "eventbrite_url": response.json().get("url"),
        "start_date": response.json().get("start"),
        "end_date": response.json().get("end"),
        "cost": {
            "price": response.json()
            .get("ticket_classes")[0]
            .get("cost")
            .get("major_value"),
            "currency": response.json()
            .get("ticket_classes")[0]
            .get("cost")
            .get("currency"),
        },
        "venue": {
            "venue_id": response.json().get("venue").get("id"),
            "country": response.json()
            .get("venue")
            .get("address")
            .get("country"),
            "city": response.json().get("venue").get("address").get("city"),
            "region": response.json()
            .get("venue")
            .get("address")
            .get("region"),
            "postal_code": response.json()
            .get("venue")
            .get("address")
            .get("postal_code"),
            "address": response.json()
            .get("venue")
            .get("address")
            .get("address_2"),
            "full_address": response.json()
            .get("venue")
            .get("address")
            .get("localized_address_display"),
            "latitude": response.json()
            .get("venue")
            .get("address")
            .get("latitude"),
            "longitude": response.json()
            .get("venue")
            .get("address")
            .get("longitude"),
            "capacity": response.json().get("venue").get("capacity"),
        },
    }

    return HttpResponse(json.dumps(event_details))