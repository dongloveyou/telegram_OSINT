# -*- coding: utf-8 -*-
import sqlite3
import os

DB_NAME = 'telegram_messages.db'

def database_yarat():
    """Khởi tạo cơ sở dữ liệu SQLite nếu chưa tồn tại"""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()
        cursor.execute('''
        CREATE TABLE IF NOT EXISTS messages (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            tg_id INTEGER,
            group_name TEXT,
            message_text TEXT,
            message_date TEXT
        )
        ''')
        connection.commit()
        connection.close()
        print("[+] Cơ sở dữ liệu đã được khởi tạo thành công!")
    except sqlite3.Error as error:
        print(f"[-] Lỗi khi khởi tạo cơ sở dữ liệu: {error}")

def mesaj_elave_et(username, tg_id, group_name, message_text, message_date):
    """Kiểm tra trùng lặp và lưu tin nhắn vào DB & File TXT"""
    try:
        connection = sqlite3.connect(DB_NAME)
        cursor = connection.cursor()

        # Kiểm tra trùng lặp dựa trên nội dung, thời gian và username
        cursor.execute('''
        SELECT COUNT(*) FROM messages WHERE message_text = ? AND message_date = ? AND username = ?;
        ''', (message_text, message_date, username))
        
        if cursor.fetchone()[0] == 0:
            cursor.execute('''
            INSERT INTO messages (username, tg_id, group_name, message_text, message_date)  
            VALUES (?, ?, ?, ?, ?);
            ''', (username, tg_id, group_name, message_text, message_date))
            connection.commit()

            # Ghi ra file TXT báo cáo
            safe_filename = "".join([c for c in username if c.isalpha() or c.isdigit() or c=='_']).rstrip()
            with open(f"{safe_filename}_messages.txt", "a", encoding="utf-8") as file:
                file.write(f"Nhóm: {group_name}\nTin nhắn: {message_text}\nNgày: {message_date}\n" + "-"*30 + "\n")
            print(f"[+] Đã lưu tin nhắn mới từ nhóm: {group_name}")
        
        connection.close()
    except sqlite3.Error as error:
        print(f"[-] Lỗi lưu DB: {error}")
    except Exception as error:
        print(f"[-] Lỗi ghi file: {error}")
