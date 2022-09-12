from curses import raw
from dataclasses import dataclass,field
from typing import List
import pandas as pd
import re

@dataclass
class CustomColumn: 
    create_col: str = 'custom_col'
    source_col: str = ''
    regex_lst: List[re.Pattern] = field(default_factory=list)
    matched_lst : List[str] = field(default_factory=list)
    na_values : str = ''
    
    def __init__(self,settings):
        self.create_col = settings["create_col"]
        self.source_col = settings["source_col"]
        self.regex_lst = settings["regex_lst"]
        self.na_values = settings["na_values"]
        self.matched_lst = []
        return
        
    def get_matches(self,df_original):
        source_column_df = df_original[self.source_col].str.lower()
        pass
        for val in source_column_df:
            matched = self.na_values 
            
            for idx,re_item in enumerate(self.regex_lst):
                
                if str(val) == "nan":
                        self.matched_lst.append(matched)
                        break
                try:
                    pt = r'^(([Rr]e:.)?.*' + re_item + r'.*)$'
                    re_comp = re.compile(pt,flags=re.I | re.U | re.MULTILINE)
                    
                   
                    matched = re_comp.search(val)
                    matched = list(matched.groups()[-1:])[0]
                    self.matched_lst.append(matched)
                    break
                    
                except Exception as e:
                    print("re.search failed with Exception:",e,"\nfield: ",val)
                    if idx == len(self.regex_lst)-1:
                        self.matched_lst.append(self.na_values)
                        break
                    continue
                    

        return self.matched_lst
