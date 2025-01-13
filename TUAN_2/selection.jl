function selection_sort!(arr)  # Hàm sắp xếp
    n = length(arr)  # Sửa cú pháp
    for i in 1:(n-1)  # Vòng lặp
        min_index = i  # Sửa giá trị min_index
        for j in (i+1):n  # Sửa vòng lặp
            if arr[j] < arr[min_index]  # Điều kiện so sánh
                min_index = j  # Cập nhật min_index
            end
        end
        if min_index != i  # Hoán đổi nếu cần
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Hoán đổi
        end
    end
    return arr  # Trả về mảng đã sắp xếp
end

# Kiểm tra ví dụ
arr = [5, 2, 9, 1, 5]
selection_sort!(arr)  # Gọi hàm sắp xếp
println("Kết quả sau Selection Sort: ", arr)  # In kết quả
