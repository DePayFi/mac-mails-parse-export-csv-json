# Mac OS Mail - Email Extractor 
## Mail App Emails to CSV or JSON

**What it (currently) does:**

Email Export from Apple's Mail App on Mac OS -> Plaintext input -> Parse/Extract -> Save to CSV or JSON

*Sometimes it can be handy to get structured data from a mailbox on Mac OS (Mail). This is a quick (still) hacky script which parses a plaintext export email export from the Mail app in Mac OS and returns a structured CSV.*

## Features
- Mode: Parse manually exported emails from a txt
- Mode: Parse emlx files created by the Mail app
- Different output formats: Saves a sorted (by utc-timestamp) output together with an exploded output based on Email addresses
- (in progress): custom column outputs based on regular expression matching of defined columns

## Input (text file mode)
1. Select the emails you want to parse in Mac OS Mail (hold shift in order to select multiple, CMD + A in order to select all from the current mailbox)
2. File > Save As > Select Format: Plain Text > Save to the script directory & rename to "input.txt"

## Input (emlx parser mode)
Edit the config.py file with your Mac OS filepath to your Mailbox that you want to extract email data from

## Run
> Tested with Python 3.10.6

```
pip install -r requirements.txt
```
1. edit config.py
2. run either in **txt file mode:**


```
rename your txt file input.txt, place in script dir, then execute:
python3 extract_txt.py
```

or 
3. run in emlx parser mode:

```
don't forget to edit config.py first, then execute:
python3 extract_txt.py
```

if you want to use a CLI with args 
(implementation in progress)

```
python3 mac-os-extract-mails.py

[Options]
-e : run emlx parser
-t : run txt file parser
-c : open config file for editing
-sinput: select input file for txt file parser
-sodir: select folder for outputs
```

## Output Columns

```

- date-isodate
- from
- from_name
- from_mail
- subject
- to
- to_name
- to_mail
- reply_to
- reply_to_name
- reply_to_mail
- content_type
- message_id
- mime_version
- xuid
- body

```

## Todo

- [x] Plaintext mode
- [x] Emlx mode
- [x] Explode outputs: Split multiple recipient email addresses into separate data rows (1 email = 1..* rows). Currently: 1 row = 1 email, recipient email addresses are comma-separated
- [ ] Custom columns from RegEx outputs
- [ ] Refactor code
- [ ] Export json option
- [ ] Command line tool
- [ ] Add "re_in_subject" column
