Kho lưu trữ telegram_OSINT chứa công cụ hỗ trợ thu thập và phân tích thông tin tình báo nguồn mở (OSINT) trên nền tảng Telegram

Thu thập thông tin từ tài khoản, nhóm (Groups) hoặc kênh (Channels) công khai.
Phân tích dữ liệu, lịch sử tin nhắn hoặc các siêu dữ liệu (metadata) liên quan.

Hướng dẫn cài đặt 
Đảm bảo hệ thống của bạn đã cài đặt Python 3.8+ (Khuyến nghị sử dụng các bản phân phối Linux như Kali Linux hoặc cài đặt Python trên Windows)



§cài đặt gói phụ thuộc 

pip install -r requirements.txt
 
python main.py

§ Hướng dẫn cài đặt telegram_OSINT trên Termux (Android)
Để chạy công cụ này trên điện thoại, bạn cần cài đặt ứng dụng Termux (khuyến nghị tải bản mới nhất từ F-Droid hoặc GitHub, không nên tải từ Google Play vì bản trên đó đã cũ và bị lỗi
pkg update && pkg upgrade -y

pkg install git python -y


git clone https://github.com/dongloveyou/telegram_OSINT.git

cd telegram_OSINT
pip install -r requirements.txt
python main.py
