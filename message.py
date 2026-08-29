from datetime import date
import lunar
from proverbs import proverb_of_day


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

    lines = [
        f"📅 Hôm nay {today.strftime('%d/%m/%Y')} — Âm lịch {ld}/{lm}{' nhuận' if leap else ''}/{ly}",
        f"Ngày {can} {chi}",
        "",
        f"🐍 Ngày Tỵ sắp tới: {fmt(ty)}",
        f"🌑 Mùng 1 sắp tới: {fmt(m1)}",
        f"🌕 Rằm sắp tới: {fmt(ram)}",
        "",
        f"📖 {proverb_of_day(today)}",
    ]

    return "\n".join(lines)
