from dataclasses import dataclass,field
from data_classes.mail import Mail
from typing import List

@dataclass
class Mailbox:
    Mails: List[Mail] = field(default_factory=list)