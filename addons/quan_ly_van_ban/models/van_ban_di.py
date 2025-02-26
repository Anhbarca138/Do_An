from odoo import models, fields, api


class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông van_ban_di'
    
    ngay_di = fields.Date("Ngày đi", required=True)
    so_hieu = fields.Char("Số hiệu", required=True)
    trich_yeu = fields.Char("Trích yếu", required=True)
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    



 