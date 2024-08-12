# Standalone and easy Python time Object

![image](https://wallpapercave.com/wp/wp4491645.png)

Yeah I know, `time` module does that pretty decently but I got bored. This allows you to addition, substract, convert timezone. ates aren't supported so days are relative to each others (+1, +2, -1...) like when talking about yesterday, tomorrow...

```python
class TimeStamp:
    def __init__(self, hour, minutes=0, seconds=0, utc=0, day=0):
        assert hour < 24 and hour >= 0
        assert minutes >= 0 and minutes < 60
        assert seconds >=0 and seconds < 60
        self.hour = hour
        self.minutes = minutes
        self.seconds = seconds
        self.utc = utc
        self.day = day

    def __str__(self):
        return f"{self.hour}:{self.minutes}:{self.seconds}{', Day ' + str(self.day) if self.day else ''} (GMT+{self.utc})"

    def __add__(self, b):
        if not isinstance(b, TimeStamp):
            hour = self.hour + b
            return TimeStamp(hour % 24, self.minutes, self.seconds, self.utc, day=self.day + hour // 24)
        a, b = self.gmt0(), b.gmt0()
        seconds = (a.seconds + b.seconds) % 60
        minutes = (a.minutes + b.minutes + seconds // 60)
        hour = (a.hour + b.hour + minutes // 60)
        return TimeStamp(hour % 24, minutes % 60, seconds, day=hour//24)
    
    def __sub__(self, b):
        if not isinstance(b, TimeStamp):
            hour = self.hour + b
            return TimeStamp(self.hour - b, self.minutes, self.seconds, self.utc, day=self.day + hour // 24)
        a, b = self.gmt0() , b.gmt0()
        seconds = (a.seconds - b.seconds) % 60
        minutes = (a.minutes - b.minutes + seconds // 60)
        hour = (a.hour - b.hour + minutes // 60)
        return TimeStamp(hour % 24, minutes % 60, seconds, day=hour//24)
    
    def convertUTC(self, newUTC):
        out = self.gmt0() + newUTC
        out.utc = newUTC
        return out
    
    def gmt0(self):
        ts = self - self.utc
        ts.utc = 0
        return ts
```

| From | To | Departure | Arrival | Duration
| - | - |  - | - | - |
**CASABLANCA** MOHAMMED V |  **NEW YORK** JOHN F KENNEDY | 15:55, 16 Aug 2024 | 18:45, 16 Aug 2024 | 7:50
 **NEW YORK** JOHN F KENNEDY |  **BOSTON** EDWARD L LOGAN | 21:20, 16 Aug 2024 | 22:43, 16 Aug 2024 | 01:23

## Obtain the durations

> Casablanca - NYC

```python
casablanca = TimeStamp(15,55, utc=1)
new_york = TimeStamp(18,45, utc=-4)
print(new_york - casablanca)
# output : 7:50:0 (GMT+0)
```

> NYC - BOS
```python
new_york = TimeStamp(21,20, utc=-4)
boston = TimeStamp(22,43, utc=-4)
print(boston - new_york)
```


## Get total travel time

> Including transit time

```python
casablanca = TimeStamp(15,55, utc=1)
boston = TimeStamp(22,43, utc=-4)
print(boston - casablanca)
# output: 11:48:0, Day -1 (GMT+0)
```

## Get transit time

```python
new_york_arrival = TimeStamp(18,45, utc=-4)
new_york_take_off = TimeStamp(21,20, utc=-4)
print(new_york_take_off - new_york_arrival)
# output : 2:35:0, Day -1 (GMT+0)
```

## Bonus

As it may be hard to see the time it takes across timezones, here is a little script to get arrival time in GMT+1.

> Arrival at New York
```python
new_york = TimeStamp(18,45, utc=-4)
print(new_york.convertUTC(1))
# output : 23:45:0 (GMT+1)
```

> Arrival at Boston
```python
boston = TimeStamp(22,43, utc=-4)
print(boston.convertUTC(1))
# output : 3:43:0, Day 1 (GMT+1)
```
