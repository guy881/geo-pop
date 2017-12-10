from django.core.management import BaseCommand

from regions.models import Region


class Command(BaseCommand):
    help = "Ile obszarów ma być zaktualizowanych"

    def add_arguments(self, parser):
        parser.add_argument('regions_num', nargs='+', type=int)

    def handle(self, *args, **options):
        for i, reg in enumerate(Region.objects.all()):
            if i < options['regions_num'][0]:
                reg.is_updated = True
            else:
                reg.is_updated = False
            reg.save()
