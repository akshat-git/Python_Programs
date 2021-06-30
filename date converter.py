date = input("Enter a date: ")
date = date.split("/")
months = {1:"January",
    2:"February",
    3:"March",
    4:"April",
    5:"May",
    6:"June",
    7:"July",
    8:"August",
    9:"September",
    10:"October",
    11:"November",
    12:"December"}
in_month = months[int(date[0])]
in_day = ""
days = {
    1:"st",
    2:"nd",
    3:"rd",
    4:"th",
    5:"th",
    6:"th",
    7:"th",
    8:"th",
    9:"th",
    0:"th",}
in_day = date[1]+str(days[int(date[1])%10])+","
print(in_month,in_day,date[2])
