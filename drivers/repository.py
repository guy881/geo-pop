def is_valid(driver):
    #TODO define rules to validate
    return True


def no_task_pending(driver):
    #TODO specify bussiness flow
    return True


class DriversRepository:

    def add_driver(self, driver):
        if is_valid(driver):
            driver.save()

    def update_driver(self, driver):
        if is_valid(driver):
            driver

    def modify_schedule(self, listOfAvailability):
        #TODO discuss how it should be handled and stored
        return "not implemented yet"
    

    def delete_driver(self, driver):
        if no_task_pending(driver):
            driver.delete()