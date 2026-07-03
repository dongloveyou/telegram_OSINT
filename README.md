công cụ telegram_OSINT chứa công cụ hỗ trợ thu thập và phân tích thông tin tình báo nguồn mở (OSINT) trên nền tảng Telegram, được viết bằng ngôn ngữ
Python.
Thu thập thông tin từ tài khoản, nhóm (Groups) hoặc kênh (Channels) công khai.
Phân tích dữ liệu, lịch sử tin nhắn hoặc các siêu dữ liệu (metadata) liên quan.
Hướng dẫn cài đặt 
git clone https://github.com/dongloveyou/telegram_OSINT.git
cd telegram_OSINT
pip install -r requirements.txt
Cấu hình API Telegram (Quan trọng)
Để công cụ hoạt động và kết nối được với Telegram, bạn cần chuẩn bị:
Truy cập vào trang my.telegram.org và đăng nhập tài khoản của bạn.
Tạo một ứng dụng mới để lấy thông tin api_id và api_hash.
Cấu hình các thông số này vào file cấu hình (nếu có) hoặc nhập trực tiếp khi công cụ yêu cầu khởi chạy.
4. Khởi chạy công cụ
Mở terminal tại thư mục dự án và chạy file chính main.py:
python main.py
hướng dẫn cài đặt trên termux 
Để chạy công cụ này trên điện thoại, bạn cần cài đặt ứng dụng Termux (khuyến nghị tải bản mới nhất từ F-Droid hoặc GitHub, không nên tải từ Google Play vì bản trên đó đã cũ và 
bị lỗi).
pkg 

