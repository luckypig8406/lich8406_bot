# Nhắc ngày Tỵ / Rằm / Mùng 1 — chạy trên GitHub Actions (miễn phí, không cần server)

Mỗi ngày 7h sáng (giờ VN), GitHub tự động chạy 1 script gửi tin nhắn Telegram cho bạn báo:
- 🐍 Ngày Tỵ sắp tới
- 🌑 Mùng 1 sắp tới
- 🌕 Rằm sắp tới

## Bước 1 — Tạo bot Telegram
1. Mở Telegram, chat với **@BotFather**
2. Gõ `/newbot`, đặt tên bot (username kết thúc bằng `bot`, vd `NgayTyBot`)
3. Copy lại **token** BotFather đưa (dạng `123456789:ABCdef...`)
4. Vào chat với bot vừa tạo, bấm **Start** / gửi thử 1 tin bất kỳ (bước này bắt buộc, để lấy được chat id ở bước 3)

## Bước 2 — Tạo repo GitHub
1. Vào github.com → **New repository** → đặt tên tuỳ ý (vd `ngay-ty-bot`) → Create
2. Upload toàn bộ các file trong thư mục này lên repo (kéo-thả trên giao diện web GitHub, hoặc dùng `git push` — xem bước 4)

Cấu trúc file cần có trong repo:
```
.github/workflows/daily.yml
lunar.py
message.py
notify.py
requirements.txt
```

## Bước 3 — Lấy CHAT_ID
Sau khi đã nhắn tin cho bot (bước 1.4), mở trình duyệt, truy cập (thay `<TOKEN>` bằng token của bạn):
```
https://api.telegram.org/bot<TOKEN>/getUpdates
```
Tìm số ở chỗ `"chat":{"id": 123456789, ...}` — đó chính là **CHAT_ID** của bạn.

## Bước 4 — Thêm Secrets vào repo
Trong repo trên GitHub: **Settings → Secrets and variables → Actions → New repository secret**, tạo 2 secret:
| Name | Value |
|---|---|
| `BOT_TOKEN` | token lấy ở bước 1 |
| `CHAT_ID` | id lấy ở bước 3 |

## Bước 5 — Chạy thử ngay
Vào tab **Actions** trên repo → chọn workflow **"Nhac ngay Ty - Ram - Mung 1"** → bấm **Run workflow** để test ngay, không cần đợi tới 7h sáng hôm sau. Nếu thấy tin nhắn tới Telegram là thành công 🎉

Từ hôm sau, GitHub sẽ tự động chạy mỗi ngày lúc 7h sáng (giờ VN) — không cần bật máy tính, không cần server.

## Đổi giờ gửi tin
Sửa dòng `cron` trong `.github/workflows/daily.yml`. Cron chạy theo giờ UTC, VN = UTC+7, nên muốn gửi lúc 8h sáng VN thì đặt `cron: "0 1 * * *"`.

## Ghi chú
- `lunar.py`: tự chuyển đổi Dương lịch ↔ Âm lịch Việt Nam (thuật toán Hồ Ngọc Đức).
- GitHub Actions free tier cho repo public là miễn phí không giới hạn cho việc này; repo private cũng có free quota hàng tháng dư sức dùng cho 1 job/ngày.
- Muốn dùng thêm lệnh `/lich` gõ trực tiếp trong Telegram bất cứ lúc nào (không chỉ theo lịch), cần một server chạy liên tục — nói mình biết nếu bạn muốn bản đó.
