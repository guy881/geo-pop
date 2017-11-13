class DriversRepository:
    @staticmethod
    def add_driver(driver):
        driver.save()

    @staticmethod
    def update_driver(driver):
        driver.save()

    @staticmethod
    def modify_schedule(listOfAvailability):
        # TODO discuss how it should be handled and stored
        return "not implemented yet"

    @staticmethod
    def delete_driver(driver):
        driver.delete()
