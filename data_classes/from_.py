from dataclasses import dataclass,field

@dataclass
class From:
    from_str: str = ''
    from_name: str = ''
    from_mail: str = ''
    def __post_init__(self):
        self.split_from()
    def split_from(self):
        try:
            self.from_str=str(self.from_str).replace("","")
        except Exception as e:
            print("1",e)
        try:
            fr_name = self.from_str.split("<")[0].replace("\n","")
            self.from_name = fr_name.strip()
        except Exception as e:
            print("2",e)
        try:
            if "<" in self.from_str:
                fr_mail  = self.from_str.split("<")[1].replace(">","").replace("\n","")
                self.from_mail = fr_mail.strip()
        except Exception as e:
            print("3",e)
