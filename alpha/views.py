from django.views.generic.base import TemplateView


class HomeView(TemplateView):
    """Home page template view."""

    template_name = 'home.html'
