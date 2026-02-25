from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.views import View
from datetime import datetime
from typing import Dict, List, Optional


def main_home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page with a title.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home.html template with context.
    """
    return render(request, "main/home.html", {"title": "Home"})


def main_about(request: HttpRequest) -> HttpResponse:
    """
    Render the about page with company description and current date.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about.html template with context.
    """
    context: Dict[str, object] = {
        "title": "About",
        "description": "some description",
        "date": datetime.now(),
    }
    return render(request, "main/about.html", context)


class ContactView(View):
    """
    Class-based view to display contact information.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET request and render contact page.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered contact.html template with contact info.
        """
        contacts: Dict[str, str] = {
            "address": "some address",
            "phone": "",
            "email": "company@mail.com"
        }
        context: Dict[str, object] = {
            "contacts": contacts,
            "has_contact": bool(contacts["email"])
        }
        return render(request, "main/contact.html", context)


class ServiceView(View):
    """
    Class-based view to display list of services with optional search.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        """
        Handle GET request and render services page.
        Filters services based on optional search query.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: Rendered services.html template with services list and date.
        """
        services: List[Dict[str, str]] = [
            {"name": "product1", "description": "cheap"},
            {"name": "product2", "description": "middle quality"},
            {"name": "product3", "description": "premium"}
        ]

        keyword: Optional[str] = request.GET.get('q')

        if keyword:
            services = [s for s in services if keyword.lower() in s["name"].lower()]

        context: Dict[str, object] = {
            "services": services,
            "date": datetime.now()
        }

        return render(request, "main/services.html", context)
