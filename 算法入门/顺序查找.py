"""
输入：列表，待查找元素
输出：元素下标（未找到时一般返回None或-1）
"""


def linear_search(li, val):
    for ind, v in enumerate(li):
        if v == val:
            return ind
    else:
        return None


li = [-1, 0, 3, 5, 9, 12]
val = 9

print(list(enumerate(li)))
print(linear_search(li, val))

"""
>>> seasons = ['Spring', 'Summer', 'Fall', 'Winter']
>>> list(enumerate(seasons))
[(0, 'Spring'), (1, 'Summer'), (2, 'Fall'), (3, 'Winter')]
>>> list(enumerate(seasons, start=1))       # 下标从 1 开始
[(1, 'Spring'), (2, 'Summer'), (3, 'Fall'), (4, 'Winter')]
"""
