from dataclasses import dataclass,field
from data_classes.body import Body
from data_classes.dates import Dates
from data_classes.from_ import From
import traceback
import re

@dataclass
class Mail:
    body: Body

    is_emlx: bool = False

    body_emlx: str = ''

    from_: str = ''
    from_name: str = ''
    from_mail: str = ''
    
    subject: str = ''

    date: str = ''
    date_iso: str = ''
    date_utc: int = 0
    
    to: str = ''
    to_name: str = ''
    to_mail: str = ''
    
    reply_to: str = ''
    reply_to_name: str = ''
    reply_to_mail: str = ''
    
    reply_to = ''
    
    xuid: str = ''
    message_id: str = ''
    mime_version: str = ''
    content_type: str = ''
    
    field_count: int = 0
    
    

    def count_pp(self):
        self.field_count = self.field_count + 1
        return 
    def __init__(self,is_emlx):
        self.is_emlx = is_emlx
        self.body = Body()
        pass
    def add(self,attr_name,to_add):
        try:
            match(attr_name):
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: ignore
                case 'ignore':
                    pass
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: body
                case 'body':
                    try:
                        self.body.add_to_body(to_add)
                    except Exception as e:
                        print(e)
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: from_        
                case 'from_':
                    if self.is_emlx == True:
                        self.__setattr__('from_',to_add)
                        self.count_pp()
                    else:
                        try:
                            to_add = re.match('^from:.?(.*)$',to_add,flags=re.IGNORECASE)
                            try:
                                to_add = to_add.group(1)
                            except Exception as e:
                                print(e)
                            pass
                            self.__setattr__(attr_name,to_add)
                            self.count_pp()
                        except Exception as e:
                            print("2 - error setting attributes from_mail,from_name:",e,traceback.format_exc())
                    try:
                        from_tmp = From(from_str=str(to_add))
                    except Exception as e:
                        print(e)
                    try:
                        self.__setattr__('from_name',from_tmp.from_name)
                    except Exception as e:
                        print(e)
                    try:
                        if len(from_tmp.from_mail) == 0 and '@' in self.from_name:
                            self.__setattr__('from_mail',from_tmp.from_name)
                            self.__setattr__('from_name',self.from_name.split("@")[0])    
                        else:
                            self.__setattr__('from_mail',from_tmp.from_mail)
                    except Exception as e:
                        print("1 - error setting attributes from_mail,from_name:",e,traceback.format_exc())
                
                        
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: date
                case 'date':
                    try:
                        date_tmp = Dates(dt_str=to_add)
                    except Exception as e:
                        print("error setting date_tmp = Dates:",e,traceback.format_exc())
                    try:    
                        self.__setattr__(attr_name,date_tmp.dt_str)
                        self.count_pp()
                        self.__setattr__('date_iso',date_tmp.date_iso)
                        self.count_pp()
                        self.__setattr__('date_utc',date_tmp.date_utc)
                        self.count_pp()

                    except Exception as e:
                            print("Exception (date_iso):",e)
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: to
                case 'to':
                    try:
                        #to_add = str(to_add).replace("To:","").replace("to:","").strip()
                        to_add = re.sub(r'to:\s?','',to_add,flags=re.IGNORECASE)
                        self.__setattr__(attr_name,to_add)
                        self.count_pp()
                        to_list_tmp = []
                        to_name_list_tmp = [""]
                        to_mail_list_tmp = [""]
                        t_split = None
                        
                        try:
                            if "," in to_add:
                                to_name_list_tmp = []
                                to_mail_list_tmp = []
                                to_list_tmp = to_add.split(",")
                                for idx,t in enumerate(to_list_tmp):
                                    try:
                                        #to_list_tmp[idx] = t.strip()
                                        t = t.strip()
                                        t_split = t.split("<")
                                        pass
                                    except Exception as e:
                                        print("error in for loop - enumerate to_list_tmp:",e,traceback.format_exc())
                                        pass
                                    if len(t_split) > 0:
                                        to_name_list_tmp.append(t_split[0].strip())
                                        to_mail_list_tmp.append(t_split[1].replace(">","").strip())
                                if len(to_name_list_tmp) > 0:
                                    to_name_list_tmp = ",".join(to_name_list_tmp)
                                    self.__setattr__('to_name',to_name_list_tmp)
                                if len(to_mail_list_tmp) > 0:
                                    to_mail_list_tmp = ",".join(to_mail_list_tmp)
                                self.__setattr__('to_mail',to_mail_list_tmp)
                            elif '<' in to_add:
                                t = to_add.strip()
                                t_split = t.split("<")
                                self.__setattr__('to_name',t_split[0].strip())
                                self.__setattr__('to_mail',t_split[1].replace(">","").strip())
                                pass
                        except Exception as e:
                            print(e)            
                            
                            
                    except Exception as e:
                        print("error in case 'to':",e,traceback.format_exc())
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: subject    
                case 'subject':
                    try:
                        to_add = str(to_add).replace("Subject:","").replace("subject:","").strip()
                        self.__setattr__(attr_name,to_add)
                        self.count_pp()
                    except Exception as e:
                        print("error in case 'subject':",e,traceback.format_exc())
                #   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .   .CASE: reply-tp
                case 'reply-to':
                    try:
                        to_add = str(to_add).replace("Reply-To:","").replace("reply-to:","").strip()
                        self.__setattr__(attr_name,to_add)
                        self.count_pp()
                    except Exception as e:
                        print("error in case 'reply-to':",e,traceback.format_exc())
                case 'body':
                    try:
                        Body.add_to_body(self.body,to_add)
                        pass
                    except Exception as e:
                        print("error adding body (case 'body') in Mail.py",e)
                case 'body_emlx' | 'content_type' | 'xuid' | 'mime_version':
                    try:
                        self.__setattr__(attr_name,to_add)
                        pass
                    except Exception as e:
                        print(e)
                
                
        except Exception as e:
            print(e)