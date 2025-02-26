from odoo import models, fields, api


class DoMat(models.Model):
    _name = 'do_mat'
    _description = 'Bảng chứa thông tin độ mật'
    _rec_name = "do_mat"
    
    id = fields.Integer("ID độ mật", required=True)
    do_mat = fields.Char("Độ mật", required=True)
    mo_ta = fields.Char("Mô tả")
 