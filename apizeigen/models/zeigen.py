# -*- coding: utf-8 -*-
from odoo import fields, models, api
from odoo.exceptions import AccessError, UserError

class zeigen(models.Model):
    _name = 'api.zeigen'
    _description = 'Api zeigen'
    _rec_name = 'name'

    name = fields.Char('Name',help="Nombre")