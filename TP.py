import re
from collections import Counter

logfile = "access.log"

logreg = r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - - \[(.+).{5}] \"[^\"]+\" (\d{3}) \d+ .{4}\"(?P<userid>.+)\/\d"
with open(logfile) as f:
    fread = f.read()
    ip_list = re.findall(logreg, fread)
    for k, v in Counter(ip_list).items():
        print(k, v)

import json

data = {
    "ip address": ip_list
}
#
with open("file.json", "w") as json_file_pointer:
    json.dump(data, json_file_pointer)
