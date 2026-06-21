def count_matching_elements(mat: list, e: int):
    c=0
    for arr in mat:
        for i in arr:
            if i==e:
                c+=1
    return c