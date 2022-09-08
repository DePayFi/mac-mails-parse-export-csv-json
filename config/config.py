# general output folder
output_folder ="" # outputs/

# emlx file parsing
mail_root_dir = "" # Library/Mail/V9/
mailbox_folder = "" # 12xxxxx4-CxxC-4xx3-8xxD-9xxxxxxxx1
target_folder = "" # Sent Items.mbox


remove_signature = True # to be further implemented
signature_starts = "" # to be further implemented



prefix_patterns = {"from_"      : '\x0cfrom:',
                    "from_1"     : 'from:',
                    "from_2"     : ' from:',
                    "from_3"     : 'from:',
                    "subject"   : 'subject:',
                    "date_1"      : 'date:',
                    "date_2"      : 'sent:.*(?!iphone)',
                    "date_3"      : 'sent:',
                    "to"        : 'to:',
                    "reply-to"  : 'reply_to'
                    }
ignore_line_patterns = ['^\xa0\n','^\n(?!from)']



#Custom Columns from RegEx extraction outputs (in progress)
match_re_list = [
                ['welcome:.([A-Za-z0-9\.-]+).[&+].*',2],
                ['.*to.([A-Za-z0-9\.-]+)\?.*',2],
                ['([a-zA-Z0-9\.-]+).[\+x].web3.*',2],
                ]
re_list_bounces = [
                ['.*error occurred while trying to deliver the mail to the following recipients: ([a-zA-Z0-9_\.\-@,]+) .*',2],
                [".*message wasn't delivered to ([a-zA-Z0-9_\.\-@,]+) because.*",2],
                ['.*following address(es) failed:[ ]+([a-zA-Z0-9_\.\-@,]+) .*',2],
                ['.*[(]generated from ([a-zA-Z0-9_\.\-@,]+))[)].*'],
                ['.*message was created automatically by mail delivery software.*for[ ]+([a-zA-Z0-9_\.\-@,]+);.*',2]
                ]

