import base64
from io import BytesIO
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import EmptyPage
from django.forms import modelform_factory
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, get_object_or_404
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from . import forms
from .models import Driver


class DriverList(LoginRequiredMixin, generic.ListView):
    template_name = 'drivers/list.html'
    model = Driver
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        ret = super().get(request, *args, **kwargs)
        page = request.GET.get('page', None)
        num_pages = ret.context_data['paginator'].num_pages

        try:
            page = int(page)
            pages = range(page - 2 if page - 2 > 0 else 1, page + 3 if page + 3 <= num_pages + 1 else num_pages + 1)
        except EmptyPage:
            page = num_pages
            pages = range(page - 2 if page - 2 > 0 else 1, num_pages + 1)
        except:
            page = 1
            pages = range(page - 2 if page - 2 > 0 else 1, page + 3 if page + 3 <= num_pages + 1 else num_pages + 1)

        ret.context_data['pages'] = pages
        return ret

    def get_queryset(self):
        return Driver.objects.all().order_by('pesel')


class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.DriverBasicForm
    template_name = 'drivers/create_form.html'

    def post(self, request, *args, **kwargs):
        if self.request.user.is_staff:
            return super().post(request, *args, **kwargs)
        else:
            print('oks')
            return reverse('drivers:create', kwargs={'error': 'You are not a staff member'})

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('drivers:list')


class DriverEditBasic(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.DriverBasicForm
    template_name = 'drivers/edit_form.html'

    def get_queryset(self):
        return Driver.objects.all()

    def get_success_url(self):
        return reverse('drivers:list')

    def post(self, request, *args, **kwargs):
        # next_btn = request.POST.get('next', None)
        form1 = forms.DriverBasicForm(request.POST)

        if form1.is_valid():
            super(DriverEditBasic, self).post(self, request, *args, **kwargs)
            return HttpResponseRedirect(reverse('drivers:list'))
        else:
            kwargs['error'] = _('Please fill out all required fields!')
        kwargs['success'] = _('Data saved correctly!')
        return super(DriverEditBasic, self).post(self, request, *args, **kwargs)

class DriverEditImage(LoginRequiredMixin, generic.UpdateView):
    # form_class = forms.AllImagesForm
    model = Driver
    fields = ['image', ]
    template_name = 'drivers/image_form.html'

    def get_form_class(self):
        form = modelform_factory(Driver, fields=self.fields)
        return form

    def get_queryset(self):
        return Driver.objects.all()

    def get_success_url(self):
        return reverse('drivers:edit_cars', kwargs={'pk': self.object.pk})

    def post(self, request, *args, **kwargs):
        back_btn = request.POST.get('back', None)
        next_btn = request.POST.get('next', None)
        instance = get_object_or_404(Driver, pk=self.kwargs['pk'])
        form_class = self.get_form_class()
        for field in form_class.base_fields.keys():
            filename = None
            upload_field = 'upload_%s' % field
            if request.FILES.get(upload_field):
                filename = request.FILES[upload_field].name
            elif instance:
                filename = instance.image.name

            if filename and request.POST.get(field):
                file = BytesIO(base64.b64decode(request.POST[field].split('base64,')[1]))
                image = InMemoryUploadedFile(file,
                                             field_name='file',
                                             name=filename,
                                             content_type="image/png",
                                             size=len(file.getvalue()),
                                             charset=None)
                request.FILES[field] = image

        if back_btn:
            return HttpResponseRedirect(reverse('drivers:edit_basic', kwargs={'pk': kwargs['pk']}))
        if next_btn:
            form1 = form_class(request.POST)
            if form1.is_valid():
                super(DriverEditImage, self).post(self, request, *args, **kwargs)
                return HttpResponseRedirect(reverse('drivers:edit_cars', kwargs={'pk': kwargs['pk']}))
            else:
                kwargs['error'] = _('Please fill out all required fields!')
        else:
            # form1 = forms.DriverImageForm(request.POST, validate=False)
            kwargs['success'] = _('Data saved correctly!')
        return super(DriverEditImage, self).post(self, request, *args, **kwargs)


class DriverEditCars(LoginRequiredMixin, generic.UpdateView):
    form_class = forms.DriverCarsForm
    prefix = 'parent_form'
    template_name = 'drivers/driver_cars_form.html'

    def get_queryset(self):
        return Driver.objects.all()

    def get_success_url(self):
        return reverse('drivers:edit_cars', kwargs={'pk': self.kwargs['pk']})

    def get_context_data(self, **kwargs):
        obj = get_object_or_404(Driver, pk=self.kwargs['pk'])
        post_data = self.request.POST or None

        if obj.car_set.all().count() == 0:
            form = forms.CarFormSet(post_data, instance=obj)
        else:
            form = forms.CarFormSet_no_extra(post_data, instance=obj)
        context = super(DriverEditCars, self).get_context_data(**kwargs)
        context['parent_form'] = context['form']
        context['form'] = form
        return context

    def post(self, request, *args, **kwargs):
        back_btn = request.POST.get('back', None)
        next_btn = request.POST.get('next', None)
        # back without save
        if back_btn:
            return HttpResponseRedirect(reverse('drivers:edit_image', kwargs={'pk': kwargs['pk']}))

        obj = get_object_or_404(Driver, pk=self.kwargs['pk'])
        post_data = request.POST or None
        form = forms.CarFormSet(post_data, instance=obj)
        parent_form = forms.DriverCarsForm(request.POST or None, instance=obj, prefix='parent_form')
        if parent_form.is_valid() and form.is_valid():
            form.save()

        if back_btn:
            return HttpResponseRedirect(reverse('driver_edit_image', kwargs={'pk': kwargs['pk']}))
        elif next_btn:
            if form.is_valid() and parent_form.is_valid():
                super(DriverEditCars, self).post(request, *args, **kwargs)
                return HttpResponseRedirect(reverse('drivers:edit_cars', kwargs={'pk': kwargs['pk']}))
            else:
                kwargs['error'] = _('Please fill out all required fields!')
        else:
            kwargs['success'] = _('Data saved correctly!')
        return super(DriverEditCars, self).post(request, *args, **kwargs)
