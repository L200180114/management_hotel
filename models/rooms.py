from odoo import _, api, fields, models

class RoomHotel(models.Model):
    _name = 'hotel.rooms'
    _description = 'Room Hotel'

    name = fields.Selection([
        ('ekonomi', 'Ekonomi'),
        ('vip', 'VIP'),
        ('vvip', 'VVIP')
    ], string='Tipe Kamar', required=True)
    harga = fields.Integer(string='Harga/malam', required=True)
    descrips = fields.Text(string='Deskripsi')
    