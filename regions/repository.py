
class RegionsRepository:

    @staticmethod
    def add_region(region):
        region.save()

    @staticmethod
    def update_region(region):
        region.save()

    @staticmethod
    def modify_schedule(listOfAvailability):
        # TODO discuss how it should be handled and stored
        return "not implemented yet"

    @staticmethod
    def delete_region(region):
        region.delete()
