heights = []

f = open("test_numbers.txt", "r")
for line in f.readlines():
    fields = list(line.strip())
    heights.append(fields)

my_list = []
for h in range(len(heights)):
    height_ints = map(int, heights[h])
    my_list.append(list(height_ints))
print(my_list)

