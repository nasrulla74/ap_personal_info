# -*- coding: utf-8 -*-
from odoo import fields, models

class ApCompanyPartner(models.Model):
    _inherit = 'res.partner'

    id_no = fields.Char(string="Id Card No")
    id_serial_no = fields.Char(string="Id Serial No")
    id_expiry_date = fields.Date("ID Expiry Date")
    passport_no = fields.Char(string="Passport No")
    pp_issue_date = fields.Date("Passport Issue")
    pp_expiry_date = fields.Date("Passport Expiry")
    birth_date = fields.Date("Birth Date")
