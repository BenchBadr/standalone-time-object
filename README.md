# Standalone and easy Python time Object

![image](https://wallpapercave.com/wp/wp4491645.png)

Yeah I know, `time` module does that pretty decently but I got bored. This allows you to addition, substract, convert timezone. ates aren't supported so days are relative to each others (+1, +2, -1...) like when talking about yesterday, tomorrow...

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
