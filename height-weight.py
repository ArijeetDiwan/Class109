import plotly.figure_factory as ff
import pandas as pd
import csv

import random
import plotly.express as px

import statistics

df=pd.read_csv("D:/python/class109/height-weight.csv")


height_list=df["Height(Inches)"].tolist()
weight_list=df["Weight(Pounds)"].tolist()

height_mean=statistics.mean(height_list)
weight_mean=statistics.mean(weight_list)

height_median=statistics.median(height_list)
weight_median=statistics.median(weight_list)


height_mode=statistics.mode(height_list)
weight_mode=statistics.mode(weight_list)

height_std_deviation=statistics.stdev(height_list)
weight_std_deviation=statistics.stdev(weight_list)

print("Mean,Median and Mode of Height is {} ,{} and {} respectively".format(height_mean,height_median,height_mode))
print("Mean,Median and Mode of Weight is {} ,{} and {} respectively".format(weight_mean,weight_median,weight_mode))
print("std deviation of height data :",height_std_deviation)
print("std deviation of weight data :",weight_std_deviation)

first_std_deviation_start, first_std_deviation_end = height_mean-height_std_deviation, height_mean+height_std_deviation
second_std_deviation_start, second_std_deviation_end = height_mean-(2*height_std_deviation), height_mean+(2*height_std_deviation)
third_std_deviation_start, third_std_deviation_end = height_mean-(3*height_std_deviation), height_mean+(3*height_std_deviation)

list_of_data_within_1_std_deviation = [result for result in height_list if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in height_list if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in height_list if result > third_std_deviation_start and result < third_std_deviation_end]


print("{}% of data lies within 1 standard deviation of height".format(len(list_of_data_within_1_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within 2 standard deviations of height".format(len(list_of_data_within_2_std_deviation)*100.0/len(height_list)))
print("{}% of data lies within 3 standard deviations of height".format(len(list_of_data_within_3_std_deviation)*100.0/len(height_list)))


fig=ff.create_distplot([df["Height(Inches)"].tolist()],["Height"],show_hist=False)

#y axis can be anystring  ex: "Height" is taken here..
#you can take "abc" or "xyz"
#frequency shows in y axis(out of 1)--its the probablity of that data
fig.show()