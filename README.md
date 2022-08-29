# Mac OS Email data extractor (Plaintext to CSV)

Sometimes it can be handy to get structured data from a mailbox on Mac OS (Mail).

This is a quick hacky script which parses a plaintext export email export from the Mail app in Mac OS and returns a structured CSV


## Input
1. Select the emails you want to parse in Mac OS Mail (hold shift in order to select multiple, CMD + A in order to select all from the current mailbox)
2. File > Save As > Select Format: Plain Text > Save to the script direction & rename to "input.txt"

## Run
Tested with Python 3.10.6
> pip install -r requirements.txt
> python3 mac-os-extract-mails.py

## Output
> columns = ['date_utc','date_iso','date','from','from_name','from_mail','subject','to','to_name','to_mail','reply_to','reply_to_name','reply_to_mail','body']

## Todo

- [ ] Improve date parsing (minor bugs)
- [ ] Export json option
- [ ] Improve reliability for recurring use
    - Command line tool
    - Try .emxl file parsing approach which might be more reliable (see emlx_test.py)
