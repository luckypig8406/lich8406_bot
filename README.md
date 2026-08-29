# Nhắc ngày Tỵ / Rằm / Mùng 1 — chạy trên GitHub Actions (miễn phí, không cần server)

Mỗi ngày 8h sáng (giờ VN), GitHub tự động chạy 1 script gửi tin nhắn Telegram cho bạn báo:
- 🐍 Ngày Tỵ sắp tới
- 🌑 Mùng 1 sắp tới
- 🌕 Rằm sắp tới
- ⏰ Giờ hoàng đạo trong ngày (theo lịch vạn niên dân gian) + giờ nào hợp với giờ sinh của bạn
- 📖 Một câu tục ngữ / ngạn ngữ / thành ngữ mỗi ngày, có ghi nguồn gốc

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
gio_hoang_dao.py
proverbs.py
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
Sửa dòng `cron` trong `.github/workflows/daily.yml`. Cron chạy theo giờ UTC, VN = UTC+7. Hiện đang đặt `"0 1 * * *"` = 8h sáng VN. Muốn đổi giờ khác thì lấy giờ VN mong muốn trừ 7.

## Giờ sinh cá nhân
Trong `message.py` có dòng:
```python
CHI_GIO_SINH = ghd.chi_of_hour(11)  # gio sinh 11h05 -> khung gio Ngo (11h-13h)
```
Đang set cứng theo giờ sinh 11h05 (8/4/2006) → rơi vào giờ Ngọ. Nếu cần đổi, thay số `11` bằng giờ sinh khác (0-23).

## Câu tục ngữ / ngạn ngữ mỗi ngày
Nằm trong `proverbs.py`, mỗi ngày bot chọn 1 câu khác nhau theo vòng xoay ~60 câu (tục ngữ, ca dao Việt Nam, ngạn ngữ nước ngoài, ngụ ngôn), mỗi câu đều ghi nguồn gốc thay vì gán cho một "tác giả" — vì đây là trí tuệ dân gian truyền miệng qua nhiều đời, không thuộc về một cá nhân cụ thể. Muốn thêm/sửa câu, chỉnh trực tiếp list `PROVERBS` trong file đó.

## Giờ hoàng đạo
`gio_hoang_dao.py` dùng bảng tra truyền thống trong lịch vạn niên (6 giờ tốt / 12 giờ mỗi ngày, tính theo Chi của ngày), cộng thêm phần đối chiếu với giờ sinh (tam hợp/lục hợp) để gợi ý giờ nào hợp với bạn nhất trong ngày. Đây là kiến thức dân gian mang tính tham khảo, không phải khẳng định khoa học.

## Ghi chú
- `lunar.py`: tự chuyển đổi Dương lịch ↔ Âm lịch Việt Nam (thuật toán Hồ Ngọc Đức).
- GitHub Actions free tier cho repo public là miễn phí không giới hạn cho việc này; repo private cũng có free quota hàng tháng dư sức dùng cho 1 job/ngày.
- Muốn dùng thêm lệnh `/lich` gõ trực tiếp trong Telegram bất cứ lúc nào (không chỉ theo lịch), cần một server chạy liên tục — nói mình biết nếu bạn muốn bản đó.
