from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib import messages

from main_app.forms import EditProfileForm
from main_app.models import Profile


class CreateProfileView(LoginRequiredMixin, generic.CreateView):
    template_name = 'profile_create.html'
    model = Profile
    form_class = EditProfileForm
    success_url = reverse_lazy('home_page')

    def dispatch(self, request, *args, **kwargs):
        if Profile.objects.filter(account=self.request.user):
            return redirect('account_detail')
        return super(CreateProfileView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            form.instance.account = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


# class ProfileEditView(generic.UpdateView):
#     template_name = 'profile_edit.html'
#     model = Profile
#     form_class = EditProfileForm
#     success_url = reverse_lazy('account_detail')
#     messages.success('Profile was updated')
#
#     def dispatch(self, request, *args, **kwargs):
#         profile = self.get_object()
#         if profile.account != self.request.user:
#             return redirect('account_detail')
#         return super(ProfileEditView, self).dispatch(request, *args, **kwargs)


class ProfileDeleteView(generic.DeleteView):
    template_name = 'profile_delete.html'
    model = Profile
    success_url = reverse_lazy('home_page')

    def dispatch(self, request, *args, **kwargs):
        profile = self.get_object()
        if profile.account != self.request.user:
            return redirect('account_detail')
        return super(ProfileDeleteView, self).dispatch(request, *args, **kwargs)


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['full_name'] = f'{self.object.first_name} {self.object.last_name}'
        context['picture'] = self.object.picture
        return self.render_to_response(context)
