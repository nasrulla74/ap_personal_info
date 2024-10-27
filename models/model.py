# -*- coding: utf-8 -*-
import json
from odoo import fields, models, api

# class MaldivesIslands(models.Model):
#     _name = "maldives.island"
#     _description = "Islands"
#
#     name = fields.Char(string="Island", required=True)
#     atoll_id = fields.Many2one('res.country.state', string="Atoll", domain="[('country_id', '=', 154)]")
#     postal_code = fields.Char(string="Postal Code")


class ContactRelations(models.Model):
    _name = "contact.relation"
    _description = "Contact Relations"
    _rec_name = 'relation_type'

    relation_type = fields.Selection([('mother', 'Mother'), ('father', 'Father'), ('spause', 'Spause'), ('brother', 'Brother'), ('sister', 'Sister'), ('child', 'Children')],
                              string="Relation Type", required=True)
    relation_id = fields.Many2one('res.partner', string="Relationship")
    partner_id = fields.Many2one('res.partner', "Contact", index=True)


class ApCompanyPartner(models.Model):
    _inherit = 'res.partner'

    id_no = fields.Char(string="Id Card No")
    id_serial_no = fields.Char(string="Id Serial No")
    id_expiry_date = fields.Date("ID Expiry Date")
    passport_no = fields.Char(string="Passport No")
    pp_issue_date = fields.Date("Passport Issue")
    pp_expiry_date = fields.Date("Passport Expiry")
    birth_date = fields.Date("Birth Date")
    # x_birth_place_id = fields.Many2one('res.country.state', string="Birth Place")
    #island_id = fields.Many2one('maldives.island', string="Island")
    #relation_ids = fields.One2many('contact.relation', 'partner_id', string="Family Relations")
    mother = fields.Char(string="Mother")
    father = fields.Char(string="Father")
    # x_blood_group = fields.Char(string="Blood Group")
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')],
                              string="Gender")
    island_id_domain = fields.Char(compute="_compute_island_id_domain", readonly=True, store=False)
    # x_occupation_type = fields.Char("Occupation Type")
    # x_monthly_income = fields.Char("monthly_income")

    # is_private = fields.Boolean(string="Is Private", default=False)

    # @api.depends('state_id')
    # def _compute_island_id_domain(self):
    #     for rec in self:
    #         rec.island_id_domain = json.dumps(
    #             [('atoll_id', '=', rec.state_id.id)]
    #         )

    # @api.onchange('state_id')
    # def onchange_state_id(self):
    #     for rec in self:
    #         print(rec.state_id.id)
    #         return {'domain': {'island_id': ['atoll_id', '=', rec.state_id.id]}}




