def isValid(driver):
    #TODO define rules to validate
    return True


def NoTasksPending(driver):
    #TODO specify bussiness flow
    return True


class DriversRepository:

    def addDriver(self, driver):
        if isValid(driver):
            driver.save()

    def updateDriver(self, driver):
        if isValid(driver):
            driver

    def modifySchedule(self, listOfAvailability):
        #TODO discuss how it should be handled and stored
        return "not implemented yet"
    

    def deleteDriver(self, driver):
        if NoTasksPending(driver):
            driver.delete()