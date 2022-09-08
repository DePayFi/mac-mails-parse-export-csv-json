from dataclasses import dataclass,field
from dateutil.parser import parse
from datetime import *
import calendar
from curses.ascii import isdigit
import re


@dataclass
class Dates:
    dt_str: str = ''
    date_iso: str = ''
    date_utc: int = 0
    alt_time_formats = ['%A, %d %B %Y %H:%M %p',
                    '%d %B %Y at %H:%M:%S %z',
                    '%a, %d %b %Y %H:%M:%S %z',
                    '%A, %d %B %Y %H:%M %p'
                    ]
    
    def __post_init__(self):
        self.decode_dt()

    def decode_dt(self):
        try:
            self.dt_str = self.dt_str.replace("Date: ","").strip()
            self.dt_str = self.dt_str.replace("Sent: ","").strip()
            self.dt_str = self.dt_str.replace("Last-Attempt-","").strip()
            self.dt_str = self.dt_str.replace("Arrival-","")
            
            
            self.dt_str = re.sub("date:\s|sent:\s","",self.dt_str,flags=re.IGNORECASE)
            self.dt_str = re.sub("arrival-","",self.dt_str)
        except Exception as e:
            print(e)        

        tmp_dates = []
        if "CEST" in self.dt_str:
            tmp_dates.append(self.dt_str.replace("CEST","UTC+2"))
        elif "PDT" in self.dt_str:
            tmp_dates.append(self.dt_str.replace("(PDT)",""))
        else:
            tmp_dates.append(self.dt_str)
        
        if isdigit(self.dt_str[0]): 
            tmp_dates.append("0"+self.dt_str.replace("CEST","UTC+2"))
        
        tmp_dates = list(set(tmp_dates))
        found_date = None

        for dt in tmp_dates:
            try:
                found_date = parse(dt)
                break

            except Exception as e:
                print(e)
        if not found_date:
            for tmp_date in tmp_dates:

                for format_str in self.alt_time_formats:
                    try:
                        found_date = datetime.strptime(tmp_date, format_str)
                        #print("found date:",found_date)
                        break
                    except Exception as e:
                        print(e)
                        continue
        try:
            self.date_iso = found_date.isoformat()
            #print("found iso date:",self.date_iso)
        except Exception as e:
            print(e)
        try:
            self.date_utc = calendar.timegm(found_date.utctimetuple())
            #print("found utc date:",self.date_utc)
        except Exception as e:
            print(e)