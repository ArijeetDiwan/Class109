import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics


dice_result=[]
count=[]

#we want to roll the dice 100 times 
for i in range (0,10000232):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    dice_result.append(dice1+dice2)
    count.append(i)


mean=sum(dice_result)/len(dice_result)

sd=statistics.stdev(dice_result)
mode=statistics.mode(dice_result)
median=statistics.median(dice_result)

print("mean of the data is ",mean)
print("mode of the data is ",mode)
print("median of the data is ",median)

print("sandard deviation of the data is ",sd)

first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-2*sd,mean+2*sd
third_sd_start,third_sd_end=mean-3*sd,mean+3*sd



list_of_data_within_1_std_deviation = [result for result in dice_result if result > first_sd_start and result < first_sd_end]
list_of_data_within_2_std_deviation = [result for result in dice_result if result > second_sd_start and result < second_sd_end]
list_of_data_within_3_std_deviation = [result for result in dice_result if result > third_sd_start and result < third_sd_end]


print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 2 standard deviations".format(len(list_of_data_within_2_std_deviation)*100.0/len(dice_result)))
print("{}% of data lies within 3 standard deviations".format(len(list_of_data_within_3_std_deviation)*100.0/len(dice_result)))


fig=ff.create_distplot([dice_result],["Result"],show_hist=False)
fig.show()
