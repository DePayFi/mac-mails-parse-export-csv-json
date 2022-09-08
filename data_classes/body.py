from typing import List
from dataclasses import dataclass,field

@dataclass
class Body:
    body_lines : List[str] = field(default_factory=list)
    recording: bool = False
    last_line: str = ""
    blacklist: List[str] = field(default_factory=list)
    replace: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        self.body_lines = []
        self.blacklist = ["subject:","from:","to:"]
        self.replace = [["\n",""]]

    def clean_line(self,body_line):
        for b in self.blacklist:
            if body_line.startswith(b):
                return ""
        for r in self.replace:
            body_line = body_line.replace(r[0],r[1])

        return body_line.strip()

    def add_to_body(self,body_line):
        line_tmp = None
        
        if body_line.startswith("from:"):
            try:
                self.recording = False
            except Exception as e:
                print(e)
        
        elif self.recording == True:
            line_tmp = self.clean_line(body_line)
            self.last_line = body_line
            try:
                self.body_lines.append(line_tmp)
            except Exception as e:
                print(e)
