#excuton time in python 
import statistics
import time
start_time =time.time()

data =[200000,50000,600000,43793330,230000,345000,]
mean_value=statistics.mean(data)
median_value =statistics.median(data)
mode_value =statistics.mode(data)

print(f"Mean:{mean_value}")
print(f"Median: {median_value}")
print(f"Mode: {mode_value}")

end_time =time.time()
total_time = end_time - start_time
print(f"Total  time taken :{total_time} in seconds")