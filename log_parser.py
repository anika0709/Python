# #27.59.104.166 - - [04/Oct/2019:21:15:54 +0000] "GET /users/login HTTP/1.1" 200 41716 "-" "okhttp/3.12.1"
# #IP_ADDRESS - - [DATETIME] "METHOD /users/login HTTP/1.1" STATUS_CODE 41716 "-" "okhttp/3.12.1"

# parsed_data = []
  
# with open("example.logs","r") as file:
#     prev_time = ""
#     data = {}
#     for line in file:
#         time = line.split("[")[1].split("]")[0].split(" ")[0]
#         status_code = line.split('"')[2].split(" ")[1]
#         if prev_time != "":
#             if time == prev_time:
#                 data[time]["count"] = data[time]["count"] + 1
#                 if status_code in data[time]:
#                     data[time][status_code] = data[time][status_code] + 1
#                 else:
#                     data[time][status_code] = 1
#             else:
#                 prev_time = time
#                 parsed_data.append(data)
#                 data = {}
#                 data[time] = {"count": 1, status_code: 1}
#         else:
#             prev_time = time
#             data[time] = {"count": 1, status_code: 1}

# for i in parsed_data:
#     print(i)

#######
# log files with identical structure:

# [timestamp] [level] [source] message
# For example:
# [Wed Oct 11 14:32:52 2000] [error] [client 127.0.0.1] error message

# I need to write a program in pure Python which should merge these log files into one file and then sort the merged file by timestamp.
import fileinput
# import re
# from time import strptime

# f_names = ['1.log', '2.log'] # names of log files
# lines = list(fileinput.input(f_names))
# t_fmt = '%a %b %d %H:%M:%S %Y' # format of time stamps
# t_pat = re.compile(r'\[(.+?)\]') # pattern to extract timestamp
# for l in sorted(lines, key=lambda l: strptime(t_pat.search(l).group(1), t_fmt)):
#     print(l)

#Write a program that takes filename as input(apache logfile), depending on the command line arguments(-u or -t) writes to a file:
#A. The list of all unique clients in the logfile to a text file (-u)
#B. The list of all the unique clients to a text file sorted by number of requests they made. (-t)

# ACCESS_LOG_PATTERN = '^(\S+) (\S+) (\S+) \[([\w:/]+\s[+\-]\d{4})\] "(\S+) (\S+)\s*(\S+)\s*" (\d{3}) (\S+)'

# logLine='127.0.0.1 - - [01/Jul/1995:00:00:01 -0400] "GET /images/launch-logo.gif HTTP/1.0" 200 1839'

import re


HOST = r'^(?P<host>.*?)'
SPACE = r'\s'
IDENTITY = r'\S+'
USER = r'\S+'
TIME = r'(?P<time>\[.*?\])'
REQUEST = r'\"(?P<request>.*?)\"'
STATUS = r'(?P<status>\d{3})'
SIZE = r'(?P<size>\S+)'

REGEX = HOST+SPACE+IDENTITY+SPACE+USER+SPACE+TIME+SPACE+REQUEST+SPACE+STATUS+SPACE+SIZE+SPACE

def parser(log_line):
    match = re.search(REGEX,log_line)
    return ( (match.group('host'),
            match.group('time'), 
                      match.group('request') , 
                      match.group('status') ,
                      match.group('size')
                     )
                   )


logLine = """180.76.15.30 - - [24/Mar/2017:19:37:57 +0000] "GET /shop/page/32/?count=15&orderby=title&add_to_wishlist=4846 HTTP/1.1" 404 10202 "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"""
result = parser(logLine)
print(result)

#######
import re
log = '10.243.166.74, 10.243.166.74 - - [08/Feb/2017:16:33:26 +0100] "GET /script/header_footer.js?_=1486568008442 HTTP/1.1" 200 2143 "http://www.trendtron.com/popmenu/home" "Mozilla/5.0 (Windows NT 6.1; rv:31.0) Gecko/20100101 Firefox/31.0 K-Meleon/75.1"'

regex = re.compile('(.+?)\[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"')
res = regex.match(log)
log_parts = list(res.groups())
devices_browsers_info_str = log_parts.pop(-1)
devices_browsers_info_parts = devices_browsers_info_str.split(' ')
log_parts.extend(devices_browsers_info_parts)
print(log_parts)