# result = 0

# for i in range(1, 1001):
#     # print('current number to be added:', i)
#     result = result + i
#     # print('new result after this iteration:', result)

# print('The final result:', result)


# result = 0

# for i in range(1, 1001):
#     if i % 2 == 0:
#         result = result + i

# print('The sum of odd numbers is', result)


# result = 0

# for i in range(1, 1001, 2):
#     result = result + i

# print('The sum of odd numbers is', result)


# result = 1

# for i in range(1, 11):
#     result = result * i

# print('The factorial of 10 is', result)

# import time


# def countdown(n):
#     while n > 0:
#         print(n)
#         time.sleep(1)
#         n = n-1
#     print('Blastoff!')


# countdown(5)


# iteration = 0

# while iteration < 5:
#     count = 0
#     # the variable 'letter' in the loop stands for every
#     # character, including spaces and commas!
#     for letter in "hello, world":
#         count += 1
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1


# iteration = 0
# while iteration < 5:
#     count = 0
#     for letter in "hello, world":
#         count += 1
#         if iteration % 2 == 0:
#             break
#     print("Iteration " + str(iteration) + "; count is: " + str(count))
#     iteration += 1


# while True:
#     print('press "q" to quit')
#     line = input('> ')
#     if line == 'q':
#         break
#     print(line)

# print('Done!')


mysum = 0
for i in range(5, 11, 2):
    mysum += i
    if mysum == 5:
        break
print(mysum)
