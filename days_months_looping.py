from isoweek import Week
import os
import pkg_resources
# to save table as image
from pandas.plotting import table
import matplotlib.pyplot as plt

def iter_by_weeks(year, start_week, end_week):
    for weeks in range(start_week, end_week):

        print(weeks)
        
        c_week = Week(year, weeks)

        s_date, e_date = c_week.monday(), c_week.sunday()

import pandas as pd
# start date and end date are inclusive
# start_date and end_date are date timestamp
def iter_by_days(start_date, end_date):
    s_date = pd.Timestamp(start_date)
    e_date = pd.Timestamp(end_date)
    while s_date <= e_date:
        current_date = s_date.date() 
        print(current_date)
        s_date += pd.Timedelta('1 days')

import time
# this function could be used to time how long a function will take
def timer(func, func_description='this', **func_parameters):
    s_time = time.time()
    output = func(**func_parameters)
    e_time = time.time()
    print('spend {time}s for {func_description} function'.format(time=e_time-s_time, func_description=func_description))
    return output

# change the format of int or float to standard notation format
def format_num(df):
    return df.apply(lambda x: x.apply(lambda y: "{:,}".format(round(y, 3)) if (isinstance(y, float) or isinstance(y, int)) else y))

# return all file names given a directory
def get_files_from_dir(add):
    add_lst = []
    for i in os.listdir(add):
        complete_add = os.path.join(add, i)
#        return complete_add
        add_lst.append(i)
        # stats[i] = pd.read_csv(complete_add, index_col=0)
    return add_lst

# get python package information
def get_pkg_version_pkg(pkg_name):
    return pkg_resources.get_distribution(pkg_name)

# save table as image
def save_table_as_img(df, img_name):
    fig = plt.figure(figsize=(5, 6), dpi=1400)
    ax = fig.add_subplot(111, frame_on=False) # no visible frame
    ax.xaxis.set_visible(False)  # hide the x axis
    ax.yaxis.set_visible(False)  # hide the y axis
    table(ax, df, loc='center')  # where df is your data frame
    plt.savefig(img_name)

def save_pandas_to_excel(df1, df2, df3):
    writer = pd.ExcelWriter('pandas_multiple.xlsx')

    # Write each dataframe to a different worksheet.
    df1.to_excel(writer, sheet_name='Sheet1')
    df2.to_excel(writer, sheet_name='Sheet2')
    df3.to_excel(writer, sheet_name='Sheet3')

    # Close the Pandas Excel writer and output the Excel file.
    writer.save()
    writer.close()