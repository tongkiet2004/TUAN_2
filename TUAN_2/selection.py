def selection_sort(arr):
    n = len(arr)  # Sửa cú pháp
    for i in range(n - 1):  # Sửa vòng lặp
        min_index = i  # Sửa cú pháp
        for j in range(i + 1, n):  # Sửa vòng lặp
            if arr[j] < arr[min_index]:  # Điều kiện so sánh
                min_index = j  # Sửa giá trị min_index
        if min_index != i:  # Hoán đổi nếu cần
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Hoán đổi

if __name__ == "__main__":  # Kiểm tra tên file
    arr = [5, 2, 9, 1, 5]  # Khai báo mảng đúng
    selection_sort(arr)  # Gọi hàm sắp xếp
    print("Kết quả sau Selection Sort:", arr)  # In kết quả
