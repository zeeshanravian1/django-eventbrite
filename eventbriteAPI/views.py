"""
    Views for the eventbriteAPI app

"""

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import requests
from requests.models import Response
from timezonefinder import TimezoneFinder

from .constants import BASE_URL, PRIVATE_TOKEN
from .forms import EventForm


def organizations(request, all_events=None) -> HttpResponse:
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
        {"id": int(organization.get("id")), "name": organization.get("name")}
        for organization in response.json().get("organizations")
    ]

    context: dict[str, list] = {"organizations": all_organizations}

    if all_events:
        context["selected_organization_id"] = all_events[0]["organization_id"]
        context["events"] = all_events

    return render(request, "organizations.html", context)


def events(request, organization_id: int) -> HttpResponse:
    """
    Get all events for the organization

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

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
            "organization_id": organization_id,
        }
        for event in response.json().get("events")
    ]

    return organizations(request=request, all_events=all_events)


def event_detail(request, event_id: int) -> HttpResponse:
    """
    Get event details for the event

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

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
    }

    if response.json().get("ticket_classes", None):
        event_details["cost"] = {
            "price": response.json()
            .get("ticket_classes")[0]
            .get("cost")
            .get("major_value"),
            "currency": response.json()
            .get("ticket_classes")[0]
            .get("cost")
            .get("currency"),
        }

    if response.json().get("venue", None):
        event_details["venue"] = {
            "id": response.json().get("venue").get("id"),
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
        }

    return render(request, "event.html", {"event": event_details})


def get_organizations_and_set_choices(form: EventForm, headers: dict) -> None:
    """
    Get all organizations and set the choices for the organization field

    :param
    **form**: The form
    **headers**: The headers

    :return
    **None**

    """

    url = f"{BASE_URL}/users/me/organizations/"
    response: Response = requests.get(url=url, headers=headers, timeout=20)
    if response.status_code != 200:
        raise ValueError(f"Error fetching organizations: {response.json()}")

    all_organizations: list = [
        {
            "id": int(organization.get("id")),
            "name": organization.get("name"),
        }
        for organization in response.json().get("organizations")
    ]

    # Update the organization field's choices
    organization_choices = [
        (str(org["id"]), org["name"]) for org in all_organizations
    ]
    form.fields["organization"].choices = organization_choices


def create_event(request) -> HttpResponseRedirect | HttpResponse:
    """
    Create an event

    :param
    **request**: The request

    :return
    **HttpResponse**: The response

    """

    headers: dict[str, str] = {
        "Authorization": f"Bearer {PRIVATE_TOKEN}",
    }

    form: EventForm = EventForm(request.POST or None)

    try:
        get_organizations_and_set_choices(form, headers)

    except ValueError as e:
        return HttpResponse(str(e))

    if request.method == "POST" and form.is_valid():
        organization_id = form.cleaned_data["organization"]

        tz_finder = TimezoneFinder()
        timezone: str | None = tz_finder.timezone_at(
            lng=form.cleaned_data["longitude"],
            lat=form.cleaned_data["latitude"],
        )

        event_data: dict = {
            "event": {
                "name": {
                    "html": form.cleaned_data["name"],
                },
                "start": {
                    "timezone": timezone,
                    "utc": form.cleaned_data["start_date"]
                    .replace(tzinfo=None)
                    .strftime("%Y-%m-%dT%H:%M:%SZ"),
                },
                "end": {
                    "timezone": timezone,
                    "utc": form.cleaned_data["end_date"]
                    .replace(tzinfo=None)
                    .strftime("%Y-%m-%dT%H:%M:%SZ"),
                },
                "currency": form.cleaned_data["currency"],
            }
        }

        url: str = f"{BASE_URL}/organizations/{organization_id}/events/"

        response: Response = requests.post(
            url=url, headers=headers, json=event_data, timeout=20
        )

        if response.status_code != 200:
            return HttpResponse(f"Error: {response.json()}")

        return HttpResponseRedirect("/eventbriteAPI/organizations")

    else:
        form: EventForm = EventForm()

        url: str = f"{BASE_URL}/users/me/organizations/"
        response: Response = requests.get(url=url, headers=headers, timeout=20)

        if response.status_code != 200:
            return HttpResponse(f"Error: {response.json()}")

        form.fields["organization"].choices = [
            (int(org["id"]), org["name"])
            for org in response.json().get("organizations")
        ]

    return render(request, "create_event.html", {"form": form})
