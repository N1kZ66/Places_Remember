from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView
from .models import Memories
from django.contrib.auth.mixins import LoginRequiredMixin


class BasePlaceView(ListView):
    template_name = 'base.html'
    model = Memories


class ListPlaceView(LoginRequiredMixin, ListView):
    template_name = 'index.html'
    model = Memories

    def get_queryset(self):
        queryset = super(ListPlaceView, self).get_queryset()
        queryset = queryset.filter(author=self.request.user)
        return queryset


class CreatePlaceView(CreateView):
    template_name = 'create.html'
    model = Memories
    success_url = reverse_lazy('home')
    fields = ['title', 'comment', 'location']

    def form_valid(self, form):
        form.instance.author = self.request.user
        if form_id:
            try:
                form = form.objects.get(id=form_id)
            except ObjectDoesNotExist:
                form = form.objects.create(form_id="Random")
        else:
            form = form.objects.create(form_id="Random")
        return super(CreatePlaceView, self).form_valid(form)


class UpdatePlaceView(UpdateView):
    model = Memories
    fields = ['title', 'comment', 'location']
    success_url = reverse_lazy('home')
    template_name = 'update.html'


class DeletePlaceView(DeleteView):
    template_name = 'delete.html'
    model = Memories
    success_url = reverse_lazy('home')