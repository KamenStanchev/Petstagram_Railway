from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.decorators import login_required

from main_app.forms import PhotoCreateForm, PhotoEditForm, PhotoDeleteForm
from main_app.models import PetPhoto



class AddPhotoView(LoginRequiredMixin, generic.CreateView):
    template_name = 'photo_create.html'
    form_class = PhotoCreateForm
    success_url = reverse_lazy('dashboard')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            form.instance.account = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)



class PhotoDeleteView(LoginRequiredMixin, generic.DeleteView):
    template_name = 'photo_delete.html'
    model = PetPhoto
    form_class = PhotoDeleteForm

    def dispatch(self, request, *args, **kwargs):
        photo = self.get_object()
        if photo.account != self.request.user:
            return HttpResponse('<h1>It is not your photo. You can not delete it.')
        return super(PhotoDeleteView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['form'] = PhotoDeleteForm(instance=self.object)
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        return self.form_valid(form)

    context_object_name = 'photo'

    success_url = reverse_lazy('dashboard')



class PhotoEditView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'photo_edit.html'
    model = PetPhoto
    form_class = PhotoEditForm
    context_object_name = 'phototo'
    success_url = reverse_lazy('dashboard')

    def dispatch(self, request, *args, **kwargs):
        photo = self.get_object()
        if photo.account != self.request.user:
            return HttpResponse('<h1>You are trying to cheat the app. It is not your photo. You can not edit it.')
        return super(PhotoEditView, self).dispatch(request, *args, **kwargs)


class PhotoDetailsView(LoginRequiredMixin, generic.DetailView):
    template_name = 'photo_details.html'
    model = PetPhoto
    context_object_name = 'phototo'


@login_required()
def like_photo(request, pk):
    pet_photo = PetPhoto.objects.get(id=pk)
    current_user = request.user
    accounts_in_liked_photo = pet_photo.list_who_like_photo.all()
    if current_user not in accounts_in_liked_photo:
        pet_photo.likes += 1
        pet_photo.list_who_like_photo.add(current_user)
        pet_photo.save()
        messages.success(request, 'You liked this photo')
    else:
        messages.error(request, 'You already liked this photo')
    return redirect('photo_details', pk)
