from odoo import models, fields

class Recruiteur(models.Model):
    _name = 'recruitment.recruiteur'
    _description = 'Recruiteur'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    depart_id = fields.Many2one('recruitment.department', string='depart_id')
