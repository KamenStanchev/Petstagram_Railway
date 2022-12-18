from django.views import generic

from main_app.models import PetPhoto


class HomePageView(generic.TemplateView):
    template_name = 'home_page.html'

    def get_context_data(self, **kwargs):
        context = super(HomePageView, self).get_context_data(**kwargs)
        context['hide_additional_nav_item'] = True
        return context


class DashboardView(generic.ListView):
    template_name = 'dashboard.html'
    model = PetPhoto
    context_object_name = 'pet_photos'


