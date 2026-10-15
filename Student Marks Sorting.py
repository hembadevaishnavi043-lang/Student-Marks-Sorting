
def merge_sort(marks):
    if len(marks) <= 1:
        return marks

    mid = len(marks) // 2

    left = merge_sort(marks[:mid])
    right = merge_sort(marks[mid:])

    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[i:])

    return result


marks = [78, 45, 90, 62, 85]

print("Original Marks:", marks)
print("Sorted Marks:", merge_sort(marks))
