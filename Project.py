import pandas as pd
import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics

df = pd.read_csv('data.csv')
scores = df['math score'].tolist()

mean_ = statistics.mean(scores)
median_ = statistics.median(scores)
mode_ = statistics.mode(scores)
stdev_ = statistics.stdev(scores)

print(f'Mean: {mean_}')
print(f'Median: {median_}')
print(f'Mode: {mode_}')
print(f'Standard Deviation: {stdev_}')

# get percent of values between 1st standard deviation
count = 0
for score in scores:
    if score > mean_ - stdev_ and score < mean_ + stdev_:
        count += 1
_1perc = (count / len(scores))*100
print('1st Standard Deviation:', _1perc, '%')

# get percent of values between 2nd standard deviation
count = 0
for score in scores:
    if score > mean_ - (stdev_ * 2) and score < mean_ + (stdev_ * 2):
        count += 1
_2perc = (count / len(scores))*100
print('2nd Standard Deviation:', _2perc, '%')

# get percent of values between 3rd standard deviation
count = 0
for score in scores:
    if score > mean_ - (stdev_ * 3) and score < mean_ + (stdev_ * 3):
        count += 1
_3perc = (count / len(scores))*100
print('3rd Standard Deviation:', _3perc, '%')

stdev1_start,stdev1_end = mean_ - stdev_,mean_ + stdev_
stdev2_start,stdev2_end = mean_ - 2 * stdev_,mean_ + 2 * stdev_
stdev3_start,stdev3_end = mean_ - 3 * stdev_,mean_ + 3 * stdev_


figure = ff.create_distplot([scores],["Result"],show_hist = False)

figure.add_trace(go.Scatter(x=[mean_,mean_],y=[0,0.17],mode = "lines",name = "Standard Deviation"))
figure.add_trace(go.Scatter(x=[stdev1_start,stdev1_start],y=[0,0.17],mode = "lines",name = "Standard Deviation 1 Start"))
figure.add_trace(go.Scatter(x=[stdev1_end,stdev1_end],y=[0,0.17],mode = "lines",name = "Standard Deviation 1 End"))
figure.add_trace(go.Scatter(x=[stdev2_start,stdev2_start],y=[0,0.17],mode = "lines",name = "Standard Deviation 2 Start"))
figure.add_trace(go.Scatter(x=[stdev2_end,stdev2_end],y=[0,0.17],mode = "lines",name = "Standard Deviation 2 End"))
figure.add_trace(go.Scatter(x=[stdev3_start,stdev3_start],y=[0,0.17],mode = "lines",name = "Standard Deviation 3 Start"))
figure.add_trace(go.Scatter(x=[stdev3_end,stdev3_end],y=[0,0.17],mode = "lines",name = "Standard Deviation 3 End"))

figure.show()