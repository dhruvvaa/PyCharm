rainfall = [68, 58, 0, 99, 200, 39, 73, 43, 68, 0, 19]

min_r = min(rainfall)
max_r = max(rainfall)
avg = sum(rainfall)/len(rainfall)

print("Minimun Rainfall: ", min_r)
print("Maximum Rainfall: ", max_r)
print("Average Rainfall: ", avg)
print(sorted(rainfall))