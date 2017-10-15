from pandas.tseries.holiday import USFederalHolidayCalendar
cal = USFederalHolidayCalendar()
holidays = cal.holidays(start='2014-01-01', end='2014-12-31').to_pydatetime()
if datetime.datetime(2014,01,01) in holidays:
    print True 
