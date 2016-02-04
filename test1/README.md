#Bài 1: Cho 1 tháp dãy số có dạng như sau:
```
3
2 6
5 4 6
4 8 2 5
```

Tìm đường đi từ đỉnh tháp xuống chân tháp sao cho tổng bình phương các số trên đường đi là lớn nhất. (Tại hàng tiếp theo chỉ được rẽ phải hoặc rẽ trái 1 đơn vị, nói khác đi là chỉ đc đi theo số gần kề với nó)
(Với tháp ví dụ như trên thì đường đi tối ưu là: `3 - 6 - 4 - 8, vì 3^2 + 6^2 + 4^2 + 8^2 là lớn nhất`)

Input: là file input.txt được viết theo dạng:
```
3
2 6
5 4 6
4 8 2 5
```

Output: ra file `output.txt` là dãy đường đi từ đỉnh đến đáy sao cho tổng bình phương các số trên đường đi là lớn nhất:
`3 6 4 8`
(Yêu cầu ko dùng giải thuật vét cạn)
##Lời giải
Dùng phương pháp "Dynamic Programming"

Ta duyệt ngược file input.txt từ dòng cuối cùng lên trên đến dòng đầu tiên,
giả sử file input.txt có n dòng, lần đầu duyệt dòng n ta không làm cả mà lưu lại
đến dòng n-1 ta tính toán để tìm xem với mỗi số trên dòng n-1 ta sẽ tìm dường
lớn nhất đi xuống dòng n, sau đó lưu lại các giá trị mà đường đi lớn nhất từ phần tử
đó xuống dòng dưới tạo ra. Sau đó ta sẽ có 1 dãy các giá trị lớn nhất mà các phần
tử tại dòng n-1 đi xuống dòng n có thể tạo ra. Sử dụng dãy giá trị mới tạo ra làm
dòng n-1 áp dụng phương pháp dùng cho dòng n-1 và n cho dòng n-2 và n-1(chú ý
dòng n-1 là dòng mới được tạo). Tiếp tục làm như vậy cho đến khi duyệt qua hết
dòng 1, khi đó giá trị của phần tử được tạo ra sẽ là giá trị do đường đi lớn nhất
theo luật của bài đề ra. 
```
ví dụ

5 4 6
4 8 2 5

từ phần tử 5 xuống dòng dưới để đạt được giá trị lớn nhất theo luật của đề bài
ta phải xuống phần tử 8 tại dòng dưới giá trị của đường đi lớn nhất này tạo
ra là 5^2 + 8^2 = 25 + 64 = 89. Làm lần lượt với các phần tử còn lại (với 4 là
8, với 6 là 5). Ta có dãy các giá trị lớn nhất

89 80 61

lấy dãy giá trị trên làm dòng thay thế cho dòng

5 4 6

tiếp tục duyệt lên trên cho đến khi kết thúc ta sẽ tìm được giá trị mà đường
đi lớn nhất tạo ra.
```

Phương pháp trên chỉ đưa ra giá trị lớn nhất còn để tìm ra đường đi ta cần lưu
lại các vị trị phần tử ở dòng n mà phần tử từ dòng n-1 đi xuống sẽ cho giá trị
lớn nhất, làm như vậy khi duyệt các dòng khác, sau khi duyệt hết dòng 1 ta sẽ
có đường đi cho ta giá trị lớn nhất.

##Chạy chương trình
cần chạy lệnh
```
./test1.py ten_file_chua_cau_truc_tam_giac
```

kết quả đường đi cho giá trị lớn nhất được ghi ra file mặc định là `output.txt`

hoặc
```
./test1.py
```
file mặc định chứa cấu trúc tam giác mà chương trình đọc sẽ là `input.txt`
