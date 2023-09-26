import calendar
def test(m, y): 
    return str(calendar.weekday(y, m, 13) == 4)

month =10
year =2023          
print(f"Friday 13th in {month},{year}: " + test(month, year))
