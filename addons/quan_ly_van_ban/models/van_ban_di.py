from odoo import models, fields, api


class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông van_ban_di'
    ten_van_ban = fields.Char("Tên văn bản đi", required=True)
    file = fields.Binary("File")
    ngay_tao = fields.Date("Ngày tạo", required=True)

    trang_thai_id = fields.Many2one("trang_thai", string="Trạng thái", required=True)
    nhan_vien_id =fields.Many2one("nhan_vien",string="Nhân viên", required=True)  


 