# v1 创建新列表，遍历最小值添加到新列表
def select_sort_simple(li):
    li_new = []
    for i in range(len(li)):
        min_val = min(li)
        li_new.append(min_val)
        li.remove(min_val)
    return li_new


li = [3, 9, 2, 4, 1, 5, 6, 8, 7, 9]
print(select_sort_simple(li))

print("")

# v2 无需创建新列表，最小值添加到第一位
def select_soart(li):
    for i in range(len(li) - 1):
        min_loc = i
        for j in range(i + 1, len(li)):
            if li[j] < li[min_loc]:
                min_loc = j
        li[i], li[min_loc] = li[min_loc], li[i]
        print(li)


li = [3, 2, 9, 4, 1, 5, 6, 8, 7, 9]
print(li)
select_soart(li)
