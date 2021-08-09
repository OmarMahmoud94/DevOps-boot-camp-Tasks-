import datetime
new_date_list = []


def change_date_format(date_list, date_format="%Y/%m/%d", i=0):
    print(date_list)
    for date in date_list:
        print(date, "begin")
        condition = True
        while condition:
            try:
                date_ob = datetime.datetime.strptime(date, date_format)
                new_date = date_ob.strftime("%Y%m%d")
                new_date_list.append(new_date)
                i = 0
                date_format = "%Y/%m/%d"
                condition = False
            except:
                i += 1
                if i == 1:
                    date_format = "%d/%m/%Y"
                elif i == 2:
                    date_format = "%m-%d-%Y"
                else:
                    condition = False
    print(new_date_list)


change_date_format(["2021/12/01", "01/12/2020", "03-20-1996", "19630303"])
