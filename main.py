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
            hour = self.hour - b
            return TimeStamp(hour % 24, self.minutes, self.seconds, self.utc, day=self.day + hour // 24)
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
