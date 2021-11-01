from odoo import _, api, fields, models

class Custommer(models.Model):
    _inherit = 'res.partner'

    is_custommer = fields.Boolean(string='Custommer', default=False)