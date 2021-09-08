# import re
# def change_date_format(dt):
#         return re.sub(r'(\d{4})-(\d{1,2})-(\d{1,2})', '\\3-\\2-\\1', dt)
# dt1 = "2026-01-02"
# print("Original date in YYY-MM-DD Format: ",dt1)
# print("New date in DD-MM-YYYY Format: ",change_date_format(dt1))


import datetime

today_date = datetime.date.today()
# h = str(today_date).split('-')
# year_d = h[0]
# month_d = h[1]
# date_d = h[2]
# new_date = (date_d + '-' + month_d + '-' + year_d)
# print(today_date)
# print(h)
# print(new_date)

new_today_date = today_date.strftime("%d-%m-%Y")
print (new_today_date)

