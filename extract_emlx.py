import traceback
import os
import emlx
import glob

from config.config import ConfigSettings

from data_classes.mailbox import Mailbox
from data_classes.mail import Mail

from utils.create_outputs import create_outputs
import utils.string_utils as string_utils
from utils.mail_tuples import mails_to_tuples
from utils.tuples_to_df import tuples_to_df


emlx_config= ConfigSettings(mode="emlx")

mail_dir = "/".join(os.getcwd().split("/")[:3])+'/'+ emlx_config.mail_root_dir

search_mailbox = "/".join([mail_dir,emlx_config.mail_account_folder,emlx_config.target_folder])
script_loc = os.getcwd()
os.chdir(search_mailbox)

files = glob.glob(pathname=os.getcwd()+"/**/*.emlx",recursive = True)
  
columns = ["date_utc","date_iso","date","from","from_name","from_mail","subject","to","to_name","to_mail","from","reply_to","reply_to_name","reply_to_mail","body","x-universally-unique-identifier","message-id","mime-version","content-type"]

for idx,file in enumerate(files):

    if str(file).endswith(".eml") or "Attachment" in file:
        break
    message = emlx.read(file)
    alt_dates = [None,None]
    mail_header_keys = message.headers.keys()
    tmp_dict = dict()
    

    for key in mail_header_keys:
        tmp_dict[key.lower()] = message[key]

    current_mail = Mail(is_emlx=True)
    Mail.add(current_mail,"from_",tmp_dict["from"])


    try:
        Mail.add(current_mail,"date",tmp_dict["date"])
    except Exception as e:
        print("Date parsing error:",e,traceback.format_exc())

    try:
        Mail.add(current_mail,"to",tmp_dict["to"])
        Mail.add(current_mail,"to_name",string_utils.clean(tmp_dict["to"],"to_name"))
        Mail.add(current_mail,"to_mail",string_utils.clean(tmp_dict["to"],"to_mail"))

    except Exception:
        print("error adding to_name or to_mail:",e,traceback.format_exc())

    tmp_dict["body"] = message.text

    try:
        Mail.add(current_mail,'body_emlx',tmp_dict["body"])

    except Exception as e:
        print("error adding body",e)
    try:
        Mail.add(current_mail,"subject",tmp_dict["subject"])
    except Exception as e:
        print("error adding subject",e)
    try:
        Mail.add(current_mail,"content_type",tmp_dict["content-type"]) ######content
    except Exception as e:
        print("error adding content_type",e)
    try:
        Mail.add(current_mail,"mime_version",tmp_dict["mime-version"])
    except Exception as e:
        print("error adding mime_version",e)
    try:
        Mail.add(current_mail,"xuid",tmp_dict["x-universally-unique-identifier"])
    except Exception as e:
        print("error adding xuid",e)
    try:
        Mail.add(current_mail,"message_id",tmp_dict["message-id"])
    except Exception as e:
        print("error adding message_id",e)
    try:
        Mail.add(current_mail,"reply-to",tmp_dict["reply-to"])
    except Exception as e:
        print("error adding xuid",e)


    if idx == 0:  #.    .   .   .   .   .   .   .   .   .  🔸if🔸 Mailbox: not existing, second "from_"
        mb = Mailbox([current_mail]) #.    .   .   .  create Mailbox initially
        pass
    else:
        mb.Mails.append(current_mail)

      

columns = emlx_config.output_columns


tup = mails_to_tuples(mb,is_emlx=True)

df = tuples_to_df(columns, tup)

create_outputs(emlx_config, df,mode=emlx_config.mode, script_loc=script_loc)