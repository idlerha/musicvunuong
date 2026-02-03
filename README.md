# 🎵 Music Vũ Nương - Discord Music Bot 🌸

Chào mừng mày đến với kho lưu trữ của **Music Vũ Nương**! Một con bot Discord chuyên trị nhạc YouTube với phong cách phục vụ cực gắt, giao diện hồng cánh sen sang chảnh và quan trọng nhất là: **Nói không với quảng cáo.**

---

## 🚀 Tính Năng Chính

* **Phát nhạc YouTube:** Phát âm thanh.
* **Hàng chờ thông minh:** Tự động xếp hàng bài hát khi đang phát.
* **Chế độ lặp đa dạng:**
    * `Mode 1`: Lặp lại duy nhất 1 bài (Single Loop).
    * `Mode 2`: Lặp lại cả danh sách chờ (Queue Loop).
    

## 🛠️ Yêu Cầu Cài Đặt

Để chạy được con bot này, máy mày cần có:

1.  **Python 3.8 trở lên.**
2.  **FFmpeg:** Cực kỳ quan trọng để xử lý âm thanh. [FFmpeg](https://www.ffmpeg.org/)
    * *Windows:* Tải FFmpeg và thêm vào Environment Variables.
    * *Linux:* `sudo apt install ffmpeg`
3.  **Token Bot:** Lấy tại [Discord Developer Portal](https://discord.com/developers/applications).

---

## Lệnh, Mô tả
vn!choi [Link],Thêm bài vào hàng chờ hoặc phát ngay.
vn!skip,Bỏ qua bài hiện tại (Tự tắt lặp nếu đang bật).
vn!laplai,Bật/Tắt lặp lại duy nhất bài đang phát.
vn!laplaihangcho,Bật/Tắt lặp lại toàn bộ danh sách.
vn!cut,Đuổi bot ra khỏi kênh voice và xóa sạch hàng chờ.
vn!help,"Hiện bảng hướng dẫn sử dụng ""hồng cánh sen""."

## ⚙️ Hướng Dẫn Chạy Bot
Clone project:
```
git clone https://github.com/idlerha/musicvunuong.git
```
Vào folder:
```
cd musicvunuong
```
Cấu hình: Mở file code lên, kéo xuống cuối cùng và thay token của mày vào:
```
bot.run('TOKEN')
```
Tải thư viện cần thiết:
```
pip install -r requirements.txt
```
Chạy:
```
python main.py
```
⚠️ Lưu Ý Quan Trọng
Intents: Nhớ bật Message Content Intent trong trang Developer của Discord thì bot mới đọc được lệnh.

🤝 Đóng góp nếu bạn có ý tưởng mới hoặc phát hiện lỗi, hãy mở một Issue hoặc gửi một Pull Request. Mọi đóng góp của bạn đều giúp MusicVuNuong hoàn thiện hơn!

© 2026 MusicVuNuong Project. Developed with ❤️ by IdlerHa
