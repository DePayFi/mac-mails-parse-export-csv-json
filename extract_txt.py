import traceback

from mailbox import Mailbox

from data_classes.mail import Mail
from data_classes.mailbox import Mailbox
from data_classes.body import Body

from utils.create_outputs import create_outputs
from utils.get_txt import get_txt
from utils.re_prefix_matcher import PrefixMatcher
from utils.mail_tuples import mails_to_tuples
from utils.tuples_to_df import tuples_to_df
from config.config import ConfigSettings
import os

split_mails, mb = get_txt("input.txt")
txt_config = ConfigSettings(mode='txt')
script_loc = os.getcwd()
pm = PrefixMatcher(txt_config)
current_mail = Mail(is_emlx=False)

try:
    for idx,mail_original in enumerate(split_mails):
        
        for l_idx,ln_original in enumerate(mail_original):
            ln_type = pm.get_line_type(ln_original)
            pass

            match(ln_type["line_type"]):
                case "ignore":
                    continue
                
                
                case None:#.    .   .   .    .    .   .   .    . CASE None ==> Body
                    Body.add_to_body(current_mail.body,ln_original)
                
                
                case 'from_': #.    .   .   .    .    .   .   .    . CASE from_
                    ####
                    if  (isinstance(mb,Mailbox) == False) and current_mail.field_count >1:  #.    .   .   .   .   .   .   .   .   .  🔸if🔸 Mailbox: not existing, second "from_"
                        mb = Mailbox([current_mail]) #.    .   .   .  create Mailbox initially
                        current_mail = Mail(is_emlx=False)
                        Mail.add(current_mail,'from_',ln_original)

                        
                        
                    elif isinstance(mb,Mailbox):
                        mb.Mails.append(current_mail)
                        current_mail = Mail(is_emlx=False)
                        Mail.add(current_mail,'from_',ln_original)
                        
                    else:
                        Mail.add(current_mail,'from_',ln_original)
                        pass

                #--#
                case "date": #.    .   .   .    .    .   .   .    . CASE date
                    try:
                        Mail.add(current_mail,attr_name='date',to_add=ln_original)
                    except Exception as e:
                        print("error setting 'date':",e,traceback.format_exc())
                
                #--#
                case "to":#.    .   .   .    .    .   .   .    . CASE to
                    try:
                        Mail.add(current_mail,attr_name='to',to_add=ln_original)
                        current_mail.body.recording = True
                    except Exception as e:
                        print("error setting 'to':",e,traceback.format_exc())
                    
                #--#
                case "subject":#.    .   .   .    .    .   .   .    . CASE subject
                    try:
                        Mail.add(current_mail,attr_name='subject',to_add=ln_original)
                    except Exception as e:
                        print("error setting 'subject':",e,traceback.format_exc())

                
                #--#
                case "reply_to":#.    .   .   .    .    .   .   .    . CASE reply_to
                    try:
                        Mail.add(current_mail,attr_name='reply_to',to_add=ln_original)
                        current_mail.body.recording = True
                    except Exception as e:
                        print("error setting date:",e,traceback.format_exc())
        ln_type = None
        pass

except Exception as e:
    print("error in for loop enumerate(split_mails)",e,traceback.format_exc())
   
columns = ['date_utc','date_iso','date','from','from_name','from_mail','subject','to','to_name','to_mail','reply_to','reply_to_name','reply_to_mail','body']


tup = mails_to_tuples(mb,False)

df = tuples_to_df(txt_config.output_columns, tup)

create_outputs(txt_config, df,mode=txt_config.mode,script_loc=script_loc)