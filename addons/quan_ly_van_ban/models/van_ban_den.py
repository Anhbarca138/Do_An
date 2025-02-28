from odoo import models, fields, api


class VanBanDen(models.Model):
    _name = 'van_ban_den'
    _description = 'Bảng chứa thông tin văn bản đến'
    
    id = fields.Integer("ID văn bản đến", required=True)
    ngay_den = fields.Date("Ngày đến", required=True)
    so_hieu = fields.Char("Số hiệu", required=True)
    co_quan_ban_hanh = fields.Char("Cơ quan ban hành", required=True)
    trich_yeu = fields.Text("Trích yếu", required=True)

    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    
    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')



 