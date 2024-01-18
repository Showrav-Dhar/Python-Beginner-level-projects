# Mean, Median and Mode are the fundamentals of statistics.
# They are used in almost every domain where we deal with numbers.

# sample dataset - 12 16 20 20 12 30 25 23 24 20
# mean = 20.2 [ average value of a dataset ]
# median = 20.2 [ mid value of a dataset ]
# mode = 20 [ the most frequent value in a dataset ]


# Mean
# The mean is the average value of all the values in a dataset.

print("Enter the dataset")
li = list(map(int, input().split()))    # take a whole list as input
mean = sum(li) / len(li)
print(f"The mean of the dataset = {mean}")

# Median
# The Median is the middle value among all the values in sorted order.
# when the total number of values is even: Median  = [(n/2)th term + {(n/2)+1}th]/2
# when the total number of values is odd: Median = {(n+1)/2}th term

# here the divisions for detecting index should be integer division always
li.sort()
if len(li) % 2 == 0:
    m1 = li[len(li) // 2]
    m2 = li[len(li) // 2 - 1]
    print(f"Median of the dataset = {(m1 + m2) / 2}")
else:
    a = len(li) // 2
    median = li[a]
    print(f"Median of the dataset = {median}")

# Mode
# Mode is the most frequently occurring value among all the values.
# Below is how we can calculate the mode value of a dataset using Python:

li.sort()  # sorted the dataset
mx = -1
mode = 0
for i in li:
    a = li.count(i)  # counting how many times a item is present in the dataset
    if a > mx:
        mx = a
        mode = i

print(f"Mode of the dataset = {mode}")
