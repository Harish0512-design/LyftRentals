import datetime
from .batterybase import Battery


class NubbinBattery(Battery):
    def __init__(self,last_service_date,current_date):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def need_service(self):
        return self.__current_date >= self.__last_service_date + 4