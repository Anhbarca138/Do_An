from odoo import models, fields, api 
from datetime import datetime

class NhanVienChamCong(models.Model):
    _name = 'nhan_vien_chamcong'
    _description = 'Nhân viên chấm công'
    _order = 'check_in desc'

    name = fields.Char(string="Tên bản ghi", compute='_compute_name', store=True)
    employee_id = fields.Many2one('nhan_vien', string='Nhân viên', required=True)
    check_in = fields.Datetime(string='Thời gian chấm công', default=lambda self: datetime.now())
    image = fields.Binary(string='Ảnh chấm công')

    @api.depends('employee_id', 'check_in') 
    def _compute_name(self):
        for rec in self:
            if rec.employee_id and rec.check_in:
                rec.name = f"{rec.employee_id.ho_va_ten} - {rec.check_in.strftime('%Y-%m-%d %H:%M:%S')}" 