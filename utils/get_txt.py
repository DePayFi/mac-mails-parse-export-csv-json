from xml.dom import INDEX_SIZE_ERR
from data_classes.mailbox import Mailbox
from string import printable
import re


def get_txt(fname):
    with open(fname,"r",encoding='utf-8') as input_file:
      Lines = input_file.readlines()
      split_mails = [[""]]
      mails = Mailbox()
      list_list = []
      mails_count = 0
      for idx,line in enumerate(Lines):
          line = line.splitlines()                           
          list_list.extend(line)
    
    last_idx = 0
    multi_list = []
    tmp_list = []

    for idx,l in enumerate(list_list):
        
        l = re.sub("[^{}]".format(printable), "", l)
        if l == ('' or ' ' or ''):
            continue

        l = re.sub(re.escape("=?UTF-8?Q?"),"",l)
        l = re.sub(re.escape("?="),"",l)
        
        if l.lower().startswith("from:") and idx > 1:
            multi_list.append(tmp_list)
            tmp_list = []
            tmp_list.append(l)
        else:
            tmp_list.append(l)
 
    mb = None
    return multi_list,mb
