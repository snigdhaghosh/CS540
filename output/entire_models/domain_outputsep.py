import json
import os
from collections import defaultdict
import sys

# Add the folder containing separate_domains.py to sys.path
# sys.path.append(os.path.abspath('./data'))  # Adjust if your script lives elsewhere

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


# import data.separate_domains as sd

model_outputs_dir = "output/entire_models"
output_root_dir = "separated_output"

# Loop through all JSON files in model_outputs/
for filename in os.listdir(model_outputs_dir):
    if filename.endswith(".json"):
        model_output_path = os.path.join(model_outputs_dir, filename)
        model_name = filename.replace(".json", "")
        model_folder = model_name

        with open(model_output_path, 'r', encoding='utf-8') as f:
            outdata = json.load(f)

        domain_tasks = {domain: [] for domain in domain_classnames}

        for task in outdata:
            desc = task.get("class_name")
            for domain, classnames in domain_classnames.items():
                if desc in classnames:
                    domain_tasks[domain].append(task)
                    break

        # Create model-specific output folder
        output_dir = os.path.join(output_root_dir, model_folder)
        os.makedirs(output_dir, exist_ok=True)

        for domain, tasks in domain_tasks.items():
            fname = f"{model_name}_{domain.replace(' ', '_')}.json"
            path = os.path.join(output_dir, fname)
            with open(path, "w") as f:
                json.dump(tasks, f, indent=2)

        print(f"Processed and saved: {model_output_path}")





























# import json
# from collections import defaultdict
# import os
# import sys


# # Add the folder to sys.path
# sys.path.append(os.path.abspath('/path/to/folder'))
# import data.separate_domains as sd

# model_output = "GPT-4_100_c_5.json"
# model_folder = "GPT-4_100_c_5"
# model_name = "GPT-4"

# # Load the JSON data
# with open(('model_outputs/'+model_output), 'r', encoding='utf-8') as f:
#     outdata = json.load(f)

# # for task in outdata:
# #     desc = task.get("class_name")
# #     print(desc)
# # print(len(outdata)) # 100


# domain_tasks = {domain: [] for domain in sd.domain_classnames}
# # print(f"Domain tasks: {domain_tasks}")

# # Separate tasks by domain
# for task in outdata:
#     desc = task.get("class_name")
#     # print(desc)
#     for domain, classnames in sd.domain_classnames.items():
#         if desc in classnames:
#             domain_tasks[domain].append(task)
#             break




# output_dir = "./separated_output/"+model_folder
# for domain, tasks in domain_tasks.items():
#     fname = f"{model_name}_{domain.replace(' ', '_')}.json"
#     path = os.path.join(output_dir, fname)
#     with open(path, "w") as f:
#         json.dump(tasks, f, indent=2)
    

# # # Print the number of tasks in each domain
# # for domain, tasks in domain_tasks.items():
# #     print(f"{domain}: {len(tasks)} tasks")
