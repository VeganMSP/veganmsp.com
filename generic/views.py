from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.utils.datastructures import MultiValueDictKeyError
from django.views.generic import ListView, View

from info.forms import AddressModelForm, LinkCategoryModelForm
from info.models import LinkCategory


class BaseAddView(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
    add_another = False

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={
            'add_another': self.add_another,
        })
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        try:
            if request.POST['add_another'] == 'on':
                self.add_another = True
        except MultiValueDictKeyError:
            self.add_another = False
        if form.is_valid():
            form.save()
            if self.add_another:
                pass
            else:
                return redirect(self.redirect_target)
        form = self.form_class(initial={
            'add_another': self.add_another
        })
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class BaseAddViewWithAddressForm(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
    add_another = False

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={
            'add_another': self.add_another,
        })
        address_form = AddressModelForm(prefix='address')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'address_form': address_form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        address_form = AddressModelForm(request.POST, prefix='address')
        try:
            if request.POST['add_another'] == 'on':
                self.add_another = True
        except MultiValueDictKeyError:
            self.add_another = False
        if form.is_valid() and address_form.is_valid():
            address = address_form.save()
            fm = form.save(commit=False)
            fm.address = address
            fm.save()
            if self.add_another:
                pass
            else:
                return redirect(self.redirect_target)
        form = self.form_class(initial={
            'add_another': self.add_another,
        })
        address_form = AddressModelForm(prefix='address')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'address_form': address_form,
            }
        )


class BaseAddViewWithLinkCategoryForm(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
    add_another = False

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial={
            'add_another': self.add_another,
        })
        link_category_form = LinkCategoryModelForm(prefix='link_category')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'link_category_form': link_category_form,
            }
        )

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        link_category_form = LinkCategoryModelForm(
            request.POST, prefix='link_category'
        )
        try:
            if request.POST['add_another'] == 'on':
                self.add_another = True
        except MultiValueDictKeyError:
            self.add_another = False
        if form.is_valid() and link_category_form.is_valid():
            try:
                link_category = LinkCategory.objects.get(
                    name=link_category_form.cleaned_data["name"]
                )
            except LinkCategory.DoesNotExist:
                link_category = link_category_form.save()
            link = form.save(commit=False)
            link.category = link_category
            link.save()
            if self.add_another:
                pass
            else:
                return redirect(self.redirect_target)
        form = self.form_class(initial={
            'add_another': self.add_another
        })
        link_category_form = LinkCategoryModelForm(prefix='link_category')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'link_category_form': link_category_form,
            }
        )


class BaseEditView(LoginRequiredMixin, View):
    # pylint: disable=unused-argument, redefined-builtin
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
            return redirect(self.redirect_target)
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class SlugEditViewWithAddressForm(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
    def get(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        obj.deletable, _ = obj.is_deletable()
        form = self.form_class(request.POST or None, instance=obj)
        address_form = AddressModelForm(
            request.POST or None, instance=obj.address, prefix='address'
        )
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'address_form': address_form,
                'obj': obj,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        form = self.form_class(request.POST or None, instance=obj)
        address_form = AddressModelForm(
            request.POST or None, instance=obj.address, prefix='address'
        )
        if form.is_valid() and address_form.is_valid():
            address_form.save()
            form.save()
            return redirect(self.redirect_target)
        form = self.form_class()
        address_form = AddressModelForm(prefix='address')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'address_form': address_form,
            }
        )


class SlugEditViewWithLinkCategoryForm(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
    def get(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        obj.deletable, _ = obj.is_deletable()
        form = self.form_class(request.POST or None, instance=obj)
        link_category_form = LinkCategoryModelForm(
            request.POST or None, instance=obj.category, prefix='link_category'
        )
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'link_category_form': link_category_form,
                'obj': obj,
            }
        )

    def post(self, request, slug, *args, **kwargs):
        obj = get_object_or_404(self.model_class, slug=slug)
        form = self.form_class(request.POST or None, instance=obj)
        link_category_form = LinkCategoryModelForm(
            request.POST or None, instance=obj.category, prefix='link_category'
        )
        if form.is_valid() and link_category_form.is_valid():
            link_category_form.save()
            form.save()
            return redirect(self.redirect_target)
        form = self.form_class()
        link_category_form = LinkCategoryModelForm(prefix='link_category')
        return render(
            request,
            self.template_name,
            {
                'form': form,
                'link_category_form': link_category_form,
            }
        )


class SlugEditView(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
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
            return redirect(self.redirect_target)
        form = self.form_class()
        return render(
            request,
            self.template_name,
            {
                'form': form,
            }
        )


class BaseDeleteView(LoginRequiredMixin, View):
    # pylint: disable=unused-argument, redefined-builtin
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
        return redirect(self.redirect_target)


class SlugDeleteView(LoginRequiredMixin, View):
    # pylint: disable=unused-argument
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
        return redirect(self.redirect_target)


class BaseListView(LoginRequiredMixin, ListView):  # pylint: disable=too-many-ancestors
    pass
