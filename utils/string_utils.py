def clean(field,field_type):
    if field == '':
        return field

    if field_type.startswith("from"):
      try:
        field = field.replace("\x0c","").replace("=?","").replace("\n","").replace("From: ","").replace("\x0c","").replace("\x0c","")
      except Exception as e:
        return field
      return field


    if field_type == "from_mail":
      try:
        if "from" in field.lower():
              field = field.replace("From: ","")
        field = field.split("<")[1].replace(">","").replace("\n","")
      except Exception as e:
        print("\n⚠️Error -",field_type,"-",e)  
      return field

    if field_type == "from_name":
      try:
        field = field.replace("From: ","").split(" <")[0].replace("  ","").replace("\n","")
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