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
