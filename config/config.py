from dataclasses import dataclass,field
from typing import Dict, List

@dataclass
class ConfigSettings:
    
    output_folder : str = "outputs" # outputs/
    mail_root_dir : str = "Library/Mail/V9" # Check 'Library/Mail/V9/' first, might differ for each Mac version
    mail_account_folder : str = "" # Edit: Folder name string, scheme: 12xxxxx4-CxxC-4xx3-8xxD-9xxxxxxxx1
    target_folder : str = "Inbox.mbox" # Edit: E.g. 'Sent Items.mbox'
    
    output_columns : List[str] = field(default_factory=list)
    prefix_patterns : Dict[str,str] = field(default_factory=dict)
    ignore_line_patterns : List[str] = field(default_factory=list)
    all_custom_cols : List[str] = field(default_factory=list)
    
    remove_signature : bool = True # to be further implemented
    signature_starts : str = "" # to be further implemented
    
    mode : str = ""

    def __init__(self,mode):
        self.mode = mode
        self.output_columns =  [
                                "date_utc",
                                "date-iso",
                                "date",
                                "from",
                                "from_name",
                                "from_mail",
                                "subject",
                                "to",
                                "to_name",
                                "to_mail",
                                "reply_to",
                                "reply_to_name",
                                "reply_to_mail",
                                "content_type",
                                "message_id",
                                "mime_version",
                                "xuid",
                                "body"
                                ]
        self.prefix_patterns = {    "from_"     : '\x0cfrom:',
                                    "from_1"    : 'from:',
                                    "from_2"    : ' from:',
                                    "from_3"    : 'from:',
                                    "subject"   : 'subject:',
                                    "date_1"    : 'date:',
                                    "date_2"    : 'sent:.*(?!iphone)',
                                    "date_3"    : 'sent:',
                                    "to"        : 'to:',
                                    "reply-to"  : 'reply_to'
                                }
        self.ignore_line_patterns = ['^\xa0\n','^\n(?!from)']
        self.all_custom_cols = []
        self.all_custom_cols.append(
                {
                    'create_col' : "hi-sayers",
                    'source_col': "body",
                    'na_values': "", # don't change if you want non-matching values to reflect in blank cells
                    'regex_lst': 
                        [
                                '(hi [a-zA-Z0-9]+)',
                                '(hey.[a-zA-Z0-9]+)'
                        ]
                }
        )
        self.all_custom_cols.append(
                {
                    'create_col' : "yes-sayers",
                    'source_col': "body",
                    'na_values': "", # don't change if you want non-matching values to reflect in blank cells
                    'regex_lst': 
                        [
                                '(yes...)',
                                '(sure.{10})',
                                '(am.interested.{5})'
                                
                        ]
                }
        )
        pass
    

