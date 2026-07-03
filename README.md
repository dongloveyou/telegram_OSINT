
# 🕵️‍♂️ telegram_OSINT

Công cụ hỗ trợ thu thập và phân tích thông tin tình báo nguồn mở (OSINT) trên nền tảng Telegram, tối ưu hóa để chạy mượt mà trên môi trường **Termux (Android)** và Linux.

---

## 🚀 Hướng dẫn cài đặt nhanh (All-in-One)

Để đơn giản hóa quá trình cài đặt, toàn bộ các gói hệ thống (`clang`, `git`, `python`...) và các thư viện Python (`telethon`, `pyrogram`...) đã được gộp chung vào một file cấu hình tự động.

Bạn chỉ cần mở **Termux** lên và copy-paste dòng lệnh duy nhất sau đây:

```bash
pip install -r requirements.txt

bash
git clone https://github.com/dongloveyou/telegram_OSINT.git
cd telegram_OSINT


📱 Hướng dẫn cài đặt telegram_OSINT trên Termux (Android)
Để chạy công cụ này trên điện thoại, bạn cần cài đặt ứng dụng Termux (khuyến nghị tải bản mới nhất từ F-Droid hoặc GitHub, không nên tải từ Google Play vì bản trên đó đã cũ và bị lỗi).
Bước 1: Cập nhật hệ thống Termux
Mở Termux lên và chạy lệnh sau để cập nhật danh sách gói phần mềm hệ thống:
bash
pkg update && pkg upgrade -y
bash
pkg install git python -y

bash
git clone https://github.com/dongloveyou/telegram_OSINT.git
bash
pip install -r requirements.txt
python main.py

