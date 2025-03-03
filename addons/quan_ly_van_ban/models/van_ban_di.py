from odoo import models, fields, api


class VanBanDi(models.Model):
    _name = 'van_ban_di'
    _description = 'Bảng chứa thông tin van_ban_di'
    
    id = fields.Integer("ID văn bản đi", required=True)
    ngay_di = fields.Date("Ngày đi", required=True)
    so_hieu = fields.Char("Số hiệu", required=True)
    trich_yeu = fields.Text("Trích yếu", required=True)
    tep_dinh_kem = fields.Binary("Tệp đính kèm")
    
    id_loai_van_ban = fields.Many2one('loai_van_ban', string='Loại văn bản')
    id_co_quan_ban_hanh = fields.Many2one('phong_ban', string='Cơ quan ban hành')
    id_nguoi_phat_hanh = fields.Many2one('nhan_vien', string='Người phát hành')
    id_do_mat = fields.Many2one('do_mat', string='Độ mật')
    id_nam = fields.Many2one('nam', string='Năm')




 