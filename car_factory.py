from datetime import datetime
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class CarFactory:

    def create_calliope(self,current_date,last_service_date, current_mileage, last_service_mileage):
        
        return Car(CapuletEngine(current_mileage,last_service_mileage),SpindlerBattery(last_service_date,current_date))

    def create_glissade(self,current_date, last_service_date ,current_mileage, last_service_mileage):
        
        return Car(WilloughbyEngine(current_mileage,last_service_mileage),SpindlerBattery(last_service_date,current_date))

    def create_palindrome(self,current_date, last_service_date, warning_light_on):

        return Car(SternmanEngine(warning_light_on),SpindlerBattery(last_service_date,current_date))

    def create_rorschach(self,current_date, last_service_date ,current_mileage, last_service_mileage):
        
         return Car(WilloughbyEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date))

    def create_thovex(self,current_date ,last_service_date ,current_mileage, last_service_mileage):
        
        return Car(CapuletEngine(current_mileage,last_service_mileage),NubbinBattery(last_service_date,current_date))


if __name__ == '__main__':
    today = datetime.today().date()
    c1 = CarFactory().create_palindrome(today.year,today.year-5,True)
    car = c1.need_service()
    print(car)