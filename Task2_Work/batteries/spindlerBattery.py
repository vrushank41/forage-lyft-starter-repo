from battery_parent import Battery
from datetime import date,datetime

class SpindlerBattery(Battery):
    current_date:date
    last_service_date:date
    def __init__(self,current_date,last_service_date):
        super().__init__()
        self.current_date=current_date
        self.last_service_date=last_service_date
    
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 2)
        if service_threshold_date < datetime.today().date():
            return True
        else:
            return False