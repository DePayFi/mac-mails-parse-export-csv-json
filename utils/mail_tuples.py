def mails_to_tuples(mb,is_emlx):
    if is_emlx:
        pass
    tup = []
    try:
        for idx,m in enumerate(mb.Mails.__iter__()):
            if not is_emlx:
                bl = "\n".join(m.body.body_lines)
            else:
                bl = m.body_emlx
            try:
                tmp_t = (m.date_utc,m.date_iso,m.date,m.from_,m.from_name,m.from_mail,m.subject,m.to,m.to_name,m.to_mail,m.reply_to,m.reply_to_name,m.reply_to_mail,m.content_type,m.message_id,m.mime_version,m.xuid,bl)
            except Exception as e:
                print("error creating mail tuples (tmp_t)",e)
            tup.append(tmp_t)
            if idx ==100000000000000000:
                break
    except Exception as e:
        print("error in for loop - enumerate mb.Mails:",e,traceback.format_exc())
    return tup