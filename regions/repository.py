
class RegionsRepository:

    @staticmethod
    def add_region(region):
        region.save()

    @staticmethod
    def update_region(region):
        region.save()

    @staticmethod
    def delete_region(region):
        region.delete()
