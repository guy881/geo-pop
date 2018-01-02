import base64
from io import BytesIO
import django_filters

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.paginator import EmptyPage, PageNotAnInteger
from django.forms import modelform_factory
from django.http import Http404
from django.http import HttpResponseRedirect
from django.shortcuts import reverse, get_object_or_404, render
from django.utils.translation import ugettext_lazy as _
from django.views import generic
from rest_framework.response import Response
from rest_framework.views import APIView
from django.urls import reverse_lazy

from drivers.serializers import DriverSerializer
from . import forms
from .models import Driver


class DriverList(LoginRequiredMixin, generic.ListView):
    template_name = 'drivers/list.html'
    model = Driver
    paginate_by = 6

    def get(self, request, *args, **kwargs):
        ret = super().get(request, *args, **kwargs)
        page = request.GET.get('page', None)
        paginator = ret.context_data['paginator']
        try:
            paginator = paginator.page(page)
        except PageNotAnInteger:
            paginator = paginator.page(1)
        except EmptyPage:
            paginator = paginator.page(paginator.num_pages)

        ret.context_data['paginator'] = paginator
        return ret

    def get_queryset(self):
        return Driver.objects.all().order_by('pesel')


class DriverFilter(django_filters.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Driver
        fields = ['schedule__id']

def driver_schedule(request):
    filter = DriverFilter(request.GET, queryset=Driver.objects.all())
    return render(request, 'drivers/schedule.html', {'filter': filter})


class DriverDeleteView(LoginRequiredMixin, generic.DeleteView):
    model = Driver
    template_name = 'drivers/delete_form.html'
    success_url = reverse_lazy('drivers:list')

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            messages.success(request, 'Nie jesteś członkiem zespołu. Nie mozesz usuwac kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        elif "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano usuniecie kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        else:
            messages.success(self.request, 'Pomyślnie usunieto kierowce')
            return super().post(request, *args, **kwargs)

class DriverCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = forms.DriverBasicForm
    template_name = 'drivers/create_form.html'

    def post(self, request, *args, **kwargs):
        if not self.request.user.is_staff:
            messages.success(request, 'Nie jesteś członkiem zespołu. Nie mozesz dodawać kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        elif "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano dodawanie kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        else:
            messages.success(self.request, 'Pomyślnie dodawano kierowce')
            return super().post(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

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
        form1 = forms.DriverBasicForm(request.POST)
        if not self.request.user.is_staff:
            messages.success(request, 'Nie jesteś członkiem zespołu. Nie mozesz dodawać kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        elif "cancel" in request.POST:
            messages.error(request, 'Pomyślnie anulowano dodawanie kierowcy')
            return HttpResponseRedirect(reverse('drivers:list'))
        elif form1.is_valid():
            super(DriverEditBasic, self).post(self, request, *args, **kwargs)
            messages.success(request, _('Pomyślnie edytowano kierowce'))
            return HttpResponseRedirect(reverse('drivers:list'))
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
                messages.error(request, _('Proszę wypełnij poprawnie wszystkie pola!'))
        else:
            # form1 = forms.DriverImageForm(request.POST, validate=False)
            messages.success(request, _('Zapisano poprawnie!'))
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
                messages.error(request, _('Proszę wypełnij wszystkie wymagane pola!'))
        else:
            messages.success(request, _('Dane zapisane poprawnie!!'))
        return super(DriverEditCars, self).post(request, *args, **kwargs)


class DriverDetailAPIView(APIView, LoginRequiredMixin, ):
    def get_object(self, user_id):
        try:
            return Driver.objects.get(user=user_id)
        except Driver.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        driver = self.get_object(request.user.id)
        serializer = DriverSerializer(driver)
        return Response(serializer.data)
