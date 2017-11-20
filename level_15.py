# LEVEL 15
# http://www.pythonchallenge.com/pc/return/uzi.html

import calendar
import datetime

for year in range(2016, 1582, -1):
    if calendar.isleap(year):
        if datetime.date(year, 1, 1).weekday() == 3:  # 3=Thursday
            if str(year)[0] == '1' and str(year)[3] == '6':
                print(year)
