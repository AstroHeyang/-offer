# python方法
def replace_space_py(s: str) -> str:
    if not s:
        return
    list_str = s.split()
    return '%20'.join(list_str)


# 通用方法
def replace_space(s: str) -> str:
    if not s:
        return
    count_blank = 0
    for char in s:
        if char == ' ':
            count_blank += 1
    len_res = len(s) + 2*count_blank
    res = ['']*len_res
    i, j = 0, 0
    while i < len(s) and j < len_res:
        if s[i] == ' ':
            res[j] = '%'
            res[j+1] = '2'
            res[j+2] = '0'
            j += 3
        else:
            res[j] = s[i]
            j += 1
        i += 1

    return ''.join(res)

