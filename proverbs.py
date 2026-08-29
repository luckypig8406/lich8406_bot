"""
Kho tuc ngu / ngan ngu / thanh ngu - moi ngay bot chon 1 cau khac nhau (xoay vong theo ngay).

Luu y: tuc ngu, ca dao, thanh ngu la tri tue dan gian duoc luu truyen qua nhieu doi,
khong co tac gia ca nhan cu the. O day ghi "nguon goc" (vung mien / dan toc) thay vi
bia dat mot cai ten tac gia, de dam bao chinh xac.
"""
from datetime import date

# Moi phan tu: (cau, nguon goc)
PROVERBS = [
    ("Có công mài sắt, có ngày nên kim.", "Tục ngữ Việt Nam"),
    ("Đi một ngày đàng, học một sàng khôn.", "Tục ngữ Việt Nam"),
    ("Gần mực thì đen, gần đèn thì sáng.", "Tục ngữ Việt Nam"),
    ("Lá lành đùm lá rách.", "Tục ngữ Việt Nam"),
    ("Uống nước nhớ nguồn.", "Tục ngữ Việt Nam"),
    ("Ăn quả nhớ kẻ trồng cây.", "Tục ngữ Việt Nam"),
    ("Một cây làm chẳng nên non, ba cây chụm lại nên hòn núi cao.", "Ca dao Việt Nam"),
    ("Thất bại là mẹ thành công.", "Tục ngữ Việt Nam"),
    ("Cái khó ló cái khôn.", "Tục ngữ Việt Nam"),
    ("Không thầy đố mày làm nên.", "Tục ngữ Việt Nam"),
    ("Tốt gỗ hơn tốt nước sơn.", "Tục ngữ Việt Nam"),
    ("Đói cho sạch, rách cho thơm.", "Tục ngữ Việt Nam"),
    ("Chớ thấy sóng cả mà ngã tay chèo.", "Tục ngữ Việt Nam"),
    ("Nước chảy đá mòn.", "Thành ngữ Việt Nam"),
    ("Muốn ăn quả phải trồng cây.", "Tục ngữ Việt Nam"),
    ("Kiến tha lâu cũng đầy tổ.", "Tục ngữ Việt Nam"),
    ("Cây ngay không sợ chết đứng.", "Tục ngữ Việt Nam"),
    ("Đi với Bụt mặc áo cà sa, đi với ma mặc áo giấy.", "Tục ngữ Việt Nam"),
    ("Học thầy không tày học bạn.", "Tục ngữ Việt Nam"),
    ("Ăn chắc mặc bền.", "Thành ngữ Việt Nam"),
    ("Gieo gió gặt bão.", "Thành ngữ Việt Nam"),
    ("Có chí thì nên.", "Tục ngữ Việt Nam"),
    ("Cái nết đánh chết cái đẹp.", "Tục ngữ Việt Nam"),
    ("Nhất nghệ tinh, nhất thân vinh.", "Tục ngữ Việt Nam"),
    ("Trăm hay không bằng tay quen.", "Tục ngữ Việt Nam"),
    ("Con hơn cha là nhà có phúc.", "Tục ngữ Việt Nam"),
    ("Lửa thử vàng, gian nan thử sức.", "Tục ngữ Việt Nam"),
    ("Ở hiền gặp lành.", "Tục ngữ Việt Nam"),
    ("Góp gió thành bão.", "Thành ngữ Việt Nam"),
    ("Có gan làm giàu.", "Tục ngữ Việt Nam"),
    ("Rùa thắng thỏ nhờ kiên trì, chứ không nhờ tốc độ.", "Ngụ ngôn Aesop (Rùa và Thỏ)"),
    ("Đừng bao giờ đếm gà con trước khi trứng nở.", "Ngạn ngữ phương Tây"),
    ("Ai cười người sau cùng, người đó cười ngon nhất.", "Ngạn ngữ Anh"),
    ("Con đường ngàn dặm bắt đầu từ một bước chân.", "Ngạn ngữ Trung Hoa"),
    ("Muốn đi nhanh thì đi một mình, muốn đi xa thì đi cùng nhau.", "Ngạn ngữ châu Phi"),
    ("Không có gió thuận nào giúp được người không biết mình đi đâu.", "Ngạn ngữ La Mã"),
    ("Ngã ở đâu, đứng dậy ở đó.", "Ngạn ngữ Nhật Bản"),
    ("Cây tre càng cong càng dẻo, con người càng khó càng bền.", "Ngạn ngữ Nhật Bản"),
    ("Nước sâu chảy lặng lẽ, người khôn nói ít làm nhiều.", "Ngạn ngữ Trung Hoa"),
    ("Một giọt nước không làm nên đại dương, nhưng đại dương không thể thiếu một giọt nước.", "Ngạn ngữ Ấn Độ"),
    ("Không có con đường nào trải hoa hồng dẫn đến vinh quang.", "Ngạn ngữ Pháp"),
    ("Trước khi chữa bệnh cho người, hãy tự chữa bệnh cho mình trước.", "Ngạn ngữ Trung Hoa"),
    ("Kẻ chậm chân nhưng bền bỉ vẫn thắng cuộc đua.", "Ngụ ngôn Aesop (Rùa và Thỏ)"),
    ("Đừng đánh giá một ngày qua vụ mùa bạn gặt, mà qua những hạt giống bạn gieo.", "Ngạn ngữ phương Tây"),
    ("Cẩn tắc vô áy náy.", "Thành ngữ Việt Nam"),
    ("Sai một ly đi một dặm.", "Tục ngữ Việt Nam"),
    ("Trâu chậm uống nước đục.", "Tục ngữ Việt Nam"),
    ("Đèn nhà ai nấy rạng.", "Tục ngữ Việt Nam"),
    ("Có làm thì mới có ăn, không dưng ai dễ đem phần đến cho.", "Ca dao Việt Nam"),
    ("Muốn biết phải hỏi, muốn giỏi phải học.", "Tục ngữ Việt Nam"),
    ("Cây có gốc mới nở cành xanh ngọn, nước có nguồn mới bể rộng sông sâu.", "Ca dao Việt Nam"),
    ("Chuồn chuồn bay thấp thì mưa, bay cao thì nắng, bay vừa thì râm.", "Tục ngữ Việt Nam"),
    ("Người khôn ăn nói nửa chừng, để cho người dại nửa mừng nửa lo.", "Ca dao Việt Nam"),
    ("Ăn cây nào rào cây nấy.", "Tục ngữ Việt Nam"),
    ("Đi hỏi già, về nhà hỏi trẻ.", "Tục ngữ Việt Nam"),
    ("Chim khôn kêu tiếng rảnh rang, người khôn nói tiếng dịu dàng dễ nghe.", "Ca dao Việt Nam"),
    ("Việc hôm nay chớ để ngày mai.", "Tục ngữ Việt Nam"),
    ("Muốn sang thì bắc cầu Kiều, muốn con hay chữ thì yêu lấy thầy.", "Ca dao Việt Nam"),
    ("Một điều nhịn, chín điều lành.", "Tục ngữ Việt Nam"),
    ("Ai ơi giữ chí cho bền, dù ai xoay hướng đổi nền mặc ai.", "Ca dao Việt Nam"),
]


def proverb_of_day(d: date = None):
    """Tra ve (cau, nguon_goc) cho ngay d."""
    d = d or date.today()
    idx = d.toordinal() % len(PROVERBS)
    return PROVERBS[idx]
