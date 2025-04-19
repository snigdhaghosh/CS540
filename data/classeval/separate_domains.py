import json
from collections import defaultdict
import os

# Load the JSON data
with open('ClassEval_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# # Define keywords for each domain
# domain_keywords = {
#     'Management Systems': ['system', 'account', 'booking', 'registration', 'user management', 'authentication', 'access'],
#     'Data Formatting': ['format', 'convert', 'serialize', 'parser', 'transform', 'tokenize'],
#     'Mathematical Operations': ['calculate', 'compute', 'arithmetic', 'math', 'sum', 'average'],
#     'Game Development': ['game', 'player', 'board', 'score', 'move'],
#     'File Handling': ['file', 'csv', 'json', 'read', 'write', 'load', 'save'],
#     'Database Operations': ['database', 'query', 'sql', 'record', 'table'],
#     'Natural Language Processing': ['text', 'nlp', 'word', 'sentence', 'stop word', 'token']
# }

# # Helper function to assign a domain
# def classify_domain(description):
#     description = description.lower()
#     for domain, keywords in domain_keywords.items():
#         if any(kw in description for kw in keywords):
#             return domain
#     return 'Uncategorized'  # fallback if no match

# # Classify each task
# domain_map = defaultdict(list)
# for task in data:
#     desc = task.get("class_description", "")
#     domain = classify_domain(desc)
#     domain_map[domain].append(task["class_name"])
    # domain_map[domain].append(task["task_id"])


# # Print result summary
# for domain, task_ids in domain_map.items():
#     # if domain == 'Uncategorized':
#     print(f"{domain}: ({(task_ids)}):")
#         # for task_id in task_ids:
#         #     print(f"  - {task_id}")



# Define keywords for each domain
domain_classnames = {
    # needs to be 27, but there are 27
    'Management Systems':['AccessGatewayFilter', 'AssessmentSystem', 'BankAccount', 'BookManagement', 'ClassRegistrationSystem', 
                        'Hotel', 'HRManagementSystem', 'MovieBookingSystem', 'SignInSystem', 'WeatherSystem', 
                        'Warehouse', 'VendingMachine', 'Server', 'Chat', 'Classroom', 
                        'CookiesUtil', 'Order', 'Thermostat', 'FitnessTracker', 'AutomaticGuitarSimulator',
                        'DiscountStrategy', 'EmailClient','PageUtil','ShoppingCart','MusicPlayer',
                        'JobMarketplace','CalendarUtil'
                        ],    

    # needs to be 26, but there are 26
    'Data Formatting':['BinaryDataProcessor', 'CamelCaseMap', 'CurrencyConverter', 'HtmlUtil', 'NumberConverter', 
                        'NumberWordFormatter', 'ArgumentParser', 'TimeUtils', 'UrlPath', 'BitStatusUtil', 
                        'AvgPartition', 'BalancedBrackets', 'DecryptionUtils','EncryptionUtils','IPAddress',
                        'IpUtil','Interpolation', 'Manacher', 'NumericEntityUnescaper','RegexUtils',
                        'BoyerMooreSearch', 'URLHandler','PersonRequest','SplitSentence', 'StockPortfolioTracker',
                        'VectorUtil'
                       ],

    
    # needs to be 16 but there are 17
    'Mathematical Operations': ['AreaCalculator','Calculator', 'CombinationCalculator', 'ComplexCalculator', 'DataStatistics', 
                                'BigNumCalculator','DataStatistics2', 'DataStatistics4', 'ExpressionCalculator', 'KappaCalculator', 
                                'MetricsCalculator', 'MetricsCalculator2', 'Statistics3','ArrangementCalculator', 'TriCalculator', 
                                'ChandrasekharSieve'],
    
    ## done!!
    # needs to be 10, but there are 10
    'Game Development': ['BlackjackGame', 'EightPuzzle', 'GomokuGame',
                         'MahjongConnect', 'MinesweeperGame', 'PushBoxGame', 
                         'RPGCharacter', 'Snake',  'TicTacToe', 'TwentyFourPointGame'],
    
    # needs to be 9, but there are 9
    'File Handling': ['CSVProcessor', 'DocFileHandler', 'ExcelProcessor', 'ImageProcessor', 
                      'JSONProcessor', 'PDFHandler', 'TextFileProcessor', 'XMLProcessor', 'ZipFileProcessor'],
    
    # needs to be 7, but there are 7
    'Database Operations': ['DatabaseProcessor', 'SQLGenerator', 'SQLQueryBuilder',
                            'StudentDatabaseProcessor', 'BookManagementDB', 'UserLoginDB', 'MovieTicketDB'],

    #needs to be 5, but there are 5
    'Natural Language Processing':['LongestWord', 'NLPDataProcessor', 'Lemmatization',
                                   'NLPDataProcessor2', 'Words2Numbers']
                              
}


# Print result summary
for domain, task_ids in domain_classnames.items():
    # if domain == 'Uncategorized':
    print(f"{domain}: ({len(task_ids)})")
        # for task_id in task_ids:
        #     print(f"  - {task_id}")



# === Prepare output directory ===
output_dir = "separated_domains"
os.makedirs(output_dir, exist_ok=True)

# === Build reverse lookup for fast filtering ===
class_to_domain = {}
for domain, class_list in domain_classnames.items():
    for cname in class_list:
        class_to_domain[cname] = domain

# === Group tasks ===
domain_tasks = {domain: [] for domain in domain_classnames}
# domain_tasks["Uncategorized"] = []

for task in data:
    cname = task.get("class_name")
    domain = class_to_domain.get(cname)
    if domain:
        domain_tasks[domain].append(task)
    else:
        domain_tasks["Uncategorized"].append(task)

# === Save to separate files ===
for domain, tasks in domain_tasks.items():
    fname = f"{domain.replace(' ', '_')}.json"
    path = os.path.join(output_dir, fname)
    with open(path, "w") as f:
        json.dump(tasks, f, indent=2)

