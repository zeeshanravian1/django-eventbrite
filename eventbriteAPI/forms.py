from django import forms


class EventForm(forms.Form):
    """
    Form for creating an event
    """

    organization: forms.ChoiceField = forms.ChoiceField(
        label="Organization",
        choices=(),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    name: forms.CharField = forms.CharField(
        label="Name",
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Event Name"}
        ),
    )
    # description: forms.CharField = forms.CharField(
    #     label="Description",
    #     max_length=100,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Event Description"}
    #     ),
    # )
    start_date: forms.DateTimeField = forms.DateTimeField(
        label="Start Date",
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    end_date: forms.DateTimeField = forms.DateTimeField(
        label="End Date",
        widget=forms.DateTimeInput(
            format="%Y-%m-%dT%H:%M",
            attrs={"class": "form-control", "type": "datetime-local"},
        ),
        input_formats=["%Y-%m-%dT%H:%M"],
    )
    currency: forms.CharField = forms.ChoiceField(
        label="Currency",
        choices=(
            ("USD", "USD"),
            ("PKR", "PKR"),
            ("EUR", "EUR"),
            ("GBP", "GBP"),
            ("INR", "INR"),
        ),
        widget=forms.Select(attrs={"class": "form-control"}),
    )
    # price: forms.DecimalField = forms.DecimalField(
    #     label="Price",
    #     max_digits=10,
    #     decimal_places=2,
    #     widget=forms.NumberInput(
    #         attrs={"class": "form-control", "placeholder": "Price"}
    #     ),
    # )
    longitude: forms.DecimalField = forms.DecimalField(
        label="Longitude",
        max_digits=50,
        required=False,
        decimal_places=20,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Longitude"}
        ),
    )
    latitude: forms.DecimalField = forms.DecimalField(
        label="Latitude",
        max_digits=50,
        required=False,
        decimal_places=20,
        widget=forms.NumberInput(
            attrs={"class": "form-control", "placeholder": "Latitude"}
        ),
    )
    # country: forms.CharField = forms.CharField(
    #     label="Country",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Country"}
    #     ),
    # )
    # city: forms.CharField = forms.CharField(
    #     label="City",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "City"}
    #     ),
    # )
    # region: forms.CharField = forms.CharField(
    #     label="Region",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Region"}
    #     ),
    # )
    # postal_code: forms.CharField = forms.CharField(
    #     label="Postal Code",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Postal Code"}
    #     ),
    # )
    # address: forms.CharField = forms.CharField(
    #     label="Address",
    #     max_length=100,
    #     required=False,
    #     widget=forms.TextInput(
    #         attrs={"class": "form-control", "placeholder": "Address"}
    #     ),
    # )
    # capacity: forms.IntegerField = forms.IntegerField(
    #     label="Capacity",
    #     widget=forms.NumberInput(
    #         attrs={"class": "form-control", "placeholder": "Capacity"}
    #     ),
    # )

    # def clean(self) -> dict[str, any]:
    #     cleaned_data = super().clean()
    #     latitude = cleaned_data.get("latitude")
    #     longitude = cleaned_data.get("longitude")
    #     country = cleaned_data.get("country")
    #     city = cleaned_data.get("city")
    #     region = cleaned_data.get("region")
    #     postal_code = cleaned_data.get("postal_code")
    #     address = cleaned_data.get("address")

    #     if not all((country, city, region, postal_code, address)) and not any(
    #         (latitude, longitude)
    #     ):
    #         raise forms.ValidationError(
    #             "If country, city, region, postal code, and address are not provided, latitude and longitude must be provided."
    #         )

    #     return cleaned_data
