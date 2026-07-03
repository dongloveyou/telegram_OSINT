
# 🕵️‍♂️ telegram_OSINT

Công cụ hỗ trợ thu thập và phân tích thông tin tình báo nguồn mở (OSINT) trên nền tảng Telegram, tối ưu hóa để chạy mượt mà trên môi trường **Termux (Android)** và Linux.

---

## 🚀 Hướng dẫn cài đặt nhanh (All-in-One)

Để đơn giản hóa quá trình cài đặt, toàn bộ các gói hệ thống (`clang`, `git`, `python`...) và các thư viện Python (`telethon`, `pyrogram`...) đã được gộp chung vào một file cấu hình tự động.

Bạn chỉ cần mở **Termux** lên và copy-paste dòng lệnh duy nhất sau đây:

```bash
pkg update && pkg upgrade -y && pkg install git -y && git clone

[https://github.com/dongloveyou/telegram_OSINT.git]

(https://github.com/dongloveyou/telegram_OSINT.git) && cd telegram_OSINT && chmod +x setup.sh && ./setup.sh


================≠=============
khởi chạy cấp quyền 
chmod +x setup.sh
./setup.sh
chạy tool
python main.py
