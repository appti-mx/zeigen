# -*- coding: utf-8 -*-
import itertools

import requests


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

    web_name = fields.Char(string='Nombre', related='name')
    short_description = fields.Char(string='Descripción corta')
    full_description = fields.Char(string='Descripción larga')
    stock_quantity = fields.Float(string='Cantidad en Inventario', related='qty_available')
    disable_buy_button = fields.Boolean('Habilita botón de compra')
    price = fields.Float(string='Precio de Venta', related='list_price')
    old_price = fields.Float(string='Precio anterior del producto')
    published = fields.Boolean('Publicado en Tecnofin')
    weight = fields.Float(string='Peso')
    length = fields.Float(string='Largo del equipo')
    width = fields.Float(string='Ancho del equipo')
    height = fields.Float(string='Alto del equipo ')
    product_id = fields.Integer(related='id')
    category_id = fields.Float('Familia')
    category_name = fields.Char('Familia')
    sitio = fields.Boolean(string='Integración en Tecnofin')
    sku = fields.Char(string='SKU')
    special_price = fields.Float(string='Precio especial', related='list_price')

    product_cost = fields.Float(string='Precio al costo del producto.', related='list_price')

    marca = fields.Many2one('marca.zeigen', 'Marca')
    subcategoria = fields.Many2one('subcategoria.zeigen','Subcategoría')



    @api.model_create_multi
    def create(self, vals_list):

        datos = vals_list[0]

        if datos['sitio']:

            general_data = self.env['api.zeigen'].search([('user', '!=', '')], order="id desc")

            url = str(general_data[0].url) + '/token'
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
                    "short_description":str(datos['short_description']),
                    "full_description":"<strong>" + str(datos['full_description']) + "</strong>",
                    "stock_quantity": self.qty_available,
                    "disable_buy_button": self.disable_buy_button,
                    "price":str(datos['list_price']),
                    "old_price":self.old_price,
                    "published":self.published,
                    "weight":self.weight,
                    "length":self.length,
                    "width":self.width,
                    "height":self.height,
                    "product_id":self.product_id,
                    "category_id":self.category_id,
                    "category_name":self.category_name,
                    "sitio":self.sitio,
                    "sku":str(datos['sku']),
                    "product_cost":str(datos['list_price'])
                }
            }

            json_obj2 = json.dumps(obj2)

            createproduct = str(general_data[0].url) + '/api/products/'

            headers = {
                'Content-Type': "application/json",
                'Authorization': "Bearer " + access_token
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

    # @api.multi
    def write(self, vals):

        sitio = self.sitio
        if vals.get('sitio'):
            sitio = vals['sitio']


        if sitio:

            general_data = self.env['api.zeigen'].search([('user', '!=', '')], order="id desc")

            url = str(general_data[0].url) + '/token'
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
                url = str(general_data[0].url) + '/api/productsbysku/' + sku
                rproduct = requests.get(url, headers=headers)
                rjson = rproduct.json()

                name = str(self.name)
                if vals.get('name'):
                    name = vals['name']

                short_description = str(self.short_description)
                if vals.get('short_description'):
                    short_description = vals['short_description']

                full_description = str(self.full_description)
                if vals.get('full_description'):
                    full_description = vals['full_description']

                stock_quantity = self.qty_available
                if vals.get('stock_quantity'):
                    stock_quantity = vals['stock_quantity']
                if vals.get('qty_available'):
                    stock_quantity = vals['qty_available']

                disable_buy_button = str(self.disable_buy_button)
                if vals.get('disable_buy_button'):
                    disable_buy_button = vals['disable_buy_button']

                price = str(self.price)
                if vals.get('price'):
                    price = vals['price']

                qty_available = str(self.qty_available)
                if vals.get('qty_available'):
                    qty_available = vals['qty_available']

                old_price = str(self.old_price)
                if vals.get('old_price'):
                    old_price = vals['old_price']

                published = str(self.published)
                if vals.get('published'):
                    published = vals['published']

                weight = str(self.weight)
                if vals.get('weight'):
                    weight = vals['weight']

                length = str(self.length)
                if vals.get('length'):
                    length = vals['length']

                width = str(self.width)
                if vals.get('width'):
                    length = vals['width']

                height = str(self.height)
                if vals.get('height'):
                    height = vals['height']

                product_id = str(self.product_id)
                if vals.get('product_id'):
                    product_id = vals['product_id']

                category_id = str(self.category_id)
                if vals.get('category_id'):
                    category_id = vals['category_id']

                category_name = str(self.category_name)
                if vals.get('category_name'):
                    category_name = vals['category_name']

                sitio = str(self.sitio)
                if vals.get('sitio'):
                    sitio = vals['sitio']

                sku = str(self.sku)
                if vals.get('sku'):
                    sku = vals['sku']

                product_cost = str(self.product_cost)
                if vals.get('product_cost'):
                    product_cost = vals['product_cost']





                marca = self.marca
                if vals.get('marca'):
                    id_marca = self.env['marca.zeigen'].search([('id', '=',vals['marca'])])

                    marca = id_marca[0]

                subcategoria = self.subcategoria
                if vals.get('subcategoria'):
                    id_subcategoria = self.env['subcategoria.zeigen'].search([('id', '=', vals['subcategoria'])])

                    subcategoria = id_subcategoria[0]







                try:
                    if rjson['products'][0]['name']:
                        # Actualizar producto
                        obj3 = {
                            "product": {
                                "id": str(rjson['products'][0]['id']),
                                "name": str(name),
                                "short_description": str(short_description),
                                "full_description": "<strong>" + str(full_description) + "</strong>",
                                "stock_quantity": stock_quantity,
                                "disable_buy_button": str(disable_buy_button),
                                "price": str(price),
                                "old_price": str(old_price),
                                "published": str(published),
                                "weight": str(weight),
                                "length": str(length),
                                "width": str(width),
                                "height": str(height),
                                "product_id": str(product_id),
                                "category_id": str(category_id),
                                "category_name": str(category_name),
                                "sitio": str(sitio),
                                "sku": str(sku),
                                "product_cost": str(product_cost),
                                "specification_attributes": "[{ \"attribute_type_id\": 0, \"custom_value\": null, \"allow_filtering\": false, \"show_on_product_page\": true, \"display_order\": 1, \"attribute_type\": \"Option\", \"specification_attribute_option\": { \"specification_attribute_id\": 1, \"name\": \"" + str(
                                    sku) + "\", \"color_squares_rgb\": null, \"display_order\": 0 } },{ \"attribute_type_id\": 0, \"custom_value\": null, \"allow_filtering\": false, \"show_on_product_page\": true, \"display_order\": 1, \"attribute_type\": \"Option\", \"specification_attribute_option\": { \"specification_attribute_id\": 2, \"name\": \"" + str(
                                    marca.display_name) + "\", \"color_squares_rgb\": null, \"display_order\": 0 } },{ \"attribute_type_id\": 0, \"custom_value\": null, \"allow_filtering\": false, \"show_on_product_page\": true, \"display_order\": 1, \"attribute_type\": \"Option\",\"specification_attribute_option\": { \"specification_attribute_id\": 3, \"name\": \"" + str(
                                    subcategoria.display_name) + "\", \"color_squares_rgb\": null, \"display_order\": 0 } }]"
                            }
                        }

                        updateproduct = str(general_data[0].url) + '/api/products/' + str(rjson['products'][0]['id'])

                        json_obj3 = json.dumps(obj3)

                        rproduct = requests.put(updateproduct, data=json_obj3, headers=headers)

                except:
                    cantidad = 0
                    obj2 = {
                        "product": {
                            "name": str(self.name),
                            "short_description":str(self.short_description),
                            "full_description":"<strong>" + str(self.full_description) + "</strong>",
                            "stock_quantity": stock_quantity,
                            "disable_buy_button": self.disable_buy_button,
                            "price": str(self.list_price),
                            "old_price":str(self.old_price),
                            "published":str(self.published),
                            "weight":str(self.weight),
                            "length":str(self.length),
                            "width":str(self.width),
                            "height":str(self.height),
                            "product_id":str(self.product_id),
                            "category_id":str(self.category_id),
                            "category_name":str(self.category_name),
                            "sitio":str(self.sitio),
                            "sku":str(self.sku),
                            "product_cost":str(self.list_price)
                        }
                    }

                    json_obj2 = json.dumps(obj2)

                    createproduct = str(general_data[0].url) + '/api/products/'

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




class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    incrementables = fields.Float('% de Incrementables')

    @api.onchange('incrementables')
    def increment(self):

        incrementable = 0
        subtotal_proveedor = 0

        for line in self.order_line:
            vals = line._prepare_compute_all_values()

            if self.incrementables > 0:

                incrementable =  (vals['price_unit']*self.incrementables/100)

                unitario = vals['price_unit'] + incrementable

                subtotal_proveedor = vals['price_unit'] + incrementable

                vals.update({'price_unit': unitario, 'porcentaje':incrementable, 'subtotal_proveedor':subtotal_proveedor})


            taxes = line.taxes_id.compute_all(
            vals['price_unit'],
            vals['currency_id'],
            vals['product_qty'],
            vals['product'],
            vals['partner'])


            line.update({
                'porcentaje': incrementable * vals['product_qty'],
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal': (vals['price_unit'] * vals['product_qty']),
                'subtotal_proveedor':subtotal_proveedor *vals['product_qty'],
            })

            if line.move_ids.ids != []:

                all_records = self.env['stock.valuation.layer'].search([('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                all_records.value = taxes['total_excluded'] + incrementable + sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))

    @api.depends('order_line.price_total')
    def _amount_all(self):
        for order in self:
            amount_untaxed = amount_tax = porcentaje = subtotal_proveedor = 0.0
            for line in order.order_line:
                amount_untaxed += line.price_subtotal
                amount_tax += line.price_tax
                porcentaje += line.porcentaje
                subtotal_proveedor += line.subtotal_proveedor

                if order.currency_id.id != self.user_id.currency_id:

                    amount_untaxed = order.currency_id._convert(amount_untaxed, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                    amount_tax = order.currency_id._convert(amount_tax, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                    porcentaje = order.currency_id._convert(porcentaje, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                    subtotal_proveedor = order.currency_id._convert(subtotal_proveedor, self.user_id.currency_id, self.user_id.company_id, self.date_order)


                    line.price_subtotal =  amount_untaxed

                if line.move_ids.ids != []:
                    all_records = self.env['stock.valuation.layer'].search([('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                    all_records.value = amount_untaxed + amount_tax


            order.update({
                'amount_untaxed': order.currency_id.round(amount_untaxed),
                'amount_tax': order.currency_id.round(amount_tax),
                'amount_total': amount_untaxed + amount_tax,
            })



class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    porcentaje= fields.Float('Porcentaje')
    subtotal_proveedor = fields.Float('Sub Proveedor')

    @api.depends('product_qty', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        incrementable = 0
        subtotal_proveedor = 0
        for line in self:

            vals = line._prepare_compute_all_values()

            if self.order_id.incrementables > 0:
                incrementable = (vals['price_unit'] * self.order_id.incrementables / 100 )

                unitario = vals['price_unit'] + incrementable

                subtotal_proveedor = vals['price_unit'] + incrementable

                vals.update({'price_unit': unitario, 'porcentaje':incrementable, 'subtotal_proveedor':subtotal_proveedor})

            taxes = line.taxes_id.compute_all(
                vals['price_unit'],
                vals['currency_id'],
                vals['product_qty'],
                vals['product'],
                vals['partner'],
                vals['porcentaje'])


            line.update({
                'porcentaje': incrementable * vals['product_qty'],
                'price_tax': sum(t.get('amount', 0.0) for t in taxes.get('taxes', [])),
                'price_total': taxes['total_included'],
                'price_subtotal':(vals['price_unit'] * vals['product_qty']),
                'subtotal_proveedor':subtotal_proveedor *vals['product_qty'],
            })

            if line.move_ids.ids != []:

                all_records = self.env['stock.valuation.layer'].search([('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                all_records.value = taxes['total_excluded'] + incrementable + sum(t.get('amount', 0.0) for t in taxes.get('taxes', []))

        return line

    def _prepare_compute_all_values(self):
        # Hook method to returns the different argument values for the
        # compute_all method, due to the fact that discounts mechanism
        # is not implemented yet on the purchase orders.
        # This method should disappear as soon as this feature is
        # also introduced like in the sales module.
        self.ensure_one()
        return {
            'price_unit': self.price_unit,
            'currency_id': self.order_id.currency_id,
            'product_qty': self.product_qty,
            'product': self.product_id,
            'partner': self.order_id.partner_id,
            'porcentaje': self.porcentaje,
        }

class StockQuant(models.Model):
    _inherit = 'stock.quant'
    _description = 'Quants'
    _rec_name = 'product_id'

    def write(self, vals):
        """ Override to handle the "inventory mode" and create the inventory move. """
        if self._is_inventory_mode() and 'inventory_quantity' in vals:
            if any(quant.location_id.usage == 'inventory' for quant in self):
                # Do nothing when user tries to modify manually a inventory loss
                return
            allowed_fields = self._get_inventory_fields_write()
            if any([field for field in vals.keys() if field not in allowed_fields]):
                raise UserError(_("Quant's edition is restricted, you can't do this operation."))
            self = self.sudo()

            self.product_tmpl_id.qty_available = vals['inventory_quantity']
            self.product_tmpl_id.inventory_quantity = vals['inventory_quantity']

            return super(StockQuant, self).write(vals)
        return super(StockQuant, self).write(vals)


