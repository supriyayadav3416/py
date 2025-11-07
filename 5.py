import numpy as np
data = np.array([10,20,30,40,50])
mean_value = np.mean(data)
median_value = np.median(data)
std_dev = np.std(data)
print(f"mean = {mean_value}")
print(f"median = {median_value}")
print(f"std = {std_dev}" )

data_set1 = np.array([1,2,3,4,5])
data_set2 = np.array([10,20,30,40,50])
corr_coef = np.corrcoef(data_set1,data_set2)[0,1]
print("correlation coefficient = ",{corr_coef})
