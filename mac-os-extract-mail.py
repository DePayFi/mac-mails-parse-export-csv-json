import re
import csv
import time
import datetime
from dateutil.parser import parse
import calendar

tmp_body = []
tmp_reply_to = ""
record_body = False
#error_parser = []


def parse_dates(date_str,mail):
  #example date_str = "12 August 2022 at 10:29:55 CEST"
  #can be further extended: https://www.timeanddate.com/time/zones/

  if date_str.endswith("CEST"):
    date_str = date_str.replace("CEST","UTC+2")
  
  try:
    date_tmp = parse(date_str)

  except Exception as e:
    date_tmp = ""
    print("Error parsing date. Error:",e,date_str)
  try:
    date_iso = date_tmp.isoformat()
  except Exception as e:
    date_iso = ""
    print("Error setting date_iso Error:",e,"\nMail:",mail)
  try:
    date_utc = calendar.timegm(date_tmp.utctimetuple())
  except Exception as e:
    date_utc = ""
    print("Error setting date_utc. original date string was"+date_str+str(e))

  return [date_iso,date_utc]


def clean_str(field,field_type):
    if field == '':
      return field
          
    if field_type == "from":
      try:
        field = field.replace("From: ","").replace("\n","").replace("\x0c","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)    
      return field

    if field_type == "from_mail":
      try:
        field = field.replace("From: ","").split("<")[1].replace(">","").replace("\n","").replace("\x0c","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)  
      return field

    if field_type == "from_name":
      try:
        field = field.replace("From: ","").split(" <")[0].replace("  ","").replace("\n","").replace("\x0c","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)    
      return field

    if field_type == "subject":
      try:
        field = field.replace("Subject: ","").replace("\n","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)
      return field

    if field_type == "date":
      try:
        field = field.replace("Date: ","").replace("Sent: ","").replace("\n","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)
      return field

    if field_type == "to":
      try:
        field = field.replace("To: ","").replace("\n","").replace("\x0c","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)    
      return field

    if field_type == "to_name":
      try:
        field = field.split("<")[0].strip().replace("\n","").replace("\x0c","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)
      return field      

    if field_type == "to_mail":
      try:
        field = field.split("<")[1].strip().replace(">","").replace("\n","").replace("\x0c","")
      except Exception as e:
        field = field.replace("To: ","").replace("\n","")
      return field              


with open("input.txt") as input_file:
  Lines = input_file.readlines()
  mails = []
  mail_count = 0
  for idx,line in enumerate(Lines):
    if line.strip().startswith("From: "):
      if idx > 0:
        mail_count+=1
        
        try:
          mails.append([tmp_date,tmp_from,tmp_subject,tmp_to,tmp_reply_to,tmp_body])
        except Exception as e:
          print(e)
        
        tmp_from = ""
        tmp_subject = ""
        tmp_date = ""
        tmp_to = ""
        tmp_body = []
        record_body = False
        tmp_reply_to = ""
        
        mail_count+=1

      tmp_from = line
    elif "Subject: " in line:
      tmp_subject = line
    elif ("Date: " or "Sent: ") in line:
      tmp_date = line
    elif line.startswith("To: "):
      tmp_to = line
      if "Reply-To" not in line:
        record_body = True
        
    elif line.startswith("Reply-To:"):
      tmp_reply_to = line
    elif record_body == True:
      line = line.replace("     ","").replace("  ","").replace("\n","")
      if (len(line)>2) and "Reply-To" not in line:
        tmp_body.append(line)
        #print(tmp_body)

  
  mail_count = int(mail_count/2)
  output = []
  for mail in mails:
    
    mail_vals=dict()
    
    mail_vals["from"] = clean_str(mail[1],"from")
    mail_vals["from_name"] = clean_str(mail_vals["from"],"from_name")
    mail_vals["from_mail"] = clean_str(mail_vals["from"],"from_mail")

    mail_vals["subject"] = clean_str(mail[2],"subject")

    mail_vals["date"] = clean_str(mail[0],"date")
    
    alt_dates = parse_dates(mail_vals["date"],mail)
    mail_vals["date_iso"] = alt_dates[0]
    mail_vals["date_utc"] = alt_dates[1]
    
    mail_vals["to"] = clean_str(mail[3],"to")
    mail_vals["to_name"] = clean_str(mail_vals["to"],"to_name")
    mail_vals["to_mail"] = clean_str(mail_vals["to"],"to_mail")

    mail_vals["reply_to"] = clean_str(mail[4],"to")
    mail_vals["reply_to_name"] = clean_str(mail_vals["reply_to"],"to_name")
    mail_vals["reply_to_mail"] = clean_str(mail_vals["reply_to"],"to_mail")

    mail_vals["body"] = " ".join(mail[5])
    #print("\n\n\nBody: ",mail_vals["body"])

    output.append(mail_vals)

    
  print("Mails parsed:",mail_count)
  
  columns = ['date_utc','date_iso','date','from','from_name','from_mail','subject','to','to_name','to_mail','reply_to','reply_to_name','reply_to_mail','body']

  try:
    with open("output.csv", 'w',newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=columns)
        writer.writeheader()
        for key in output:
            writer.writerow(key)
  except IOError:
    print("error writing file")
  