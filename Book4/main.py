li1: list = ["shamim", "surma", "sadhin", "tamanna", "taiba"]

ordered_list: list = list(enumerate(li1, start=1))
# print(ordered_list)

for item in enumerate(li1):
    # print(item)
    pass
another_list = [x for x in zip(li1, ordered_list)]
# print(another_list)

# print(ordered_list.__len__())
# print(ordered_list.__repr__())
import os


core = os.cpu_count()
print(core, os.terminal_size, os.times(), os.path)
print(dir(os))
