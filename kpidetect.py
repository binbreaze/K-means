import pandas as pd
import numpy as np

def read_data(file):

    dataset = pd.read_csv(file,)
    return dataset
file = 'D:\\taocloud\csvfile\cpu\cpu_xdfs7_cpu0_2019-08-22T00_00_00Z_pred.csv'
dataset = read_data(file)
dataset = dataset.ix[:,['time','mean_usage_idle','mean_usage_system']]
# print(dataset.head())

usage_idle = dataset['mean_usage_idle']

