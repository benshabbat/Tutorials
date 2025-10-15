# שם פרטי שם משחפה ת.ז

# LEVEL ONE
# FUNC ONE
def parse_line(line: str)->dict | None:
    parts = line.split(";")
    if (len(parts) == 4 and parts[0] and parts[1] and parts[2] and parts[3]):
        return {
            'ts': parts[0],
            'service': parts[1],
            'level': parts[2],
            'message': parts[3]
        }
    return None

dicts = [
    "2025-10-08T06:41:00Z;auth;INFO;user login ok",
    "2025-10-08T06:41:00Z;auth;DEBUG;user login ok",
    "2025-10-08T06:41:00Z;auth;DEBUG;user login ok",
    "2025-10-08T06:41:00Z;auth;DEBUG;user login ok",
    "2025-10-08T06:41:00Z;auth;ALERT;user login ok",
    "2025-10-08T06:41:00Z;auth;FATAL;user login ok",
    "2025-10-08T06:41:00Z;auth;FATAL;user login ok",
    "2025-10-08T06:41:00Z;auth;WARN;user login ok",
    "2025-10-08T06:41:00Z;auth;ERROR;user login ok",
    "2025-10-08T06:41:00Z;auth;ERROR;user login ok",
    "2025-10-08T06:41:00Z;auth;ERROR;user login ok",
    "2025-10-08T06:41:00Z;db;ERROR;user login ok",
    "2025-10-08T06:41:00Z;db;ERROR;user login ok",
    "2025-10-08T06:41:00Z;db;ERROR;user login ok",
    "2025-10-08T06:41:00Z;db;ERROR;user login ok",
    "2025-10-08T06:41:00Z;api;ERROR;user login ok",


    "2025-10-08T06:41:00Z;auth;INFO",
    "2025-10-08T06:41:00Z;auth;INFO;",
    "2025-10-08T06:41:00Z;auth;;user login ok"
]



# FUNC TWO
def parse_logs(lines: list[str]) -> list[dict]:
    return [parse_line(line) for line in lines if parse_line(line)]


logs = parse_logs(dicts)

# for log in logs:
#     print(log)
    
    
# FUNC THREE

def count_by_level(log_dicts: list[dict]) -> dict:
    # obj_levels = {'DEBUG': 0, 'INFO': 0, 'WARN': 0, 'ERROR': 0, 'FATAL': 0, 'ALERT': 0}
    # for log in log_dicts:
    #     level = log.get('level')
    #     if level in obj_levels:
    #         obj_levels[level] += 1
            
    # for level in obj_levels:
    #     if obj_levels[level] == 0:
    #         del obj_levels[level]
    # return obj_levels
    
    levels = [ 'DEBUG', 'INFO', 'ALERT', 'FATAL', 'WARN', 'ERROR']
    obj_levels = {}
    for log in log_dicts:
        level = log.get('level')
        if level in levels:
            if level not in obj_levels.keys():
                obj_levels[level] = 1
            else:
                obj_levels[level] += 1
    return obj_levels




counts = count_by_level(logs)
# print(counts)


# FUNC FOUR    


def top_service_by_errors(log_dicts: list[dict]) -> tuple[str, int] | None:
    obj_services_by_errors = {}
    for log in log_dicts:
        level = log.get('level')
        service = log.get('service')
        if level == 'ERROR':
            if service not in obj_services_by_errors.keys():
                obj_services_by_errors[service] = 1
            else:
                obj_services_by_errors[service] += 1
    max_service = max(obj_services_by_errors, key=obj_services_by_errors.get, default=None)
    return (max_service, obj_services_by_errors[max_service]) if max_service else None

print(top_service_by_errors(logs))




#LEVEL TWO
# Question one
# start section 2
'''

הבעיה בפונקציה של accumulate_errors היא שהמשתנה total_errors מוגדר מחוץ לפונקציה, ולכן כל פעם שהפונקציה נקראת
, היא יוצרת משתנה מקומי חדש בשם total_errors שמתחיל מ-0, ולא משנה את המשתנה הגלובלי.
בנוסף בלולאה יש שימוש במשתנה entries שלא מוגדר בשום מקום בקוד, מה שיגרום לשגיאה.
סביר להניח שהיה צריך להשתמש בפרמטר log_dicts במקום entries.



כמו כן בפונקציה השנייה report_and_reset יש בעיה דומה - המשתנה total_errors מוגדר מחוץ לפונקציה, ולכן כל פעם שהפונקציה נקראת
'''


# end section 2


# Found Bug
# Question two

total_errors = 0

def accumulate_errors(logs_dicts):
    global total_errors
    # total_errors = 0
    # for e in entries:
    for e in logs_dicts:
        if e.get("level") == "ERROR":
            total_errors += 1
    return total_errors

def report_and_reset():
    global total_errors
    print("Total errors so far:", total_errors)
    total_errors = 0
   
# if __name__ == "__main__":    
#     num_err= accumulate_errors(logs)  
#     print(num_err)
#     print(total_errors)
#     report_and_reset()
#     print(total_errors)
    
    
    
# LEVEL THREE 

def filter_logs(logs_dicts: list[dict]) -> list[dict]:
    print("Filter by:")
    print("1) Service")
    print("2) Level")

    choice = input("Choose: ").strip()

    filtered = []

    if choice == "1":
        service = input("Enter service name: ").strip()
        for log in logs_dicts:
            if log["service"] == service:
                filtered.append(log)

    elif choice == "2":
        level = input("Enter log level: ").strip()
        for log in logs_dicts:
            if log["level"] == level:
                filtered.append(log)

    else:
        print("Invalid choice.")
        return []

    return filtered[:5] 
    
def run_cli(logs_dicts: list[dict]) -> None:

    while True:
        print("\n=== Log Monitor ===")
        print("1) Count by level")
        print("2) Top service by errors")
        print("3) Filter logs manually")
        print("4) Exit")
        num = input("Choose an option (1-4): ").strip()
        if num == '1':
            counts = count_by_level(logs_dicts)
            print("Log counts by level:")
            print(counts)
        elif num == '2':
            top_service = top_service_by_errors(logs_dicts)
            print(top_service)
        elif num == '3':
            filtered_logs = filter_logs(logs_dicts)
            print("Filtered logs (up to 5):")
            for log in filtered_logs:
                print(log)
                
        elif num == '4':
            print("Bye.")
            break        
        else:
            print("Invalid option. Please choose between 1 and 4.")


if __name__ == "__main__":
    run_cli(logs)



# LEVEL FOUR