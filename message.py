from datetime import date
import random
import lunar
from proverbs import PROVERBS
from quotes import QUOTES

# Gop chung tuc ngu (khong co tac gia) va quote (co tac gia) thanh 1 kho duy nhat.
# Moi phan tu chuan hoa thanh (cau, tac_gia_hoac_None).
CAU_HAY = [(p, None) for p in PROVERBS] + [(c, a) for c, a in QUOTES]


def cau_hay_of_day(d: date = None):
    d = d or date.today()
    rng = random.Random(d.toordinal())
    return rng.choice(CAU_HAY)


def build_message() -> str:
    today = date.today()
    can_ngay, chi_ngay = lunar.can_chi_ngay(today)
    ld, lm, ly, leap = lunar.solar_to_lunar(today.day, today.month, today.year)
    can_thang, chi_thang = lunar.can_chi_thang(lm, ly)
    can_nam, chi_nam = lunar.can_chi_nam(ly)

    ty = lunar.next_ngay_ty(today)
    at = lunar.next_ngay_can("Ất", today)
    m1 = lunar.next_mung_1(today)
    ram = lunar.next_ram(today)

    def fmt(d: date) -> str:
        if d == today:
            return f"{d.strftime('%d/%m/%Y')} (hôm nay)"
        delta = (d - today).days
        return f"{d.strftime('%d/%m/%Y')} (còn {delta} ngày)"

    lines = [
        f"📅 Hôm nay {today.strftime('%d/%m/%Y')} — Âm lịch {ld}/{lm}{' nhuận' if leap else ''}/{ly}",
        f"Ngày {can_ngay} {chi_ngay}, tháng {can_thang} {chi_thang}, năm {can_nam} {chi_nam}",
        "",
        f"🐍 Ngày Tỵ sắp tới: {fmt(ty)}",
        f"🈺 Ngày Ất sắp tới: {fmt(at)}",
        f"🌑 Mùng 1 sắp tới: {fmt(m1)}",
        f"🌕 Rằm sắp tới: {fmt(ram)}",
        "",
    ]

    cau, tac_gia = cau_hay_of_day(today)
    if tac_gia:
        lines += [f"💬 “{cau}”", f"— {tac_gia}"]
    else:
        lines += [f"📖 {cau}"]

    return "\n".join(lines)
