import json
from collections import defaultdict
import os

# Load the JSON data
with open('ClassEval_data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


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


def getTaskID():
    # Create a mapping of domain to task IDs
    domain_map = defaultdict(list)
    for task in data:
        task_id = task['task_id']
        class_name = task['class_name']
        for domain, keywords in domain_classnames.items():
            if class_name in keywords:
                domain_map[domain].append(task_id)
                break

    # # Print result summary
    # for domain, task_ids in domain_map.items():
    #     print(f"{domain}: ({len(task_ids)}):")
    #     for task_id in task_ids:
    #         print(f"  - {task_id}")
    
    return domain_map


domain_taskid = getTaskID()
for domain, task_ids in domain_taskid.items():
    print(f"{domain}: ({len(task_ids)})")
    for task_id in task_ids:
        print(f"  - {task_id}")