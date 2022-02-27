from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, View


class BaseAddView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(self.redirect_target))
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class BaseEditView(LoginRequiredMixin, View):
    def get(self, request, id, *args, **kwargs):
        obj = get_object_or_404(self.model_class, id=id)
        obj.deletable, _ = obj.is_deletable()
        form = self.form_class(request.POST or None, instance=obj)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'obj': obj,
            }
        )

    def post(self, request, id, *args, **kwargs):
        obj = get_object_or_404(self.model_class, id=id)
        form = self.form_class(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(self.redirect_target))
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class SlugEditView(LoginRequiredMixin, View):
    def get(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        obj.deletable, _ = obj.is_deletable()
        form = self.form_class(request.POST or None, instance=obj)
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'obj': obj,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        form = self.form_class(request.POST or None, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse(self.redirect_target))
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class BaseDeleteView(LoginRequiredMixin, View):    
    def get(self, request, id, *args, **kwargs):
        obj = get_object_or_404(self.model_class, id=id)
        obj.deletable, _ = obj.is_deletable()
        return render(
            request,
            self.template_name,
            {
                'obj': obj,
            }
        )

    def post(self, request, id, *args, **kwargs):
        obj = get_object_or_404(self.model_class, id=id)
        obj.delete()
        return redirect(reverse(self.redirect_target))


class SlugDeleteView(LoginRequiredMixin, View):
    def get(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        obj.deletable, _ = obj.is_deletable()
        return render(
            request,
            self.template_name,
            {
                'obj': obj,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        obj.delete()
        return redirect(reverse(self.redirect_target))


class BaseListView(LoginRequiredMixin, ListView):
    pass
