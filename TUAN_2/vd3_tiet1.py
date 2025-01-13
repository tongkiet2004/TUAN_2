def binary_search(arr, target):
    left, right = 0, len(arr) - 1  # Thiết lập phạm vi tìm kiếm
    while left <= right:
        mid = (left + right) // 2  # Tính chỉ số giữa
        if arr[mid] == target:
            return mid  # Tìm thấy mục tiêu
        elif arr[mid] < target:
            left = mid + 1  # Tìm nửa phải
        else:
            right = mid - 1  # Tìm nửa trái
    return -1  # Nếu không tìm thấy

arr = [1, 3, 5, 7, 9, 11]
print(binary_search(arr, 7))  # Output: 3 (chỉ số của 7 trong mảng)
