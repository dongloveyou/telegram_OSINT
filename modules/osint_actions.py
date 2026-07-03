# -*- coding: utf-8 -*-
import os
from telethon import TelegramClient
from telethon.tl.types import InputMessagesFilterPhotos, InputMessagesFilterVideo
from database import mesaj_elave_et

async def mesajlari_topla(client, search_value):
    """Thu thập tin nhắn của mục tiêu từ các nhóm công khai/tham gia"""
    try:
        print(f"[*] Đang quét các nhóm để tìm mục tiêu: {search_value}...")
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                group_name = dialog.name
                print(f"[~] Đang tìm kiếm trong nhóm: {group_name}")
                
                # Giới hạn an toàn 1000 tin nhắn gần nhất để tránh dính FloodWait bới Telegram
                async for message in client.iter_messages(dialog.id, from_user=search_value, limit=1000):
                    if message.text:
                        mesaj_elave_et(str(search_value), message.sender_id, group_name, message.text, str(message.date))
        print("[+] Hoàn thành tìm kiếm tin nhắn!")
    except Exception as error:
        print(f"[-] Lỗi khi thu thập tin nhắn: {error}")

async def qrup_melumatlarini_topla(client, group_link):
    """Thu thập thông tin chi tiết và danh sách thành viên của một nhóm"""
    try:
        print(f"[*] Đang kết nối tới nhóm: {group_link}...")
        group = await client.get_entity(group_link)
        group_name = group.title
        group_description = getattr(group, 'about', 'Không có mô tả')

        print(f"[+] Đang trích xuất danh sách thành viên nhóm: {group_name}...")
        members = await client.get_participants(group)
        
        safe_filename = "".join([c for c in group_name if c.isalpha() or c.isdigit() or c=='_']).rstrip()
        with open(f"{safe_filename}_info.txt", "w", encoding="utf-8") as file:
            file.write(f"🛡️ THÔNG TIN NHÓM: {group_name} 🛡️\n")
            file.write(f"Mô tả: {group_description}\nID: {group.id}\nSố thành viên: {len(members)}\n")
            file.write("=" * 50 + "\n\n")

            for idx, member in enumerate(members, start=1):
                first = member.first_name or ''
                last = member.last_name or ''
                phone = member.phone or 'Ẩn'
                status = 'Bot' if member.bot else 'Người dùng'
                file.write(f"#{idx} - ID: {member.id} | Tên: {first} {last} | SĐT: {phone} | Loại: {status}\n")

        print(f"[+] Đã lưu thông tin nhóm vào file: {safe_filename}_info.txt")
    except Exception as error:
        print(f"[-] Lỗi trích xuất thông tin nhóm: {error}")

async def mesaj_statistikasini_topla(client, search_value):
    """Thống kê tần suất hoạt động của mục tiêu trên các nhóm"""
    try:
        message_counts = {}
        print(f"[*] Đang lập thống kê cho mục tiêu: {search_value}...")
        
        async for dialog in client.iter_dialogs():
            if dialog.is_group:
                count = 0
                async for _ in client.iter_messages(dialog.id, from_user=search_value, limit=500):
                    count += 1
                if count > 0:
                    message_counts[dialog.name] = count

        if message_counts:
            print(f"\n Thống kê hoạt động của '{search_value}':")
            for group, count in message_counts.items():
                print(f" -> Nhóm: {group} | Số tin nhắn: {count}")
        else:
            print("[!] Không tìm thấy dữ liệu hoạt động.")
    except Exception as error:
        print(f"[-] Lỗi lập thống kê: {error}")

async def qrup_mediasini_yukle(client, group_link):
    """Tải tệp phương tiện (ảnh/video) từ nhóm chỉ định"""
    try:
        group = await client.get_entity(group_link)
        os.makedirs("media_downloads", exist_ok=True)
        print(f"[*] Đang quét tải media từ nhóm: {group.title} (Giới hạn 100 file gần nhất)...")
        
        count = 0
        async for message in client.iter_messages(group, limit=100):
            if message.media:
                path = await client.download_media(message.media, file="media_downloads/")
                print(f"[+] Đã tải: {path}")
                count += 1
        print(f"[+] Hoàn thành. Đã tải {count} tệp tin vào thư mục 'media_downloads/'")
    except Exception as error:
        print(f"[-] Lỗi khi tải media: {error}")
