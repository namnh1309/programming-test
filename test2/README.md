##Bài 2: Xây dựng hệ thống điều khiển các server qua Email, yêu cầu đảm bảo bảo mật, hiệu năng tốt.
Flow mong muốn:

Sysadmin gửi mail đến hệ thống, trong mail chứa các info: câu lệnh cần chạy, chạy trên các server nào, xác thực, v.v..
Hệ thống nhận mail, phân tích, chạy lệnh trên các server yêu cầu, nhận lại output, gửi lại output cho Sysadmin qua email.

Yêu cầu:

1. Thiết kế sơ đồ các thành phần hệ thống, công nghệ sử dụng, phương thức giao tiếp,...

2. Code 1-2 thành phần critical trong hệ thống.

##Lời giải
###Thiết kế
```
                          1
      +------------------------------------------+
      |                                          |
      |                                          |
      |                                          |
+-----+-----+                                    |       +-----------+     +----------+
|           |                                    |       |           |     |          |
|   Mail    |                                    |       |  Server 1 |     | Server 2 |
|  Server   |                                    |       |           |     |          |
|           |                                    |       |           |     |          |
+----^------+                                    |       +-----+---^-+     +-+-^------+
     |                                           |             |   |         | |
     |                                           |            8|   |         | |
     |                                           |             |   |         | |
     |     +--------------------------------------------------------------------------+
     |     |                                     |             |   |         | |      |
     |     |                              +------v----+        |   |         | |      |
     +-------------------10---------------+           |        |   |         | |      |
           |                              |   Deamon  <---+    |   | 7       | |      |
           |      +-------------3--------->           +-+ |    |   |         | |      |
           |      |                       ++-+---^----+ | |9   |   |         | |      |
           |    +-+-----------------+      | |   5      | |   +v---+---------v-++     |
           |    |                   <--2---+ |4  |      | |   |  Send command   |     |
           |    |  User Database    |     +--v---+----+ | |   |                 |     |
           |    |      and          |     |           | | |   |                 |     |
           |    |  Authentication   |     |   Host    | | +----                 |     |
           |    |                   |     |   Config  | |     |                 |     |
           |    +-------------------+     +-----------+ |     +--------^--------+     |
           |                                            6              |              |
           |                                            |              |              |
           |                                            +--------------+              |
           |               Master Server                                              |
           |                                                                          |
           |                                                                          |
           +--------------------------------------------------------------------------+
           
```

Hoạt động trên Master Server

```
        +------------------+
        |                  |
        |       Master     |
        |       Server     |
        +-+----^-----------+
          |    |
          |    |
         7|    |8
          |    |
+----------------------------------------------+
|         |    |                               |
|         |    |                               |
|    +----v----+--+  11    +--------------+    |
|    |            +-------->      Runing  |    |
|    | Receive    |   12   |      command |    |
|    | Command    <--------+              |    |
|    +------------+        +--------------+    |
|                                              |
|                                              |
|                                              |
|                                              |
|                     Slave Server             |
+----------------------------------------------+
```
Hoạt động trên Slave Server

###Mô tả thiết kế

####Các thành phần

#####Trên Master Server

* Mail Server: Nơi nhận mail điều khiển của system admin 
* Master Server: Nơi chứa chương trình thực hiên tác vụ điều khiển các server
con
* Deamon: Chương trình chạy ngầm kiểm tra xem có email điều khiển của sysadmin
hay ko, nếu có thì sẽ đọc dữ liệu từ mail và sẽ gọi các thành phần khác để thực
thi email điều khiển của sysadmin.
* User Database and Authentication: là thành phần thực hiện tác vụ kiểm tra tính
xác thực của sysadmin và dữ liệu trong email, quyền của sysadmin đối với server
muốn chạy lệnh
* Host Config: là một thành phần thao tác với 1 file cấu hình cho các Slave Server
chụi sự điều khiển của Master Server
* Send command: là gửi lệnh đến các Slave Server để service trên Slave Server thực thi

* Server 1, Server 2 là các server được điều khiển bởi Master server

#####Luồng chạy chương trình

1. Deamon kiểm tra xem có mail điều khiển của sysadmin không, nếu có thì sẽ lấy
các dữ liệu về sysamin( tên, mã xác thực), lệnh muốn thực thi và tên server muốn
thực thi lện đó.

2. Phần User Database and Authentication được gọi để kiểm tra tính xác thực của
sysadmin nếu sysadmin được xác thực thì sẽ kiểm tra xem có quyền với server
muốn thực thi hay không.

3. Dữ liệu trả về xem sysadmin có được xác thực hay không.

4. Nếu các thông tin đã được xác thực thì phần Host config sẽ được gọi để lấy
thông tin về server cần chạy lệnh như địa chỉ IP

5. Thông tin được trả về deamon

6. Câu lệnh cần chạy cùng thông tin server được gửi cho Send Command

7. Send Command nhận được lệnh cùng địa chỉ IP thì sẽ gửi câu lệnh đến Server
con

8. Slave Server nhận được câu lệnh sẽ chạy lệnh đó và trả vè kết quả cho send command

9. Kết quả đươc send command nhận và gửi lại cho deamon.

10. Deamon nhận được kết quả sẽ gửi lại mail kết quả chạy tới mail server vào
địa chỉ của sysadmin gửi yêu cầu chạy lệnh

####Trên Slave Server

#####Các thành phần

* Receive Command: nhận command từ Master Server
* Run Command: thực thi command trên Slave Server

######Luồng chạy chương trình

7. Receive Command nhận command từ Master Server tương gửi bởi Send Command
11. Receive Command gửi command đến Run Command
12. Run Command nhận được lệnh và thực thi lệnh đó rồi gửi kết quả thực thi lệnh
về Receive Command
8. Receive Command chuyển tiếp kết quả thực thi lệnh về Master Server

###Demo(code 1-2 thành phần cơ bản)

