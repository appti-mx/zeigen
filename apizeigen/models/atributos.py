# -*- coding: utf-8 -*-
import itertools

import requests


from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression
from odoo.tools import pycompat
from requests.auth import HTTPBasicAuth
import json


class marcazeigen(models.Model):
    _name = 'marca.zeigen'
    _description = 'marca_zeigen'
    _rec_name = 'nombre'

    id_atribute = fields.Integer('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')




class subcategoriazeigen(models.Model):
    _name = 'subcategoria.zeigen'
    _description = 'subcategoria_zeigen'
    _rec_name = 'nombre'

    id_atribute = fields.Integer('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')



