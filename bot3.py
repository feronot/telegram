import time

with open('fetch.txt') as f:
    for line in f:
        print(line)
        time.sleep(0.3)

# with open('fetch.txt') as f:
#     line = f.readline()
#     while line:
#         line = f.readline()
#         print(line)
#         time.sleep(0.3)

# with open('fetch.txt') as f:
#     contents = f.read()
#     print(contents)
#     time.sleep(0.3)



# lines = []
# with open('fetch.txt') as f:
#     lines = f.readlines()
#
# count = 0
# for line in lines:
#     count += 1
#     print(f'line {count}: {line}')
#     time.sleep(0.1)

