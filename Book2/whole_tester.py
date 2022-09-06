import re
#  +8801612 8798881 +88016128798882
numbers = "+88016128798888"
result = re.findall(r'^(\+8801)[3456789]{1}(\d){8}$', numbers)

print(result)