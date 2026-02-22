from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    """
    Render the home page of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home/index.html',  {"title": "home", "data": "Welcome to the home page"})


def about(request: HttpRequest) -> HttpResponse:
    """
    Render the about page of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered about page template.
    """
    return render(request, 'home/index.html', {"title": "about", "data": "Welcome to the about page"})


def contact(request: HttpRequest) -> HttpResponse:
    """
    Render the contact page of the application.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: Rendered contact page template.
    """
    return render(request, 'home/index.html', {"title": "contact", "data": "Welcome to the contact page"})


def post(request: HttpRequest, post_id: int) -> HttpResponse:
    """
    Render a page displaying a post by its ID.

    Args:
        request (HttpRequest): The HTTP request object.
        post_id (int): The unique identifier of the post.

    Returns:
        HttpResponse: Rendered post page template with the post ID.
    """
    return render(request, 'home/index.html', {"title": f" post id: {post_id}"})


def profile(request: HttpRequest, username: str) -> HttpResponse:
    """
    Render a user profile page.

    Args:
        request (HttpRequest): The HTTP request object.
        username (str): The username of the profile to display.

    Returns:
        HttpResponse: Rendered profile page template with the username.
    """
    return render(request, 'home/index.html', {"title": f"username: {username}"})


def event(request: HttpRequest, year: int, month: int, day: int) -> HttpResponse:
    """
    Render a page for an event with a specific date.

    Args:
        request (HttpRequest): The HTTP request object.
        year (int): The year of the event.
        month (int): The month of the event.
        day (int): The day of the event.

    Returns:
        HttpResponse: Rendered event page template with the date context.
    """
    return render(request, 'home/index.html', {"title": f"year: {year}, month: {month}, day: {day}"})

