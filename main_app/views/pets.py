from django.shortcuts import redirect
from django.views import generic

from main_app.forms import PetForm, EditPetForm, DeletePetForm
from main_app.models import Pet
from django.urls import reverse_lazy, reverse


class AddPetView(generic.CreateView):
    template_name = 'pet_create.html'
    form_class = PetForm
    success_url = reverse_lazy('account_detail')

    # it is use if one user have to have only one Pet
    # def dispatch(self, request, *args, **kwargs):
    #     if Pet.objects.filter(account=self.request.user):
    #         return redirect('account_detail')
    #     return super(AddPetView, self).dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        user = request.user
        if form.is_valid():
            form.instance.account = user
            return self.form_valid(form)
        else:
            return self.form_invalid(form)


class PetEditView(generic.UpdateView):
    template_name = 'pet_edit.html'
    model = Pet
    form_class = EditPetForm
    success_url = reverse_lazy('account_detail')

    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.account != self.request.user:
            return redirect('dashboard')
        return super(PetEditView, self).dispatch(request, *args, **kwargs)


class PetDeleteView(generic.DeleteView):
    template_name = 'pet_delete.html'
    model = Pet
    form_class = DeletePetForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        context['form'] = DeletePetForm(instance=self.object)
        return self.render_to_response(context)

    def dispatch(self, request, *args, **kwargs):
        pet = self.get_object()
        if pet.account != self.request.user:
            return redirect('dashboard')
        return super(PetDeleteView, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        return reverse('profile_details')

