#正则表达式
import re

def get_num(input):
    nums = re.findall(r'\d+', input)
    return nums[0]