#include <iostream>
#include <vector>
using namespace std;

// Hàm Selection Sort
void selectionSort(vector<int>& arr) {
    int n = arr.size();  // Sửa cú pháp
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i;  // Sửa lỗi ở đây, minIndex cần khởi tạo bằng i
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;  // Sửa cú pháp
            }
        }
        // Hoán đổi nếu minIndex khác i
        if (minIndex != i) {
            int temp = arr[i];  // Sửa cú pháp
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }
}

int main() {
    vector<int> arr = {15, 2, 9, 1, 5};  // Sửa cú pháp khai báo mảng
    selectionSort(arr);  // Gọi hàm sắp xếp

    cout << "Ket qua sau Selection Sort: ";  // Sửa dấu <<
    for (int x : arr) {
        cout << x << " ";  // Sửa dấu <<
    }
    cout << endl;  // Dòng mới
    return 0;
}
