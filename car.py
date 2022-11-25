from serviceable import Serviceable
from abc import ABC

class Car(Serviceable):
    def __init__(self, engine,battery):
        self.__engine = engine
        self.__battery = battery
    
    def need_service(self):
        return True if self.__engine.need_service() or self.__battery.need_service() == True else False
