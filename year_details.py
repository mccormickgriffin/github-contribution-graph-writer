from datetime import datetime, timedelta

SUNDAY = 6
SATURDAY = 5

class YearDetails:
    def __init__(self, year) -> None:
        self.year = year
        
        # Find first Sunday of the year
        self.first_sunday = datetime(year, 1, 1, 12, 0, 0)
        while self.first_sunday.weekday() != SUNDAY:
            self.first_sunday += timedelta(days=1)
        
        # Find last Saturday of the year
        self.last_saturday = datetime(year, 12, 31, 12, 0, 0)
        while self.last_saturday.weekday() != SATURDAY: 
            self.last_saturday -= timedelta(days=1)

        # Find number of full weeks in the year
        days_count = (self.last_saturday - self.first_sunday).days + 1
        self.full_weeks = int(days_count / 7)
    