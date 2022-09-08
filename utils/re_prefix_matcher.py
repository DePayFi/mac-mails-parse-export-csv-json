import re
from outputs.config.config import prefix_patterns,ignore_line_patterns

class PrefixMatcher:
    patterns = None
    ignore_patterns = None
    last_match = None

    def __init__(self):
        self.patterns = prefix_patterns
        self.ignore_patterns = ignore_line_patterns
    
    def get_line_type(self,txt_line):
        # * * * * * * * * * * * * * * * * # 
        assert type(self.patterns) == dict
        assert type(txt_line) == str
        # * * * * * * * * * * * * * * * * #

        result_dict = {"line_type": None,"last_match":self.last_match}
        prev_match = self.last_match

        for ignore_patt in self.ignore_patterns:
            if re.search(ignore_patt,txt_line,flags=re.IGNORECASE):
                result_dict['line_type'] = "ignore"
                result_dict['last_match'] = prev_match
                return result_dict

        for prefix in self.patterns.keys():
            pattern = r'(' + self.patterns[prefix] + r')'
            if prefix.startswith("from") and prefix.endswith(("1","2","3")):
                    prefix = "from_"
            elif prefix.startswith("date") and prefix.endswith(("1","2","3")):
                    prefix = "date"
            if re.search(pattern,txt_line,flags=re.IGNORECASE):
                self.last_match = prefix
                
                result_dict['line_type'] = prefix
                result_dict['last_match'] = prev_match
                

                return result_dict

            
        self.last_match = None
        return result_dict