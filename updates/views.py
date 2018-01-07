import datetime

from django_common.mixin import LoginRequiredMixin
from rest_framework.parsers import MultiPartParser
from rest_framework.response import Response
from rest_framework.views import APIView

from drivers.models import Driver
from regions.models import Region, GeoLocalization
from updates.models import Obstacle


class CreateUpdateAPI(APIView, LoginRequiredMixin):
    parser_classes = (MultiPartParser,)

    def post(self, request, filename='sdds.jpg', format=None):
        driver = Driver.objects.filter(user=request.user).first()
        if driver is not None:
            file_obj = request.FILES['file']
            lat = float(request.POST.get('lat'))
            long = float(request.POST.get('long'))
            location = GeoLocalization(latitude=lat, longitude=long)
            location.save()
            photo = Obstacle.Photo(location=location,
                                   send_date=datetime.datetime.now(),
                                   image=file_obj,
                                   driver=driver)

            photo.save()
            # update region
            region = Region.objects.filter(
                    north_west__latitude__gt=lat,
                    north_west__longitude__lt=long,
                    south_east__latitude__lt=lat,
                    south_east__longitude__gt=long).first()
            if region is not None:
                region.is_updated = True
                region.last_updated = datetime.datetime.now()
                region.updated_by = 'DRV'
                region.save()
            return Response(status=200, data="Great photo- you look beautiful")
        else:
            return Response(status=401, data='Ten użytkownik nie jest kierowcą więc nie może dodawć zdjęć.')
