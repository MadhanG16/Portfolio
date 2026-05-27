"""
Views for the portfolio app.
Renders the main portfolio page and handles the contact form.
"""
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_protect
from .models import ContactMessage


def index(request):
    """
    Main portfolio page view.
    All portfolio data is hardcoded in templates for simplicity,
    but models are available for dynamic content via admin.
    """
    context = {
        'page_title': 'Madhan G | Python Developer & Full Stack Learner',
        'meta_description': 'Portfolio of Madhan G - Python Developer, Django Developer, and Full Stack Learner. Building scalable web applications with modern technologies.',
    }
    return render(request, 'core/index.html', context)


@csrf_protect
@require_POST
def contact_form(request):
    """
    Handle contact form submissions via AJAX.
    Saves message to the database and returns JSON response.
    """
    try:
        name = request.POST.get('name', '').strip()
        email = request.POST.get('email', '').strip()
        message = request.POST.get('message', '').strip()

        # Validate fields
        if not all([name, email, message]):
            return JsonResponse({
                'status': 'error',
                'message': 'All fields are required.'
            }, status=400)

        if len(name) < 2:
            return JsonResponse({
                'status': 'error',
                'message': 'Name must be at least 2 characters.'
            }, status=400)

        if '@' not in email or '.' not in email:
            return JsonResponse({
                'status': 'error',
                'message': 'Please enter a valid email address.'
            }, status=400)

        if len(message) < 10:
            return JsonResponse({
                'status': 'error',
                'message': 'Message must be at least 10 characters.'
            }, status=400)

        # Save to database
        ContactMessage.objects.create(
            name=name,
            email=email,
            message=message
        )

        return JsonResponse({
            'status': 'success',
            'message': 'Thank you! Your message has been sent successfully.'
        })

    except Exception as e:
        return JsonResponse({
            'status': 'error',
            'message': 'Something went wrong. Please try again.'
        }, status=500)
