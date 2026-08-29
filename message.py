from datetime import date
import lunar
import gio_hoang_dao as ghd
from proverbs import proverb_of_day

# ---- Thong tin gio sinh cua ban, dung de tinh gio hop moi ngay ----
# Sinh 8/4/2006, luc 11h05 -> roi vao khung gio Ngo (11h-13h)
CHI_GIO_SINH = ghd.chi_of_hour(11)  # = "Ngọ"


def build_message() -> str:
    today = date.today()
    can, chi = lunar.can_chi_ngay(today)
    ld, lm, ly, leap = lunar.solar_to_lunar(today.day, today.month, today.year)

    ty = lunar.next_ngay_ty(today)
    m1 = lunar.next_mung_1(today)
    ram = lunar.next_ram(today)

    def fmt(d: date) -> str:
        if d == today:
            return f"{d.strftime('%d/%m/%Y')} (hôm nay)"
        delta = (d - today).days
        return f"{d.strftime('%d/%m/%Y')} (còn {delta} ngày)"

    chi_ngay, gio_tot = ghd.gio_hoang_dao_hom_nay(today)
    gio_tot_str = ", ".join(f"{c} ({ghd.fmt_range(c)})" for c in gio_tot)

    gio_hop = ghd.gio_hop_voi_ban(CHI_GIO_SINH)
    gio_hop_trong_ngay = [c for c in gio_tot if c in gio_hop]

    lines = [
        f"📅 Hôm nay {today.strftime('%d/%m/%Y')} — Âm lịch {ld}/{lm}{' nhuận' if leap else ''}/{ly}",
        f"Ngày {can} {chi}",
        "",
        f"🐍 Ngày Tỵ sắp tới: {fmt(ty)}",
        f"🌑 Mùng 1 sắp tới: {fmt(m1)}",
        f"🌕 Rằm sắp tới: {fmt(ram)}",
        "",
        f"⏰ Giờ hoàng đạo hôm nay (ngày {chi_ngay}): {gio_tot_str}",
    ]
    if gio_hop_trong_ngay:
        hop_str = ", ".join(f"{c} ({ghd.fmt_range(c)})" for c in gio_hop_trong_ngay)
        lines.append(f"✨ Trong đó hợp với giờ sinh của bạn ({CHI_GIO_SINH}): {hop_str}")
    else:
        lines.append(
            f"ℹ️ Hôm nay không có giờ hoàng đạo nào hợp trực tiếp với giờ sinh ({CHI_GIO_SINH}) của bạn."
        )
    lines.append(
        "(Giờ hoàng đạo theo lịch vạn niên dân gian, mang tính tham khảo cho vui.)"
    )

    cau, nguon = proverb_of_day(today)
    lines += ["", f"📖 “{cau}”", f"— {nguon}"]

    return "\n".join(lines)
