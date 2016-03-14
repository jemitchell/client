#!/usr/bin/env python
from pprint import pprint
import json
import requests

issue = {}
for (attribute, length) in \
                [
                ("P",4),
                ("N",4),
                ("title",20),
                ("assignee",10),
                ("milestone",10),
                ("labels",20)
                ]:
    issue[attribute] = attribute
print("| {P:4} | {N:4} | {title:20} | {assignee:10} | {milestone:10} | {labels:20} |".format(**issue))

for (attribute, length) in \
                [
                ("P",4),
                ("N",4),
                ("title",20),
                ("assignee",10),
                ("milestone",10),
                ("labels",20)
                ]:
    issue[attribute] = "-" * (length)
print("| {P:4} | {N:4} | {title:20} | {assignee:10} | {milestone:10} | {labels:20} |".format(**issue))


for page in range(1,2):
    url = 'https://api.github.com/repos/cloudmesh/client/issues?page={}&per_page=100'.format(page)
    r = requests.get(url)
    issues = r.json()
    for issue in issues:
        #print (issue)
        #print (type(issue))
        assignee = issue["assignee"]
        if issue["assignee"] is not None:
            issue["assignee"] = issue["assignee"]["login"]
        else:
            issue["assignee"] = "None"

        if issue["milestone"] is not None:
            issue["milestone"] = issue["milestone"]["title"]
        else:
            issue["milestone"] = "None"

        if issue["labels"] is not None:
            content = []
            for label in issue["labels"]:
                content.append(label["name"])
            issue["labels"] = ", ".join(content)
        else:
            issue["labels"] = "None"


        priority = 999
        if issue["body"] is not None:
            body = issue["body"].splitlines()
            if len(body) >= 1:
                line = str(body[0])

                if "P:" in line:
                    priority = line.split("P:")[1]

        issue["priority"] = int(priority)

        content = ""
        for (attribute, length) in \
                [
                ("priority",4),
                ("number",4),
                ("title",20),
                ("assignee",10),
                ("milestone",10),
                ("labels",20)
                ]:
            data =  str(issue[attribute])
            if len(data) > length:
                issue[attribute] = data[:length-3] + "..."
        print("| {priority:4} | {number:4} | {title:20} | {assignee:10} | {milestone:10} | {labels:20} |".format(**issue))

