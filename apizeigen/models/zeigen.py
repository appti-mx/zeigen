# -*- coding: utf-8 -*-
import itertools

import requests

from odoo.addons import decimal_precision as dp

from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression
from odoo.tools import pycompat
from requests.auth import HTTPBasicAuth
import json



class Apizeigen(models.Model):
    _name = 'api.zeigen'
    _description = 'Api zeigen'
    _rec_name = 'user'

    user = fields.Char('Usuario')
    password = fields.Char('Password')
    token = fields.Char('Token')
    url = fields.Char('URL')
    access_token = fields.Char('access_token')
    token_type = fields.Char('token_type')
    expires_in = fields.Char('expires_in')
    error_description = fields.Char('error_description')

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    _description = 'Purchase Order related to Payments'

    web_name = fields.Char(string='Nombre del producto', related='name')
    short_description = fields.Char(string='Descripción corta del producto', related='name')
    full_description = fields.Char(string='Descripción larga del producto')
    sku = fields.Char(string='sku')
    stock_quantity = fields.Float(string='stock_quantity')
    price = fields.Float(string='Precio de Lista del producto', related='list_price')
    old_price = fields.Float(string='Precio anterior del producto')
    product_cost = fields.Float(string='Precio al costo del producto.', related='list_price')
    special_price = fields.Float(string='Precio especial')
    maximum_customer_entered_price = fields.Float(string='maximum_customer_entered_price')
    baseprice_amoun = fields.Float(string='baseprice_amoun')
    weight = fields.Float(string='weight')
    length = fields.Float(string='length')
    width = fields.Float(string='width')
    height = fields.Float(string='height')
    product_type = fields.Char(string='product_type')
    sitio = fields.Boolean(string='Vincular a sitio')


    @api.model_create_multi
    def create(self, vals_list):

        datos = vals_list[0]

        general_data = self.env['api.zeigen'].search([('user', '!=', '')], order="id desc")

        url = str(general_data[0].url)+'/token'
        myobj = {'username': str(general_data[0].user), 'password': str(general_data[0].password)}

        r = requests.post(url, data=myobj)

        rjson = r.json()

        access_token = rjson['access_token']
        token_type = rjson['token_type']
        expires_in = rjson['expires_in']
        error_description = rjson['error_description']


        obj2 = {
          "product": {
            "name": str(datos['name']),
            "full_description": "<strong>"+str(datos['full_description'])+"</strong>",
            "short_description": str(datos['short_description']),
            "sku": str(datos['sku']),
            "price" : str(datos['list_price']),
            "stock_quantity": self.qty_available,
          }
        }

        json_obj2 = json.dumps(obj2)


        createproduct = str(general_data[0].url)+'/api/products/'

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer "+access_token
        }

        try:

            rproduct = requests.post(createproduct, data=json_obj2, headers=headers)

        except:

            raise UserError(rproduct.text)

        ''' Store the initial standard price in order to be able to retrieve the cost of a product template for a given date'''
        templates = super(ProductTemplate, self).create(vals_list)
        if "create_product_product" not in self._context:
            templates._create_variant_ids()

        # This is needed to set given values to first variant after creation
        for template, vals in zip(templates, vals_list):
            related_vals = {}
            if vals.get('barcode'):
                related_vals['barcode'] = vals['barcode']
            if vals.get('default_code'):
                related_vals['default_code'] = vals['default_code']
            if vals.get('standard_price'):
                related_vals['standard_price'] = vals['standard_price']
            if vals.get('volume'):
                related_vals['volume'] = vals['volume']
            if vals.get('weight'):
                related_vals['weight'] = vals['weight']
            # Please do forward port
            if vals.get('packaging_ids'):
                related_vals['packaging_ids'] = vals['packaging_ids']
            if related_vals:
                template.write(related_vals)

        return templates

    #@api.multi
    def write(self, vals):

        general_data = self.env['api.zeigen'].search([('user', '!=', '')], order="id desc")

        url = str(general_data[0].url)+'/token'
        myobj = {'username': str(general_data[0].user), 'password': str(general_data[0].password)}

        r = requests.post(url, data=myobj)

        rjson = r.json()

        access_token = rjson['access_token']
        token_type = rjson['token_type']
        expires_in = rjson['expires_in']
        error_description = rjson['error_description']

        headers = {
            'Content-Type': "application/json",
            'Authorization': "Bearer " + access_token
        }

        name_product = ''

        if vals:
            sku = str(self.sku)

            cantidad = 0
            url = str(general_data[0].url)+'/api/productsbysku/'+sku
            rproduct = requests.get(url, headers=headers)
            rjson = rproduct.json()

            name = str(self.name)
            if vals.get('name'):
                name = vals['name']

            list_price = str(self.list_price)
            if vals.get('list_price'):
                list_price = vals['list_price']

            qty_available = self.qty_available
            if vals.get('qty_available'):
                qty_available = vals['qty_available']

            try:
                if rjson['products'][0]['name']:
                    #Actualizar producto
                    obj3 = {
                        "product": {
                            "id": str(rjson['products'][0]['id']),
                            "name": name,
                            "full_description": "<strong>" + name + "</strong>",
                            "short_description": name,
                            "sku": sku,
                            "price": list_price,
                            "stock_quantity": qty_available,
                        }
                    }

                    updateproduct = str(general_data[0].url)+'/api/products/'+str(rjson['products'][0]['id'])

                    json_obj3 = json.dumps(obj3)

                    rproduct = requests.put(updateproduct, data=json_obj3, headers=headers)

            except:
                cantidad = 0
                obj2 = {
                    "product": {
                        "name": str(self.name),
                        "full_description": "<strong>" + str(self.name) + "</strong>",
                        "short_description": str(self.name),
                        "sku": str(self.sku),
                        "price": str(self.list_price),
                        "stock_quantity": str(self.qty_available)
                    }
                }

                json_obj2 = json.dumps(obj2)

                createproduct = str(general_data[0].url)+'/api/products/'

                rproduct = requests.post(createproduct, data=json_obj2, headers=headers)






        uom = self.env['uom.uom'].browse(vals.get('uom_id')) or self.uom_id
        uom_po = self.env['uom.uom'].browse(vals.get('uom_po_id')) or self.uom_po_id
        if uom and uom_po and uom.category_id != uom_po.category_id:
            vals['uom_po_id'] = uom.id

        res = super(ProductTemplate, self).write(vals)
        if 'attribute_line_ids' in vals or vals.get('active'):
            self._create_variant_ids()
        if 'active' in vals and not vals.get('active'):
            self.with_context(active_test=False).mapped('product_variant_ids').write({'active': vals.get('active')})
        if 'image_1920' in vals:
            self.env['product.product'].invalidate_cache(fnames=[
                'image_1920',
                'image_1024',
                'image_512',
                'image_256',
                'image_128',
                'can_image_1024_be_zoomed',
            ])
        return res
