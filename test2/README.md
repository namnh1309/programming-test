Bài 2: Xây dựng hệ thống điều khiển các server qua Email, yêu cầu đảm bảo bảo mật, hiệu năng tốt.
Flow mong muốn:
Sysadmin gửi mail đến hệ thống, trong mail chứa các info: câu lệnh cần chạy, chạy trên các server nào, xác thực, v.v..
Hệ thống nhận mail, phân tích, chạy lệnh trên các server yêu cầu, nhận lại output, gửi lại output cho Sysadmin qua email.
Yêu cầu:
1. Thiết kế sơ đồ các thành phần hệ thống, công nghệ sử dụng, phương thức giao tiếp,...
2. Code 1-2 thành phần critical trong hệ thống.

##Lời giải
###Thiết kế
```
+-------------+           +----------+       +-----------+
|             |           |          |       |           |
| Mail Server |           |Server 1  <-----+ | Server 2  ^
|             |           |          |     | |           |
+-----+---+---+           +-----+----+     | +------+---^+
  get |   ^                     |          |        |   |
  mail|   |send                 |          |        |   |
      |   |output of command    |          |        |   |
  +-------------------------------------------------------------+
  |   |   |     +----------+    |          |        |   |       |
  |   |   |     |          |    |          |        |   |       |
  |   |   +-----+  Deamon  |    |result    |call    |   |       |
  |   +--------->          |    |          |command |   |       |
  |             +--+--+-+-^+    |          |        |   |       |
  |                |  | | |     |          |        |   |       |
  |   +----------+ |  | | result|        +-+^-------v-+ |       |
  |   |Database  <-+  | | |     +-------->            | |       |
  |   |  User    +----+ | +--------------|  Satlstack +-+       |
  |   +----------+      +---------------->            |         |
  |                      call command    +------------+         |
  |                                                             |
  |   Master Server                                             |
  +-------------------------------------------------------------+
```

