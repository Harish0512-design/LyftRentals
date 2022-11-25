from .enginebase import Engine


class WilloughbyEngine(Engine):
    def __init__(self, current_mileage, last_service_mileage):
        self.__current_mileage = current_mileage
        self.__last_service_mileage = last_service_mileage

    def need_service(self):
        return self.current_mileage - self.last_service_mileage > 60000
