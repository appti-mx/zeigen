# -*- coding: utf-8 -*-
from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'

    phone_related = fields.Char(track_visibility='always', related='phone')

