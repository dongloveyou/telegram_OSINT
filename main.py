# -*- coding: utf-8 -*-
import os
import sys
import asyncio
from datetime import datetime
from telethon import TelegramClient

# Thêm thư mục modules vào hệ thống tìm kiếm tệp tin
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

from database import database_yarat
import osint_actions

SESSION_NAME = 'tg_osint_expert'

def get_time_color():
    """Trả về mã màu ANSI tương ứng với các khung giờ trong ngày"""
    hour = datetime.now().hour
    
    # Mã màu ANSI định dạng chuẩn
    RESET = "\033[0m"
    
    if 5 <= hour < 12:      # Sáng: Màu Vàng ánh bình minh
        return "\033[1;33m", "BUỔI SÁNG (Morning Mode)" + RESET
    elif 12 <= hour < 17:    # Chiều: Màu Xanh Dương năng động
        return "\033[1;34m", "BUỔI CHIỀU (Afternoon Mode)" + RESET
    elif 17 <= hour < 22:    # Tối: Màu Tím hoàng hôn / huyền bí
        return "\033[1;35m", "BUỔI TỐI (Evening Mode)" + RESET
    else:                    # Đêm (22h - 4h sáng): Màu Đỏ cảnh báo / chuyên gia đêm
        return "\033[1;31m", "BAN ĐÊM (Night-Owl Mode)" + RESET

def clear_screen():
    """Xóa màn hình tương thích Windows, Linux, Android (Termux)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    clear_screen()
    color_code, mode_name = get_time_color()
    reset_code = "\033[0m"
    
    # Logo gốc của bạn được bọc trong mã màu động
    banner = f"""{color_code}
███████ ██ ██      ██    ██ ███████ ██████  ████████  ██████   ██████  ███████ ██ ███    ██ ████████ 
██      ██ ██      ██    ██ ██      ██   ██    ██    ██       ██    ██ ██      ██ ████   ██    ██    
███████ ██ ██      ██    ██ █████   ██████     ██    ██   ███ ██    ██ ███████ ██ ██ ██  ██    ██    
     ██ ██ ██       ██  ██  ██      ██   ██    ██    ██    ██ ██    ██      ██ ██ ██  ██ ██    ██    
███████ ██ ███████   ████   ███████ ██   ██    ██     ██████   ██████  ███████ ██ ██   ████    ██    

⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⣿⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣿⣿⡿⠿⠛⢙⣿⣿⠃
⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣶⣾⣿⣿⠿⠛⠋⠁⠀⠀⠀⣸⣿⣿⠀
⠀⠀⠀⠀⣀⣤⣴⣾⣿⣿⡿⠟⠛⠉⠀⠀⣠⣤⠞⠁⠀⠀⣿⣿⡇⠀
⠀⣴⣾⣿⣿⡿⠿⠛⠉⠀⠀⠀⢀⣠⣶⣿⠟⠁⠀⠀⠀⢸⣿⣿⠀⠀
⠸⣿⣿⣿⣧⣄⣀⠀⠀⣀⣴⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⣼⣿⡿⠀⠀
⠀⠈⠙⠻⠿⣿⣿⣿⣿⣿⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⠇⠀⠀
⠀⠀⠀⠀⠀⠀⠘⣿⣿⣿⣿⡇⠀⣀⣄⡀⠀⠀⠀⠀⢸⣿⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣠⣾⣿⣿⣿⣦⡀⠀⠀⣿⣿⡏⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⡿⠋⠈⠻⣿⣿⣦⣸⣿⣿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠛⠁⠀⠀⠀⠀⠈⠻⣿⣿⣿⠏⠀⠀⠀⠀

                  Author : SilverX     Tg: t.me/silverxvip{reset_code}
    -----------------------------------------------------------------------
    [ Hệ thống tình báo Telegram ] -> Chế độ: {mode_name}
    -----------------------------------------------------------------------
    """
    print(banner)

async def get_telegram_client():
    """Khởi tạo Client động, không hardcode thông tin cũ khi có session"""
    session_path = f"{SESSION_NAME}.session"
    
    if not os.path.exists(session_path):
        print("[!] Không tìm thấy phiên làm việc trước đó. Vui lòng thiết lập cấu hình:")
        try:
            api_id = input("[-] Nhập API ID: ").strip()
            api_hash = input("[-] Nhập API Hash: ").strip()
            phone = input("[-] Nhập Số điện thoại (Ví dụ: +84...): ").strip()
            
            client = TelegramClient(SESSION_NAME, int(api_id), api_hash)
            await client.start(phone_number=phone)
            return client
        except KeyboardInterrupt:
            print("\n[!] Đã hủy tác vụ.")
            sys.exit(0)
    else:
        print("[+] Đang khôi phục phiên làm việc cũ từ file .session...")
        client = TelegramClient(SESSION_NAME, 12345, 'placeholder') 
        await client.connect()
        if not await client.is_user_authorized():
            print("[-] Phiên làm việc cũ hết hạn hoặc không hợp lệ. Vui lòng xóa file .session và chạy lại.")
            sys.exit(1)
        return client

async def main():
    database_yarat()
    client = await get_telegram_client()
    
    async with client:
        while True:
            print_banner()
            print(" Chức năng công cụ:")
            print(" [1] Quét & Thu thập tin nhắn của mục tiêu")
            print(" [2] Trích xuất danh sách và thông tin nhóm")
            print(" [3] Thống kê tần suất hoạt động của mục tiêu")
            print(" [4] Tải xuống hàng loạt hình ảnh/video từ nhóm")
            print(" [5] Thoát")
            
            choice = input("\n[>] Chọn một tùy chọn (1-5): ").strip()
            
            if choice == "1":
                target = input("[?] Nhập Username hoặc ID của mục tiêu: ").strip()
                if target.isdigit(): target = int(target)
                await osint_actions.mesajlari_topla(client, target)
                
            elif choice == "2":
                group = input("[?] Nhập Link nhóm hoặc Username nhóm: ").strip()
                await osint_actions.qrup_melumatlarini_topla(client, group)
                
            elif choice == "3":
                target = input("[?] Nhập Username hoặc ID cần thống kê: ").strip()
                if target.isdigit(): target = int(target)
                await osint_actions.mesaj_statistikasini_topla(client, target)
                
            elif choice == "4":
                group = input("[?] Nhập Link nhóm cần tải phương tiện: ").strip()
                await osint_actions.qrup_mediasini_yukle(client, group)
                
            elif choice == "5":
                print("[+] Đang đóng kết nối. Tạm biệt!")
                break
            else:
                print("[-] Lựa chọn không hợp lệ!")
                
            input("\n[Nhấn Enter để quay lại Menu chính...]")

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\n[!] Chương trình đã dừng đột ngột.")
