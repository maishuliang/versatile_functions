from isoweek import Week

def iter_by_weeks(year, start_week, end_week):
    for weeks in range(start_week, end_week):

        print(weeks)
        
        c_week = Week(year, weeks)

        s_date, e_date = c_week.monday(), c_week.sunday()

