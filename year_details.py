from datetime import datetime, timedelta

SUNDAY = 6
SATURDAY = 5

class YearDetails:
    def __init__(self, year) -> None:
        self.year = year
        
        # Find first Sunday of the year
        date = datetime(year, 1, 1)
        while date.weekday() != SUNDAY:
            date += timedelta(days=1)
        self.first_sunday = date
        
        # Find last Saturday of the year
        date = datetime(year, 12, 31)
        while date.weekday() != SATURDAY: 
            date -= timedelta(days=1)
        self.last_saturday = date

        # Find number of full weeks in the year
        days_count = (self.last_saturday - self.first_sunday).days + 1
        self.full_weeks = int(days_count / 7)
    