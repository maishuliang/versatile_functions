from isoweek import Week

def iter_by_weeks(year, start_week, end_week):
    for weeks in range(start_week, end_week):

        print(weeks)
        
        c_week = Week(year, weeks)

        s_date, e_date = c_week.monday(), c_week.sunday()

import time
# this function could be used to time how long a function will take
def timer(func, func_description='this', **func_parameters):
    s_time = time.time()
    output = func(**func_parameters)
    e_time = time.time()
    print('spend {time}s for {func_description} function'.format(time=e_time-s_time, func_description=func_description))
    return output
