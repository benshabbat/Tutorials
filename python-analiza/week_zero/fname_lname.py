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

    '2025-10-08T06:41:00Z;auth;INFO;user login ok',
    '2025-10-08T06:42:00Z;db;ERROR;connection timeout',
    '2025-10-08T06:43:00Z;api;WARN;slow response detected',
    '2025-10-08T06:44:00Z;auth;INFO;new user registered',
    '2025-10-08T06:45:00Z;web;DEBUG;session cookie created',
    '2025-10-08T06:46:00Z;auth;INFO;user logout ok',
    '2025-10-08T06:47:00Z;db;INFO;query executed successfully',
    '2025-10-08T06:48:00Z;api;ERROR;invalid json format',
    '2025-10-08T06:49:00Z;cache;INFO;cache cleared',
    '2025-10-08T06:50:00Z;auth;WARN;multiple failed logins',
    '2025-10-08T06:51:00Z;db;INFO;replica sync complete',
    '2025-10-08T06:52:00Z;api;INFO;endpoint /status called',
    '2025-10-08T06:53:00Z;web;INFO;homepage rendered',
    '2025-10-08T06:54:00Z;auth;ERROR;invalid token',
    '2025-10-08T06:55:00Z;cache;DEBUG;cache hit for user id=23',
    '2025-10-08T06:56:00Z;db;WARN;slow query detected',
    '2025-10-08T06:57:00Z;api;INFO;GET /users successful',
    '2025-10-08T06:58:00Z;auth;INFO;password reset requested',
    '2025-10-08T06:59:00Z;web;ERROR;missing static resource',
    '2025-10-08T07:00:00Z;cache;INFO;cache warmup completed',
    '2025-10-08T07:01:00Z;auth;INFO;user verified via email',
    '2025-10-08T07:02:00Z;db;INFO;backup completed',
    '2025-10-08T07:03:00Z;api;WARN;rate limit reached',
    '2025-10-08T07:04:00Z;auth;DEBUG;JWT token created',
    '2025-10-08T07:05:00Z;web;INFO;page /profile loaded',
    '2025-10-08T07:06:00Z;cache;INFO;cache updated for /api/users',
    '2025-10-08T07:07:00Z;db;ERROR;duplicate key error',
    '2025-10-08T07:08:00Z;api;INFO;POST /login success',
    '2025-10-08T07:09:00Z;auth;INFO;2FA verified',
    '2025-10-08T07:10:00Z;web;INFO;assets preloaded',
    '2025-10-08T07:11:00Z;cache;WARN;cache miss for session id=45',
    '2025-10-08T07:12:00Z;db;INFO;transaction committed',
    '2025-10-08T07:13:00Z;api;ERROR;missing authorization header',
    '2025-10-08T07:14:00Z;auth;INFO;role updated to admin',
    '2025-10-08T07:15:00Z;web;INFO;logout page rendered',
    '2025-10-08T07:16:00Z;cache;INFO;cache entry expired',
    '2025-10-08T07:17:00Z;db;DEBUG;query plan optimized',
    '2025-10-08T07:18:00Z;api;INFO;PUT /settings success',
    '2025-10-08T07:19:00Z;auth;WARN;user session expired',
    '2025-10-08T07:20:00Z;web;INFO;error 404 rendered',
    '2025-10-08T07:21:00Z;cache;DEBUG;cache cleanup started',
    '2025-10-08T07:22:00Z;db;INFO;index rebuilt',
    '2025-10-08T07:23:00Z;api;INFO;DELETE /session ok',
    '2025-10-08T07:24:00Z;auth;INFO;user deleted',
    '2025-10-08T07:25:00Z;web;WARN;redirect loop detected',
    '2025-10-08T07:26:00Z;cache;INFO;cache compression done',
    '2025-10-08T07:27:00Z;db;INFO;schema migration complete',
    '2025-10-08T07:28:00Z;api;ERROR;internal server error',
    '2025-10-08T07:29:00Z;auth;INFO;user login ok',
    '2025-10-08T07:30:00Z;web;INFO;dashboard loaded'
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

# print(top_service_by_errors(logs))




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


# if __name__ == "__main__":
#     run_cli(logs)



# LEVEL FOUR

# FUNCTION ONE
def errors_by_service(logs_dicts: list[dict]) -> dict[str, int]:
    service_errors = {}
    for log in logs_dicts:
        if log.get("level") == "ERROR":
            service = log.get("service")
            if service not in service_errors:
                service_errors[service] = 1
            else:
                service_errors[service] += 1
    return service_errors

# print(errors_by_service(logs))


# FUNCTION TWO

def worst_service_ratio(logs_dicts: list[dict]) -> tuple[str, float] | None:
    service_errors = errors_by_service(logs_dicts)
    service_totals = {}

    for log in logs_dicts:
        service = log.get("service")

        if service not in service_totals:
            service_totals[service] = 0
        service_totals[service] += 1  
    # print(service_totals)
    # print(service_errors)
    worst_service = None
    worst_ratio = -1.0

    for service, total in service_totals.items():
        errors = service_errors.get(service, 0)
        # print(errors)
        # print(total)
        ratio = errors / total if total > 0 else 0

        if ratio > worst_ratio:
            worst_ratio = ratio
            worst_service = service

    return (worst_service, worst_ratio) if worst_service else None
# print(worst_service_ratio(logs))



# FUNCTION THREE
def sort_by_severity(logs_dicts: list[dict]) -> list[dict]:
    severity_order = {'ERROR': 1, 'WARN': 2, 'INFO': 3}
    logs_dicts = [log for log in logs_dicts if log['level'] in severity_order]
    return sorted(logs_dicts, key=lambda log: severity_order.get(log['level'], 0))


# print(sort_by_severity(logs))

# FUNCTION FOUR    
def find_by_message(logs_dicts: list[dict], keyword: str) -> list[dict]:
    keyword = keyword.lower()
    return [log for log in logs_dicts if keyword in log['message'].lower()]
# print(find_by_message(logs, "user"))

# FUNCTION FIVE
def generate_report(logs_dicts: list[dict]) -> str:

    total_entries = len(logs_dicts)    
    total_errors = sum(1 for log in logs_dicts if log.get('level') == 'ERROR')
    worst_service_info = worst_service_ratio(logs_dicts)
    if worst_service_info:
        worst_service_name = worst_service_info[0]
        worst_service_ratio_percent = int(worst_service_info[1] * 100)
    else:
        worst_service_name = "N/A"
        worst_service_ratio_percent = 0
    
    top_service_info = top_service_by_errors(logs_dicts)
    if top_service_info:
        top_service_name = top_service_info[0]
        top_service_errors = top_service_info[1]
    else:
        top_service_name = "N/A"
        top_service_errors = 0
    
    report = f"""=== System Report ===
    Total entries: {total_entries}
    Total errors: {total_errors}
    Most problematic service (by ratio): {worst_service_name} ({worst_service_ratio_percent}%)
    Most errors (by count): {top_service_name} ({top_service_errors} errors)"""
    
    return report

data = [
    {'ts': '2025-10-08T06:41:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'user login ok'},
    {'ts': '2025-10-08T06:42:00Z', 'service': 'db', 'level': 'ERROR', 'message': 'connection timeout'}, 
    {'ts': '2025-10-08T06:43:00Z', 'service': 'api', 'level': 'WARN', 'message': 'slow response detected'}, 
    {'ts': '2025-10-08T06:44:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'new user registered'}, 
    {'ts': '2025-10-08T06:45:00Z', 'service': 'web', 'level': 'DEBUG', 'message': 'session cookie created'}, 
    {'ts': '2025-10-08T06:46:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'user logout ok'},
    {'ts': '2025-10-08T06:47:00Z', 'service': 'db', 'level': 'INFO', 'message': 'query executed successfully'}, 
    {'ts': '2025-10-08T06:48:00Z', 'service': 'api', 'level': 'ERROR', 'message': 'invalid json format'}, 
    {'ts': '2025-10-08T06:49:00Z', 'service': 'cache', 'level': 'INFO', 'message': 'cache cleared'},
    {'ts': '2025-10-08T06:50:00Z', 'service': 'auth', 'level': 'WARN', 'message': 'multiple failed logins'},
    {'ts': '2025-10-08T06:51:00Z', 'service': 'db', 'level': 'INFO', 'message': 'replica sync complete'}, 
    {'ts': '2025-10-08T06:52:00Z', 'service': 'api', 'level': 'INFO', 'message': 'endpoint /status called'},
    {'ts': '2025-10-08T06:53:00Z', 'service': 'web', 'level': 'INFO', 'message': 'homepage rendered'},
    {'ts': '2025-10-08T06:54:00Z', 'service': 'auth', 'level': 'ERROR', 'message': 'invalid token'},
    {'ts': '2025-10-08T06:55:00Z', 'service': 'cache', 'level': 'DEBUG', 'message': 'cache hit for user id=23'},
    {'ts': '2025-10-08T06:56:00Z', 'service': 'db', 'level': 'WARN', 'message': 'slow query detected'},
    {'ts': '2025-10-08T06:57:00Z', 'service': 'api', 'level': 'INFO', 'message': 'GET /users successful'},
    {'ts': '2025-10-08T06:58:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'password reset requested'},
    {'ts': '2025-10-08T06:59:00Z', 'service': 'web', 'level': 'ERROR', 'message': 'missing static resource'},
    {'ts': '2025-10-08T07:00:00Z', 'service': 'cache', 'level': 'INFO', 'message': 'cache warmup completed'},
    {'ts': '2025-10-08T07:01:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'user verified via email'},
    {'ts': '2025-10-08T07:02:00Z', 'service': 'db', 'level': 'INFO', 'message': 'backup completed'},
    {'ts': '2025-10-08T07:03:00Z', 'service': 'api', 'level': 'WARN', 'message': 'rate limit reached'},
    {'ts': '2025-10-08T07:04:00Z', 'service': 'auth', 'level': 'DEBUG', 'message': 'JWT token created'},
    {'ts': '2025-10-08T07:05:00Z', 'service': 'web', 'level': 'INFO', 'message': 'page /profile loaded'},
    {'ts': '2025-10-08T07:06:00Z', 'service': 'cache', 'level': 'INFO', 'message': 'cache updated for /api/users'},
    {'ts': '2025-10-08T07:07:00Z', 'service': 'db', 'level': 'ERROR', 'message': 'duplicate key error'},
    {'ts': '2025-10-08T07:08:00Z', 'service': 'api', 'level': 'INFO', 'message': 'POST /login success'},
    {'ts': '2025-10-08T07:09:00Z', 'service': 'auth', 'level': 'INFO', 'message': '2FA verified'},
    {'ts': '2025-10-08T07:10:00Z', 'service': 'web', 'level': 'INFO', 'message': 'assets preloaded'},
    {'ts': '2025-10-08T07:11:00Z', 'service': 'cache', 'level': 'WARN', 'message': 'cache miss for session id=45'},
    {'ts': '2025-10-08T07:12:00Z', 'service': 'db', 'level': 'INFO', 'message': 'transaction committed'},
    {'ts': '2025-10-08T07:13:00Z', 'service': 'api', 'level': 'ERROR', 'message': 'missing authorization header'},
    {'ts': '2025-10-08T07:14:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'role updated to admin'},
    {'ts': '2025-10-08T07:15:00Z', 'service': 'web', 'level': 'INFO', 'message': 'logout page rendered'},
    {'ts': '2025-10-08T07:16:00Z', 'service': 'cache', 'level': 'INFO', 'message': 'cache entry expired'},
    {'ts': '2025-10-08T07:17:00Z', 'service': 'db', 'level': 'DEBUG', 'message': 'query plan optimized'},
    {'ts': '2025-10-08T07:18:00Z', 'service': 'api', 'level': 'INFO', 'message': 'PUT /settings success'},
    {'ts': '2025-10-08T07:19:00Z', 'service': 'auth', 'level': 'WARN', 'message': 'user session expired'},
    {'ts': '2025-10-08T07:20:00Z', 'service': 'web', 'level': 'INFO', 'message': 'error 404 rendered'},
    {'ts': '2025-10-08T07:21:00Z', 'service': 'cache', 'level': 'DEBUG', 'message': 'cache cleanup started'},
    {'ts': '2025-10-08T07:22:00Z', 'service': 'db', 'level': 'INFO', 'message': 'index rebuilt'},
    {'ts': '2025-10-08T07:23:00Z', 'service': 'api', 'level': 'INFO', 'message': 'DELETE /session ok'},
    {'ts': '2025-10-08T07:24:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'user deleted'},
    {'ts': '2025-10-08T07:25:00Z', 'service': 'web', 'level': 'WARN', 'message': 'redirect loop detected'},
    {'ts': '2025-10-08T07:26:00Z', 'service': 'cache', 'level': 'INFO', 'message': 'cache compression done'},
    {'ts': '2025-10-08T07:27:00Z', 'service': 'db', 'level': 'INFO', 'message': 'schema migration complete'},
    {'ts': '2025-10-08T07:28:00Z', 'service': 'api', 'level': 'ERROR', 'message': 'internal server error'},
    {'ts': '2025-10-08T07:29:00Z', 'service': 'auth', 'level': 'INFO', 'message': 'user login ok'},
    {'ts': '2025-10-08T07:30:00Z', 'service': 'web', 'level': 'INFO', 'message': 'dashboard loaded'}
]


print(generate_report(data))