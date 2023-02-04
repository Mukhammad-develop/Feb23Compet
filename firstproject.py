try:
    def progCount(days):
        years_r = days // 365
        weeks_r = (days - years_r * 365) // 7
        days_r = days - years_r * 365 - weeks_r * 7
        res_y = f'Years : {years_r}'
        res_w = f'Week : {weeks_r}'
        res_d = f'Days : {days_r}'
        return res_y, res_w, res_d

    print(progCount(int(input("Enter days: "))))
except ValueError:
    print("Enter only numbers\nRun programm again!")
