"""
Gio Hoang Dao (gio tot) theo Chi cua ngay - theo bang tra truyen thong trong lich van nien.
Tham khao / giai tri theo quan niem dan gian, khong phai khang dinh khoa hoc.
"""
from datetime import date, time
import lunar

# Khung gio theo 12 dia chi (gio am lich, moi khung 2 tieng)
GIO_CHI_RANGES = {
    "Tý": (23, 1), "Sửu": (1, 3), "Dần": (3, 5), "Mão": (5, 7),
    "Thìn": (7, 9), "Tỵ": (9, 11), "Ngọ": (11, 13), "Mùi": (13, 15),
    "Thân": (15, 17), "Dậu": (17, 19), "Tuất": (19, 21), "Hợi": (21, 23),
}

# Bang gio hoang dao theo tung cap Chi ngay (ca ngay tra ra 6 gio tot trong 12 gio)
GIO_HOANG_DAO_TABLE = {
    frozenset(["Tý", "Ngọ"]): ["Tý", "Sửu", "Mão", "Ngọ", "Thân", "Dậu"],
    frozenset(["Sửu", "Mùi"]): ["Dần", "Mão", "Tỵ", "Thân", "Tuất", "Hợi"],
    frozenset(["Dần", "Thân"]): ["Tý", "Sửu", "Thìn", "Tỵ", "Mùi", "Tuất"],
    frozenset(["Mão", "Dậu"]): ["Tý", "Dần", "Mão", "Ngọ", "Mùi", "Dậu"],
    frozenset(["Thìn", "Tuất"]): ["Dần", "Thìn", "Tỵ", "Thân", "Dậu", "Hợi"],
    frozenset(["Tỵ", "Hợi"]): ["Sửu", "Thìn", "Ngọ", "Mùi", "Tuất", "Hợi"],
}

# Tam hop / luc hop cua tung Chi (dung de doi chieu voi gio sinh cua nguoi dung)
TAM_HOP = {
    "Thân": ["Thân", "Tý", "Thìn"], "Tý": ["Thân", "Tý", "Thìn"], "Thìn": ["Thân", "Tý", "Thìn"],
    "Dần": ["Dần", "Ngọ", "Tuất"], "Ngọ": ["Dần", "Ngọ", "Tuất"], "Tuất": ["Dần", "Ngọ", "Tuất"],
    "Tỵ": ["Tỵ", "Dậu", "Sửu"], "Dậu": ["Tỵ", "Dậu", "Sửu"], "Sửu": ["Tỵ", "Dậu", "Sửu"],
    "Hợi": ["Hợi", "Mão", "Mùi"], "Mão": ["Hợi", "Mão", "Mùi"], "Mùi": ["Hợi", "Mão", "Mùi"],
}
LUC_HOP = {
    "Tý": "Sửu", "Sửu": "Tý", "Dần": "Hợi", "Hợi": "Dần", "Mão": "Tuất", "Tuất": "Mão",
    "Thìn": "Dậu", "Dậu": "Thìn", "Tỵ": "Thân", "Thân": "Tỵ", "Ngọ": "Mùi", "Mùi": "Ngọ",
}


def fmt_range(chi: str) -> str:
    start, end = GIO_CHI_RANGES[chi]
    return f"{start}h-{end}h"


def gio_hoang_dao_hom_nay(d: date = None):
    """Tra ve danh sach cac Chi gio hoang dao (tot) cua ngay d."""
    d = d or date.today()
    _, chi_ngay = lunar.can_chi_ngay(d)
    for pair, gio_tot in GIO_HOANG_DAO_TABLE.items():
        if chi_ngay in pair:
            return chi_ngay, gio_tot
    return chi_ngay, []


def chi_of_hour(gio: int) -> str:
    for chi, (start, end) in GIO_CHI_RANGES.items():
        if start == 23:  # Ty vat qua nua dem
            if gio >= 23 or gio < 1:
                return chi
        elif start <= gio < end:
            return chi
    return "Tý"


def gio_hop_voi_ban(chi_sinh: str):
    """Cac Chi hop voi Chi gio sinh cua nguoi dung (tam hop + luc hop)."""
    hop = set(TAM_HOP.get(chi_sinh, []))
    hop.add(LUC_HOP.get(chi_sinh, chi_sinh))
    hop.discard(chi_sinh)
    return sorted(hop, key=lambda c: list(GIO_CHI_RANGES).index(c))


if __name__ == "__main__":
    today = date.today()
    chi_ngay, gio_tot = gio_hoang_dao_hom_nay(today)
    print(f"Ngay Chi: {chi_ngay}")
    print("Gio hoang dao:", ", ".join(f"{c} ({fmt_range(c)})" for c in gio_tot))
    print("Chi gio 11h05:", chi_of_hour(11))
    print("Hop voi Ngo:", gio_hop_voi_ban("Ngọ"))
