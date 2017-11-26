from cars.models import Car


class CarsRepository:
    @staticmethod
    def add_car(car):
        car.save()

    @staticmethod
    def update_car(car):
        car.save()

    @staticmethod
    def delete_car(car):
        car.delete()

    @staticmethod
    def get_all_cars():
        return Car.objects.all()
