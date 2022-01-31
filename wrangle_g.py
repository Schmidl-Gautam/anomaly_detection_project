# Imports
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np
import pandas as pd
from datetime import datetime

def prep_cur_df():
    # Getting curriculum log file cur_df with courses included:
    cur_df = add_course_names()

    # droping column deleted_at
    cur_df = cur_df.drop(columns = ['deleted_at'])

    # filtering out just a single null value in path
    cur_df = cur_df[~cur_df.path.isna()]

    # Combining date and time of cur_df 
    cur_df['date_time'] = cur_df.date + " " + cur_df.time

    # Converting date to pandas datetime format
    cur_df.date_time = pd.to_datetime(cur_df.date_time)

    # Creating columns date_year, date_month, date_weekday, hour
    cur_df['date_year'] = cur_df.date_time.dt.year
    cur_df['date_month'] = cur_df.date_time.dt.month_name()
    cur_df['date_weekday'] = cur_df.date_time.dt.day_name()
    cur_df['hour'] = cur_df.date_time.dt.hour

    # converting all date columns to pandas datetime format
    cur_df['start_date'] = pd.to_datetime(cur_df['start_date'])
    cur_df['end_date'] = pd.to_datetime(cur_df['end_date'])
    cur_df['created_at'] = pd.to_datetime(cur_df['created_at'])
    cur_df['updated_at'] = pd.to_datetime(cur_df['updated_at'])

    # droping date and time
    cur_df = cur_df.drop(columns=['date', 'time'])

    # Changing datatype of cohort_id and program_id
    cur_df.cohort_id = cur_df.cohort_id.astype('int64')
    cur_df.program_id = cur_df.program_id.astype('int64')

    # Turn weekday into ordered category
    cur_df.date_weekday = pd.Categorical(cur_df.date_weekday, categories = ['Sunday', 'Monday', 'Tuesday', 
                                                               'Wednesday', 'Thursday', 'Friday', 'Saturday'], ordered = True)
    return cur_df
                                         
def add_course_names():
    '''This function creates a dictionary with the Codeup course 
    information and concatenates it with the cur_df dataframe'''

        # Creating a dataframe with the course names:
    courses = pd.DataFrame({'id': [1, 2, 3, 4], 
                       'course_name': ['PHP Full Stack Web Dev', 'Java Full Stack Web Dev', 'Data Science', 'Front End Web Dev'],
                       'course_subdomain': ['php', 'java', 'ds', 'fe']})

        # Getting the cur_df files:
    cur_df = pd.read_csv('curriculum_logs.csv')

        # Adding the course names to the cur_df files:
    cur_df = cur_df.merge(courses, how='left', left_on='program_id', right_on='id')

    return cur_df                                         