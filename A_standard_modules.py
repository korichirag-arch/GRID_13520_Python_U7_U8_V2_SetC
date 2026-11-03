# A_standard_modules.py
from datetime import datetime, timedelta

print("Section: A - \n")
print("Q.1 Date and Time \n")
''' 1st question. '''

def is_leap_year(year):
    """Check if a given year is a leap year."""
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


years = [1700, 2016, 2026, 2200, 2032]

for year in years:
    print(f"{year} {is_leap_year(year)}")

''' 2nd question. '''
    
def day_of_week(text):
    return datetime.strptime(text, "%Y-%m-%d").strftime("%A")

dates = ['2026-05-01', '2026-10-02','2027-03-14']
for date in dates:
    print(f"{date} is a {day_of_week(date)}")

''' 3rd question. '''
date1 = datetime(2026, 3, 10)
date2 = datetime(2026, 9, 20)

difference = date2 - date1
print(f"Number of days: {difference.days}")

''' 4th question. '''

now = datetime(2026, 11, 2, 21, 45, 10)
print(f"{now.strftime('%d-%m-%Y')} {now.strftime('%m/%d/%Y')}")

print(f"{now.strftime('%H:%M:%S')} {now.strftime('%I:%M:%S %p')}")

''' 5th question. '''

now = datetime(2026, 11, 2, 21, 45, 10)
result = now + timedelta(weeks=1, days=6, hours=3)
print(result.strftime("%Y-%m-%d %H:%M:%S"))

print("\n")

print("Q2. The math and random modules. \n")
import math
import random


''' 1st question. '''
passengers = 129
bus_capacity = 25

buses_needed = math.ceil(passengers / bus_capacity)
print(buses_needed)



''' 2nd question. '''
total_seconds = 7384
hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(hours, minutes, seconds)


''' 3rd question. '''

def simplify(n, d):
    common = math.gcd(n, d)
    return (n // common, d // common)

print(simplify(36, 84))

'''' 4th question. '''

dist = 120
angle = 60

height = dist * math.tan(math.radians(angle))
print(round(height, 2))

''' 5th question. '''

random.seed(31)
rolls = [random.randint(1, 6) for _ in range(5)]
print(rolls, sum(rolls))

''' 6th question. '''

deck = list(range(1, 9))
random.shuffle(deck)
print(deck)
print(random.choice(["rock", "paper", "scissors"]))

print("\n")

print("Q3. The uuid and time modules. \n")

import uuid
import time
from datetime import timezone

''' 1st question. '''
names = ['Kavita', 'Lalit', 'Manoj', 'Nisha']
ids = {name: uuid.uuid5(uuid.NAMESPACE_DNS, name.lower() + ".example") for name in names}
for name, u in ids.items():
    print(f"{name}: {str(u)[:8]}")
all_different = len(set(ids.values())) == len(ids)
print(all_different)

''' 2nd question. '''

u3 = uuid.uuid3(uuid.NAMESPACE_DNS, "example.com")
u5 = uuid.uuid5(uuid.NAMESPACE_DNS, "example.com")

print(u3 != u5, u3.version, u5.version)

''' 3rd question. '''

ts = 1700000000
print(time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(ts)))
print(time.asctime(time.gmtime(ts)))
print(datetime.fromtimestamp(ts, timezone.utc).strftime("%d %b %Y"))

''' 4th question. '''

t0 = time.perf_counter()
total = sum(range(1_000_000))
elapsed = time.perf_counter() - t0

print(total, type(elapsed).__name__, elapsed >= 0)


















print("\n")