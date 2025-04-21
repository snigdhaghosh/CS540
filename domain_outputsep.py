import json
from collections import defaultdict
import os
import sys


# Add the folder to sys.path
sys.path.append(os.path.abspath('/path/to/folder'))
import data.classeval.separate_domains as sd


# Load the JSON data
with open('model_outputs/ChatGPT_100_c_5.json', 'r', encoding='utf-8') as f:
    outdata = json.load(f)

# for task in outdata:
#     desc = task.get("class_name")
#     print(desc)
# print(len(outdata)) # 100


domain_tasks = {domain: [] for domain in sd.domain_classnames}
# print(f"Domain tasks: {domain_tasks}")

# Separate tasks by domain
for task in outdata:
    desc = task.get("class_name")
    # print(desc)
    for domain, classnames in sd.domain_classnames.items():
        if desc in classnames:
            domain_tasks[domain].append(task)
            break

output_dir = "./separated_output/ChatGPT_100_c_5"
for domain, tasks in domain_tasks.items():
    fname = f"{domain.replace(' ', '_')}.json"
    path = os.path.join(output_dir, fname)
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)
    

# # Print the number of tasks in each domain
# for domain, tasks in domain_tasks.items():
#     print(f"{domain}: {len(tasks)} tasks")
