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

    web_name = fields.Char(string='Nombre ss')
    short_description = fields.Text(string='Descripción corta')
    full_description = fields.Text(string='Descripción larga')
    stock_quantity = fields.Float(string='Cantidad en Inventario', related='qty_available')
    disable_buy_button = fields.Boolean('Habilita botón de compra')
    price = fields.Float(string='Precio de Venta', related='list_price')
    old_price = fields.Float(string='Precio anterior del producto')
    published = fields.Boolean('Publicado en Tecnofin')
    weight = fields.Float(string='Peso')
    length = fields.Float(string='Largo del equipo')
    width = fields.Float(string='Ancho del equipo')
    height = fields.Float(string='Alto del equipo ')
    product_id = fields.Integer()
    category_id = fields.Float('Familia')
    category_name = fields.Char('Familia')
    sitio = fields.Boolean(string='Integración en Tecnofin')
    sku = fields.Char(string='SKU')
    special_price = fields.Float(string='Precio especial', related='list_price')
    product_cost = fields.Float(string='Precio al costo del producto.', related='list_price')
    tag_ids = fields.Many2many('tags.zeigen')

    marca = fields.Many2one('marca.zeigen', 'Marca')
    subcategoria = fields.Many2one('subcategoria.zeigen','Subcategoría')
    marcasanatom = fields.Many2one('marcasanatom.zeigen', '	Marcas anatómicas')
    materiales = fields.Many2one('materiales.zeigen', 'Materiales')
    ojos = fields.Many2one('ojos.zeigen', 'Ojos')
    tipo = fields.Many2one('tipo.zeigen', '	Tipo')
    nivel = fields.Many2one('nivel.zeigen', 'Nivel')
    pulso = fields.Many2one('pulso.zeigen', 'Pulso')
    respiracion = fields.Many2one('respiracion.zeigen', 'Respiración')
    incluye = fields.Many2one('incluye.zeigen', 'Incluye')
    cuerpo = fields.Many2one('cuerpo.zeigen', 'Cuerpo')
    cabezal = fields.Many2one('cabezal.zeigen', 'Cabezal')
    velocidad = fields.Many2one('	velocidad.zeigen', 'Velocidad')
    desfibrilacio = fields.Many2one('desfibrilacio.zeigen', 'Desfibrilación')
    pecho = fields.Many2one('pecho.zeigen', 'Pecho')
    rtemp = fields.Many2one('rtemp.zeigen', 'Rango de temperaratura')
    tipcabezal = fields.Many2one('tipcabezal.zeigen', 'Tipo de cabezal')
    inccabezal = fields.Many2one('inccabezal.zeigen', 'Inclinación del cabezal')
    plato = fields.Many2one('plato.zeigen', 'Plato')
    auscult = fields.Many2one('auscult.zeigen', 'Auscultación')
    rcp = fields.Many2one('rcp.zeigen', 'RCP')
    tiempo = fields.Many2one('tiempo.zeigen', 'Tiempo')
    cabgir = fields.Many2one('cabgir.zeigen', 'Cabezal giratorio')
    ajusdiot = fields.Many2one('ajusdiot.zeigen', 'Ajuste de dioptrías')
    rango = fields.Many2one('rango.zeigen', 'Rango')
    pressang = fields.Many2one('pressang.zeigen', 'Presión sanguínea')
    reflejos = fields.Many2one('reflejos.zeigen', 'Reflejos')
    reproduc = fields.Many2one('	reproduc.zeigen', 'Reproductibilidad')
    ajusinterpu = fields.Many2one('ajusinterpu.zeigen', 'Ajuste interpupilar')
    oculares = fields.Many2one('oculares.zeigen', 'Oculares')
    errlin = fields.Many2one('errlin.zeigen', 'Error lineal')
    sindrom = fields.Many2one('sindrom.zeigen', 'Síndromes')
    fichpacien = fields.Many2one('fichpacien.zeigen', 'Fichas de pacientes')
    pothot = fields.Many2one('pothot.zeigen', 'Potencia de calentamiento')
    ocpris = fields.Many2one('ocpris.zeigen', 'Ocular con prisionero')
    revol = fields.Many2one('revol.zeigen', 'Revólver')
    dimtina = fields.Many2one('dimtina.zeigen', 'Dimensiones de tina')
    cian = fields.Many2one('cian.zeigen', 'Cianosis')
    bombinfu = fields.Many2one('	bombinfu.zeigen', 'Bompa de infusión')
    rotor = fields.Many2one('rotor.zeigen', 'Rotor')
    optica = fields.Many2one('optica.zeigen', 'Óptica')
    object = fields.Many2one('object.zeigen', 'Objetivos')
    motor = fields.Many2one('motor.zeigen', 'Motor')
    suda = fields.Many2one('suda.zeigen', 'Suda')
    llora = fields.Many2one('llora.zeigen', 'Llora')
    dimmanti = fields.Many2one('	dimmanti.zeigen', 'Dimensiones de mantilla')
    aumen = fields.Many2one('aumen.zeigen', 'Aumentos')
    enfo = fields.Many2one('enfo.zeigen', 'Enfoque')
    contrem = fields.Many2one('contrem.zeigen', 'Control remoto')
    table = fields.Many2one('table.zeigen', 'Tableta')
    anchband = fields.Many2one('anchband.zeigen', 'Ancho de banda')
    platina = fields.Many2one('platina.zeigen', 'Platina')
    tamplat = fields.Many2one('tamplat.zeigen', 'Tamaño de platina')
    sistopt = fields.Many2one('sistopt.zeigen', 'Sistema óptico')
    compu = fields.Many2one('compu.zeigen', 'Computadora')
    procsimu = fields.Many2one('procsimu.zeigen', 'Procedimientos simulados')
    rangfoto = fields.Many2one('	rangfoto.zeigen', '	Rango fotométrico')
    tope = fields.Many2one('tope.zeigen', 'Tope')
    conden = fields.Many2one('conden.zeigen', 'Condensador')
    alcalong = fields.Many2one('alcalong.zeigen', 'Alcance de longitud')
    conect = fields.Many2one('conect.zeigen', 'Conectividad')
    puntion = fields.Many2one('puntion.zeigen', 'Punción')
    alcafoto = fields.Many2one('alcafoto.zeigen', 'Alcance fotométrico')
    diafra = fields.Many2one('diafra.zeigen', 'Diafragma')
    portfilt = fields.Many2one('portfilt.zeigen', 'Porta filtros')
    prefoto = fields.Many2one('prefoto.zeigen', 'Precisión fotométrica')
    ecg = fields.Many2one('ecg.zeigen', 'ECG')
    traq = fields.Many2one('traq.zeigen', 'Traqueotomía')
    preslongond = fields.Many2one('preslongond.zeigen', 'Precisión de longitud de onda')
    contilum = fields.Many2one('contilum.zeigen', 'Control de iluminación')
    ilum = fields.Many2one('ilum.zeigen', 'Iluminación')
    reprodlongonda = fields.Many2one('reprodlongonda.zeigen', 'Reproductibilidad de longitud de onda')
    descomp = fields.Many2one('descomp.zeigen', 'Descompresión')
    voz = fields.Many2one('voz.zeigen', 'Voz')
    luzdisp = fields.Many2one('luzdisp.zeigen', 'Luz dispersa')
    kohler = fields.Many2one('	kohler.zeigen', 'Kohler')
    alimenelect = fields.Many2one('alimenelect.zeigen', 'Alimentación eléctrica')
    arrast = fields.Many2one('arrast.zeigen', 'Arrastre')
    manvias = fields.Many2one('manvias.zeigen', 'Manejo de vías aéreas')
    sistgast = fields.Many2one('sistgast.zeigen', 'Sistema gástrico')
    fuentluz = fields.Many2one('fuentluz.zeigen', 'Fuente de luz')
    camdig = fields.Many2one('camdig.zeigen', 'Cámara digital')
    filt = fields.Many2one('filt.zeigen', 'Filtros')
    voltout = fields.Many2one('voltout.zeigen', 'Voltaje de salida')
    sisturog = fields.Many2one('sisturog.zeigen', 'Sistema urogenital')
    cuidpacien = fields.Many2one('cuidpacien.zeigen', 'Cuidados del paciente')
    poten = fields.Many2one('poten.zeigen', 'Potencia')
    opccamposc = fields.Many2one('opccamposc.zeigen', 'Opción de campo obscuro')
    sistnerv = fields.Many2one('sistnerv.zeigen', 'Sistema nervioso')
    sistmet = fields.Many2one('sistmet.zeigen', 'Sistema metabólico')
    opcepiflo = fields.Many2one('opcepiflo.zeigen', 'Opción epiflourescencia')
    opccontfas = fields.Many2one('opccontfas.zeigen', 'Opción de contraste de fases')
    monidesem = fields.Many2one('monidesem.zeigen', 'Monitoreo de desempeño')
    disttrab = fields.Many2one('disttrab.zeigen', 'Distancia de trabajo')
    sistelev = fields.Many2one('sistelev.zeigen', 'Sistema de elevación')
    garantia = fields.Many2one('garantia.zeigen', 'Garantía')
    zoom = fields.Many2one('zoom.zeigen', 'Zoom')
    observaciones = fields.Many2one('observaciones.zeigen', 'Observaciones')
    capaci = fields.Many2one('capaci.zeigen', 'Capacidad')
    software = fields.Many2one('software.zeigen', 'Software')
    video = fields.Many2one('video.zeigen', 'Video')
    resolus = fields.Many2one('resolus.zeigen', 'Resolución')
    fuentalim = fields.Many2one('fuentalim.zeigen', 'Fuente de alimentación')
    sonidos = fields.Many2one('sonidos.zeigen', 'Sonidos')



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
                else:
                    short_description=''

                full_description = str(self.full_description)
                if vals.get('full_description'):
                    full_description = vals['full_description']
                else:
                    full_description = ''

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
                else:
                    category_id = ''

                category_name = str(self.category_name)
                if vals.get('category_name'):
                    category_name = vals['category_name']
                else:
                    category_name = ''

                sitio = str(self.sitio)
                if vals.get('sitio'):
                    sitio = vals['sitio']

                sku = str(self.sku)
                if vals.get('sku'):
                    sku = vals['sku']

                product_cost = str(self.product_cost)
                if vals.get('product_cost'):
                    product_cost = vals['product_cost']


                atributstr = [{"\"attribute_type_id\"": 0, "\"custom_value\"": 'null'
, "\"allow_filtering\"": 'false'
, "\"show_on_product_page\"": 'true'
, "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": { "\"specification_attribute_id\"": 1, "\"name\"": "\""+str(sku) +"\"", "\"color_squares_rgb\"": 'null'
, "\"display_order\"": 0 }}]


                marca = self.marca
                if vals.get('marca'):
                    id_marca = self.env['marca.zeigen'].search([('id', '=', vals['marca'])])
                    marca = id_marca[0]

                    marca_show = ''

                    if marca.show_on_product_page:
                        marca_show = "true"
                    else:
                        marca_show = "false"

                    marcastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": marca_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": marca.id_atribute,
                            "\"name\"": "\"" + str(marca.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(marcastr)

                subcategoria = self.subcategoria
                if vals.get('subcategoria'):
                    id_subcategoria = self.env['subcategoria.zeigen'].search([('id', '=', vals['subcategoria'])])
                    subcategoria = id_subcategoria[0]
                    subcategoriastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                       "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                       "\"specification_attribute_option\"": {
                                           "\"specification_attribute_id\"": subcategoria.id_atribute,
                                           "\"name\"": "\"" + str(subcategoria.display_name) + "\"",
                                           "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(subcategoriastr)

                marcasanatom = self.marcasanatom
                if vals.get('marcasanatom'):
                    id_marcasanatom = self.env['marcasanatom.zeigen'].search([('id', '=', vals['marcasanatom'])])
                    marcasanatom = id_marcasanatom[0]
                    marcasanatomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                       "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                       "\"specification_attribute_option\"": {
                                           "\"specification_attribute_id\"": marcasanatom.id_atribute,
                                           "\"name\"": "\"" + str(marcasanatom.display_name) + "\"",
                                           "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(marcasanatomstr)

                materiales = self.materiales
                if vals.get('materiales'):
                    id_materiales = self.env['materiales.zeigen'].search([('id', '=', vals['materiales'])])
                    materiales = id_materiales[0]
                    materialesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": materiales.id_atribute,
                                         "\"name\"": "\"" + str(materiales.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(materialesstr)

                ojos = self.ojos
                if vals.get('ojos'):
                    id_ojos = self.env['ojos.zeigen'].search([('id', '=', vals['ojos'])])
                    ojos = id_
                    ojos[0]
                    ojosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": ojos.id_atribute,
                            "\"name\"": "\"" + str(ojos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ojosstr)

                tipo = self.tipo
                if vals.get('tipo'):
                    id_tipo = self.env['tipo.zeigen'].search([('id', '=', vals['tipo'])])
                    tipo = id_tipo[0]
                    tipostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": tipo.id_atribute,
                            "\"name\"": "\"" + str(tipo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tipostr)

                nivel = self.nivel
                if vals.get('nivel'):
                    id_nivel = self.env['nivel.zeigen'].search([('id', '=', vals['nivel'])])
                    nivel = id_nivel[0]
                    nivelstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": nivel.id_atribute,
                            "\"name\"": "\"" + str(nivel.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(nivelstr)

                pulso = self.pulso
                if vals.get('pulso'):
                    id_pulso = self.env['pulso.zeigen'].search([('id', '=', vals['pulso'])])
                    pulso = id_pulso[0]
                    pulsostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": pulso.id_atribute,
                            "\"name\"": "\"" + str(pulso.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pulsostr)

                respiracion = self.respiracion
                if vals.get('respiracion'):
                    id_respiracion = self.env['respiracion.zeigen'].search([('id', '=', vals['respiracion'])])
                    respiracion = id_respiracion[0]
                    respiracionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                      "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                      "\"specification_attribute_option\"": {
                                          "\"specification_attribute_id\"": respiracion.id_atribute,
                                          "\"name\"": "\"" + str(respiracion.display_name) + "\"",
                                          "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(respiracionstr)

                incluye = self.incluye
                if vals.get('incluye'):
                    id_incluye = self.env['incluye.zeigen'].search([('id', '=', vals['incluye'])])
                    incluye = id_incluye[0]
                    incluyestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": incluye.id_atribute,
                                      "\"name\"": "\"" + str(incluye.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(incluyestr)

                cabezal = self.cabezal
                if vals.get('cabezal'):
                    id_cabezal = self.env['cabezal.zeigen'].search([('id', '=', vals['cabezal'])])
                    cabezal = id_cabezal[0]
                    cabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": cabezal.id_atribute,
                                      "\"name\"": "\"" + str(cabezal.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(cabezalstr)

                velocidad = self.velocidad
                if vals.get('velocidad'):
                    id_velocidad = self.env['velocidad.zeigen'].search([('id', '=', vals['velocidad'])])
                    velocidad = id_velocidad[0]
                    velocidadstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                    "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                    "\"specification_attribute_option\"": {
                                        "\"specification_attribute_id\"": velocidad.id_atribute,
                                        "\"name\"": "\"" + str(velocidad.display_name) + "\"",
                                        "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(velocidadstr)

                desfibrilacio = self.desfibrilacio
                if vals.get('desfibrilacio'):
                    id_desfibrilacio = self.env['desfibrilacio.zeigen'].search([('id', '=', vals['desfibrilacio'])])
                    desfibrilacio = id_desfibrilacio[0]
                    desfibrilaciostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                        "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                        "\"specification_attribute_option\"": {
                                            "\"specification_attribute_id\"": desfibrilacio.id_atribute,
                                            "\"name\"": "\"" + str(desfibrilacio.display_name) + "\"",
                                            "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(desfibrilaciostr)

                pecho = self.pecho
                if vals.get('pecho'):
                    id_pecho = self.env['pecho.zeigen'].search([('id', '=', vals['pecho'])])
                    pecho = id_pecho[0]
                    pechostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": pecho.id_atribute,
                            "\"name\"": "\"" + str(pecho.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pechostr)

                rtemp = self.rtemp
                if vals.get('rtemp'):
                    id_rtemp = self.env['rtemp.zeigen'].search([('id', '=', vals['rtemp'])])
                    rtemp = id_rtemp[0]
                    rtempstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": rtemp.id_atribute,
                            "\"name\"": "\"" + str(rtemp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rtempstr)

                tipcabezal = self.tipcabezal
                if vals.get('tipcabezal'):
                    id_tipcabezal = self.env['tipcabezal.zeigen'].search([('id', '=', vals['tipcabezal'])])
                    tipcabezal = id_tipcabezal[0]
                    tipcabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": tipcabezal.id_atribute,
                                         "\"name\"": "\"" + str(tipcabezal.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(tipcabezalstr)

                inccabezal = self.inccabezal
                if vals.get('inccabezal'):
                    id_inccabezal = self.env['inccabezal.zeigen'].search([('id', '=', vals['inccabezal'])])
                    inccabezal = id_inccabezal[0]
                    inccabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": inccabezal.id_atribute,
                                         "\"name\"": "\"" + str(inccabezal.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(inccabezalstr)

                plato = self.plato
                if vals.get('plato'):
                    id_plato = self.env['plato.zeigen'].search([('id', '=', vals['plato'])])
                    plato = id_plato[0]
                    platostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": plato.id_atribute,
                            "\"name\"": "\"" + str(plato.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(platostr)

                auscult = self.auscult
                if vals.get('auscult'):
                    id_auscult = self.env['auscult.zeigen'].search([('id', '=', vals['auscult'])])
                    auscult = id_auscult[0]
                    auscultstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": auscult.id_atribute,
                                      "\"name\"": "\"" + str(auscult.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(auscultstr)

                rcp = self.rcp
                if vals.get('rcp'):
                    id_rcp = self.env['rcp.zeigen'].search([('id', '=', vals['rcp'])])
                    rcp = id_rcp[0]
                    rcpstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"",
                              "\"specification_attribute_option\"": {"\"specification_attribute_id\"": rcp.id_atribute,
                                                                     "\"name\"": "\"" + str(rcp.display_name) + "\"",
                                                                     "\"color_squares_rgb\"": 'null',
                                                                     "\"display_order\"": 0}}

                    atributstr.append(rcpstr)

                tiempo = self.tiempo
                if vals.get('tiempo'):
                    id_tiempo = self.env['tiempo.zeigen'].search([('id', '=', vals['tiempo'])])
                    tiempo = id_tiempo[0]
                    tiempostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": tiempo.id_atribute,
                            "\"name\"": "\"" + str(tiempo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tiempostr)

                cabgir = self.cabgir
                if vals.get('cabgir'):
                    id_cabgir = self.env['cabgir.zeigen'].search([('id', '=', vals['cabgir'])])
                    cabgir = id_cabgir[0]
                    cabgirstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": cabgir.id_atribute,
                            "\"name\"": "\"" + str(cabgir.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cabgirstr)

                ajusdiot = self.ajusdiot
                if vals.get('ajusdiot'):
                    id_ajusdiot = self.env['ajusdiot.zeigen'].search([('id', '=', vals['ajusdiot'])])
                    ajusdiot = id_ajusdiot[0]
                    ajusdiotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": ajusdiot.id_atribute,
                                       "\"name\"": "\"" + str(ajusdiot.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(ajusdiotstr)

                rango = self.rango
                if vals.get('rango'):
                    id_rango = self.env['rango.zeigen'].search([('id', '=', vals['rango'])])
                    rango = id_rango[0]
                    rangostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": rango.id_atribute,
                            "\"name\"": "\"" + str(rango.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rangostr)

                pressang = self.pressang
                if vals.get('pressang'):
                    id_pressang = self.env['pressang.zeigen'].search([('id', '=', vals['pressang'])])
                    pressang = id_pressang[0]
                    pressangstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": pressang.id_atribute,
                                       "\"name\"": "\"" + str(pressang.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(pressangstr)

                reflejos = self.reflejos
                if vals.get('reflejos'):
                    id_reflejos = self.env['reflejos.zeigen'].search([('id', '=', vals['reflejos'])])
                    reflejos = id_reflejos[0]
                    reflejosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": reflejos.id_atribute,
                                       "\"name\"": "\"" + str(reflejos.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(reflejosstr)

                reproduc = self.reproduc
                if vals.get('reproduc'):
                    id_reproduc = self.env['reproduc.zeigen'].search([('id', '=', vals['reproduc'])])
                    reproduc = id_reproduc[0]
                    reproducstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": reproduc.id_atribute,
                                       "\"name\"": "\"" + str(reproduc.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(reproducstr)

                ajusinterpu = self.ajusinterpu
                if vals.get('ajusinterpu'):
                    id_ajusinterpu = self.env['ajusinterpu.zeigen'].search([('id', '=', vals['ajusinterpu'])])
                    ajusinterpu = id_ajusinterpu[0]
                    ajusinterpustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                      "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                      "\"specification_attribute_option\"": {
                                          "\"specification_attribute_id\"": ajusinterpu.id_atribute,
                                          "\"name\"": "\"" + str(ajusinterpu.display_name) + "\"",
                                          "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(ajusinterpustr)

                oculares = self.oculares
                if vals.get('oculares'):
                    id_oculares = self.env['oculares.zeigen'].search([('id', '=', vals['oculares'])])
                    oculares = id_oculares[0]
                    ocularesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": oculares.id_atribute,
                                       "\"name\"": "\"" + str(oculares.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(ocularesstr)

                errlin = self.errlin
                if vals.get('errlin'):
                    id_errlin = self.env['errlin.zeigen'].search([('id', '=', vals['errlin'])])
                    errlin = id_errlin[0]
                    errlinstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": errlin.id_atribute,
                            "\"name\"": "\"" + str(errlin.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(errlinstr)

                sindrom = self.sindrom
                if vals.get('sindrom'):
                    id_sindrom = self.env['sindrom.zeigen'].search([('id', '=', vals['sindrom'])])
                    sindrom = id_sindrom[0]
                    sindromstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": sindrom.id_atribute,
                                      "\"name\"": "\"" + str(sindrom.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sindromstr)

                fichpacien = self.fichpacien
                if vals.get('fichpacien'):
                    id_fichpacien = self.env['fichpacien.zeigen'].search([('id', '=', vals['fichpacien'])])
                    fichpacien = id_fichpacien[0]
                    fichpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": fichpacien.id_atribute,
                                         "\"name\"": "\"" + str(fichpacien.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(fichpacienstr)

                pothot = self.pothot
                if vals.get('pothot'):
                    id_pothot = self.env['pothot.zeigen'].search([('id', '=', vals['pothot'])])
                    pothot = id_pothot[0]
                    pothotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": pothot.id_atribute,
                            "\"name\"": "\"" + str(pothot.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pothotstr)

                ocpris = self.ocpris
                if vals.get('ocpris'):
                    id_ocpris = self.env['ocpris.zeigen'].search([('id', '=', vals['ocpris'])])
                    ocpris = id_ocpris[0]
                    ocprisstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": ocpris.id_atribute,
                            "\"name\"": "\"" + str(ocpris.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ocprisstr)

                revol = self.revol
                if vals.get('revol'):
                    id_revol = self.env['revol.zeigen'].search([('id', '=', vals['revol'])])
                    revol = id_revol[0]
                    revolstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": revol.id_atribute,
                            "\"name\"": "\"" + str(revol.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(revolstr)

                dimtina = self.dimtina
                if vals.get('dimtina'):
                    id_dimtina = self.env['dimtina.zeigen'].search([('id', '=', vals['dimtina'])])
                    dimtina = id_dimtina[0]
                    dimtinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": dimtina.id_atribute,
                                      "\"name\"": "\"" + str(dimtina.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(dimtinastr)

                cian = self.cian
                if vals.get('cian'):
                    id_cian = self.env['cian.zeigen'].search([('id', '=', vals['cian'])])
                    cian = id_cian[0]
                    cianstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": cian.id_atribute,
                            "\"name\"": "\"" + str(cian.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cianstr)

                bombinfu = self.bombinfu
                if vals.get('bombinfu'):
                    id_bombinfu = self.env['bombinfu.zeigen'].search([('id', '=', vals['bombinfu'])])
                    bombinfu = id_bombinfu[0]
                    bombinfustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": bombinfu.id_atribute,
                                       "\"name\"": "\"" + str(bombinfu.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(bombinfustr)

                rotor = self.rotor
                if vals.get('rotor'):
                    id_rotor = self.env['rotor.zeigen'].search([('id', '=', vals['rotor'])])
                    rotor = id_rotor[0]
                    rotorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": rotor.id_atribute,
                            "\"name\"": "\"" + str(rotor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rotorstr)

                optica = self.optica
                if vals.get('optica'):
                    id_optica = self.env['optica.zeigen'].search([('id', '=', vals['optica'])])
                    optica = id_optica[0]
                    opticastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": optica.id_atribute,
                            "\"name\"": "\"" + str(optica.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opticastr)

                object = self.object
                if vals.get('object'):
                    id_object = self.env['object.zeigen'].search([('id', '=', vals['object'])])
                    object = id_object[0]
                    objectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": object.id_atribute,
                            "\"name\"": "\"" + str(object.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(objectstr)

                motor = self.motor
                if vals.get('motor'):
                    id_motor = self.env['motor.zeigen'].search([('id', '=', vals['motor'])])
                    motor = id_motor[0]
                    motorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": motor.id_atribute,
                            "\"name\"": "\"" + str(motor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(motorstr)

                suda = self.suda
                if vals.get('suda'):
                    id_suda = self.env['suda.zeigen'].search([('id', '=', vals['suda'])])
                    suda = id_suda[0]
                    sudastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": suda.id_atribute,
                            "\"name\"": "\"" + str(suda.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sudastr)

                llora = self.llora
                if vals.get('llora'):
                    id_llora = self.env['llora.zeigen'].search([('id', '=', vals['llora'])])
                    llora = id_llora[0]
                    llorastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": llora.id_atribute,
                            "\"name\"": "\"" + str(llora.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(llorastr)

                dimmanti = self.dimmanti
                if vals.get('dimmanti'):
                    id_dimmanti = self.env['dimmanti.zeigen'].search([('id', '=', vals['dimmanti'])])
                    dimmanti = id_dimmanti[0]
                    dimmantistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": dimmanti.id_atribute,
                                       "\"name\"": "\"" + str(dimmanti.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(dimmantistr)

                aumen = self.aumen
                if vals.get('aumen'):
                    id_aumen = self.env['aumen.zeigen'].search([('id', '=', vals['aumen'])])
                    aumen = id_aumen[0]
                    aumenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": aumen.id_atribute,
                            "\"name\"": "\"" + str(aumen.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(aumenstr)

                enfo = self.enfo
                if vals.get('enfo'):
                    id_enfo = self.env['enfo.zeigen'].search([('id', '=', vals['enfo'])])
                    enfo = id_enfo[0]
                    enfostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": enfo.id_atribute,
                            "\"name\"": "\"" + str(enfo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(enfostr)

                contrem = self.contrem
                if vals.get('contrem'):
                    id_contrem = self.env['contrem.zeigen'].search([('id', '=', vals['contrem'])])
                    contrem = id_contrem[0]
                    contremstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": contrem.id_atribute,
                                      "\"name\"": "\"" + str(contrem.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(contremstr)

                table = self.table
                if vals.get('table'):
                    id_table = self.env['table.zeigen'].search([('id', '=', vals['table'])])
                    table = id_table[0]
                    tablestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": table.id_atribute,
                            "\"name\"": "\"" + str(table.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tablestr)

                anchband = self.anchband
                if vals.get('anchband'):
                    id_anchband = self.env['anchband.zeigen'].search([('id', '=', vals['anchband'])])
                    anchband = id_anchband[0]
                    anchbandstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": anchband.id_atribute,
                                       "\"name\"": "\"" + str(anchband.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(anchbandstr)

                platina = self.platina
                if vals.get('platina'):
                    id_platina = self.env['platina.zeigen'].search([('id', '=', vals['platina'])])
                    platina = id_platina[0]
                    platinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": platina.id_atribute,
                                      "\"name\"": "\"" + str(platina.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(platinastr)

                tamplat = self.tamplat
                if vals.get('tamplat'):
                    id_tamplat = self.env['tamplat.zeigen'].search([('id', '=', vals['tamplat'])])
                    tamplat = id_tamplat[0]
                    tamplatstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": tamplat.id_atribute,
                                      "\"name\"": "\"" + str(tamplat.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(tamplatstr)

                sistopt = self.sistopt
                if vals.get('sistopt'):
                    id_sistopt = self.env['sistopt.zeigen'].search([('id', '=', vals['sistopt'])])
                    sistopt = id_sistopt[0]
                    sistoptstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": sistopt.id_atribute,
                                      "\"name\"": "\"" + str(sistopt.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sistoptstr)

                compu = self.compu
                if vals.get('compu'):
                    id_compu = self.env['compu.zeigen'].search([('id', '=', vals['compu'])])
                    compu = id_compu[0]
                    compustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": compu.id_atribute,
                            "\"name\"": "\"" + str(compu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(compustr)

                procsimu = self.procsimu
                if vals.get('procsimu'):
                    id_procsimu = self.env['procsimu.zeigen'].search([('id', '=', vals['procsimu'])])
                    procsimu = id_procsimu[0]
                    procsimustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": procsimu.id_atribute,
                                       "\"name\"": "\"" + str(procsimu.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(procsimustr)

                rangfoto = self.rangfoto
                if vals.get('rangfoto'):
                    id_rangfoto = self.env['rangfoto.zeigen'].search([('id', '=', vals['rangfoto'])])
                    rangfoto = id_rangfoto[0]
                    rangfotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": rangfoto.id_atribute,
                                       "\"name\"": "\"" + str(rangfoto.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(rangfotostr)

                tope = self.tope
                if vals.get('tope'):
                    id_tope = self.env['tope.zeigen'].search([('id', '=', vals['tope'])])
                    tope = id_tope[0]
                    topestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": tope.id_atribute,
                            "\"name\"": "\"" + str(tope.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(topestr)

                conden = self.conden
                if vals.get('conden'):
                    id_conden = self.env['conden.zeigen'].search([('id', '=', vals['conden'])])
                    conden = id_conden[0]
                    condenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": conden.id_atribute,
                            "\"name\"": "\"" + str(conden.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(condenstr)

                alcalong = self.alcalong
                if vals.get('alcalong'):
                    id_alcalong = self.env['alcalong.zeigen'].search([('id', '=', vals['alcalong'])])
                    alcalong = id_alcalong[0]
                    alcalongstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": alcalong.id_atribute,
                                       "\"name\"": "\"" + str(alcalong.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(alcalongstr)

                conect = self.conect
                if vals.get('conect'):
                    id_conect = self.env['conect.zeigen'].search([('id', '=', vals['conect'])])
                    conect = id_conect[0]
                    conectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": conect.id_atribute,
                            "\"name\"": "\"" + str(conect.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(conectstr)

                puntion = self.puntion
                if vals.get('puntion'):
                    id_puntion = self.env['puntion.zeigen'].search([('id', '=', vals['puntion'])])
                    puntion = id_puntion[0]
                    puntionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": puntion.id_atribute,
                                      "\"name\"": "\"" + str(puntion.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(puntionstr)

                alcafoto = self.alcafoto
                if vals.get('alcafoto'):
                    id_alcafoto = self.env['alcafoto.zeigen'].search([('id', '=', vals['alcafoto'])])
                    alcafoto = id_alcafoto[0]
                    alcafotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": alcafoto.id_atribute,
                                       "\"name\"": "\"" + str(alcafoto.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(alcafotostr)

                diafra = self.diafra
                if vals.get('diafra'):
                    id_diafra = self.env['diafra.zeigen'].search([('id', '=', vals['diafra'])])
                    diafra = id_diafra[0]
                    diafrastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": diafra.id_atribute,
                            "\"name\"": "\"" + str(diafra.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(diafrastr)

                portfilt = self.portfilt
                if vals.get('portfilt'):
                    id_portfilt = self.env['portfilt.zeigen'].search([('id', '=', vals['portfilt'])])
                    portfilt = id_portfilt[0]
                    portfiltstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": portfilt.id_atribute,
                                       "\"name\"": "\"" + str(portfilt.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(portfiltstr)

                prefoto = self.prefoto
                if vals.get('prefoto'):
                    id_prefoto = self.env['prefoto.zeigen'].search([('id', '=', vals['prefoto'])])
                    prefoto = id_prefoto[0]
                    prefotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": prefoto.id_atribute,
                                      "\"name\"": "\"" + str(prefoto.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(prefotostr)

                ecg = self.ecg
                if vals.get('ecg'):
                    id_ecg = self.env['ecg.zeigen'].search([('id', '=', vals['ecg'])])
                    ecg = id_ecg[0]
                    ecgstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"",
                              "\"specification_attribute_option\"": {"\"specification_attribute_id\"": ecg.id_atribute,
                                                                     "\"name\"": "\"" + str(ecg.display_name) + "\"",
                                                                     "\"color_squares_rgb\"": 'null',
                                                                     "\"display_order\"": 0}}

                    atributstr.append(ecgstr)

                traq = self.traq
                if vals.get('traq'):
                    id_traq = self.env['traq.zeigen'].search([('id', '=', vals['traq'])])
                    traq = id_traq[0]
                    traqstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": traq.id_atribute,
                            "\"name\"": "\"" + str(traq.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(traqstr)

                preslongond = self.preslongond
                if vals.get('preslongond'):
                    id_preslongond = self.env['preslongond.zeigen'].search([('id', '=', vals['preslongond'])])
                    preslongond = id_
                    preslongond[0]
                    preslongondstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                      "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                      "\"specification_attribute_option\"": {
                                          "\"specification_attribute_id\"": preslongond.id_atribute,
                                          "\"name\"": "\"" + str(preslongond.display_name) + "\"",
                                          "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(preslongondstr)

                contilum = self.contilum
                if vals.get('contilum'):
                    id_contilum = self.env['contilum.zeigen'].search([('id', '=', vals['contilum'])])
                    contilum = id_contilum[0]
                    contilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": contilum.id_atribute,
                                       "\"name\"": "\"" + str(contilum.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(contilumstr)

                ilum = self.ilum
                if vals.get('ilum'):
                    id_ilum = self.env['ilum.zeigen'].search([('id', '=', vals['ilum'])])
                    ilum = id_ilum[0]
                    ilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": ilum.id_atribute,
                            "\"name\"": "\"" + str(ilum.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ilumstr)

                reprodlongonda = self.reprodlongonda
                if vals.get('reprodlongonda'):
                    id_reprodlongonda = self.env['reprodlongonda.zeigen'].search([('id', '=', vals['reprodlongonda'])])
                    reprodlongonda = id_reprodlongonda[0]
                    reprodlongondastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                         "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                         "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                         "\"specification_attribute_option\"": {
                                             "\"specification_attribute_id\"": reprodlongonda.id_atribute,
                                             "\"name\"": "\"" + str(reprodlongonda.display_name) + "\"",
                                             "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(reprodlongondastr)

                descomp = self.descomp
                if vals.get('descomp'):
                    id_descomp = self.env['descomp.zeigen'].search([('id', '=', vals['descomp'])])
                    descomp = id_descomp[0]
                    descompstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": descomp.id_atribute,
                                      "\"name\"": "\"" + str(descomp.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(descompstr)

                voz = self.voz
                if vals.get('voz'):
                    id_voz = self.env['	voz.zeigen'].search([('id', '=', vals['voz'])])
                    voz = id_voz[0]
                    vozstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"",
                              "\"specification_attribute_option\"": {"\"specification_attribute_id\"": voz.id_atribute,
                                                                     "\"name\"": "\"" + str(voz.display_name) + "\"",
                                                                     "\"color_squares_rgb\"": 'null',
                                                                     "\"display_order\"": 0}}

                    atributstr.append(vozstr)

                luzdisp = self.luzdisp
                if vals.get('luzdisp'):
                    id_luzdisp = self.env['luzdisp.zeigen'].search([('id', '=', vals['luzdisp'])])
                    luzdisp = id_luzdisp[0]
                    luzdispstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": luzdisp.id_atribute,
                                      "\"name\"": "\"" + str(luzdisp.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(luzdispstr)

                kohler = self.kohler
                if vals.get('kohler'):
                    id_kohler = self.env['kohler.zeigen'].search([('id', '=', vals['kohler'])])
                    kohler = id_kohler[0]
                    kohlerstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": kohler.id_atribute,
                            "\"name\"": "\"" + str(kohler.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(kohlerstr)

                alimenelect = self.alimenelect
                if vals.get('alimenelect'):
                    id_alimenelect = self.env['alimenelect.zeigen'].search([('id', '=', vals['alimenelect'])])
                    alimenelect = id_alimenelect[0]
                    alimenelectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                      "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                      "\"specification_attribute_option\"": {
                                          "\"specification_attribute_id\"": alimenelect.id_atribute,
                                          "\"name\"": "\"" + str(alimenelect.display_name) + "\"",
                                          "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(alimenelectstr)

                arrast = self.arrast
                if vals.get('arrast'):
                    id_arrast = self.env['arrast.zeigen'].search([('id', '=', vals['arrast'])])
                    arrast = id_arrast[0]
                    arraststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": arrast.id_atribute,
                            "\"name\"": "\"" + str(arrast.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(arraststr)

                manvias = self.manvias
                if vals.get('manvias'):
                    id_manvias = self.env['manvias.zeigen'].search([('id', '=', vals['manvias'])])
                    manvias = id_manvias[0]
                    manviasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": manvias.id_atribute,
                                      "\"name\"": "\"" + str(manvias.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(manviasstr)

                sistgast = self.sistgast
                if vals.get('sistgast'):
                    id_sistgast = self.env['sistgast.zeigen'].search([('id', '=', vals['sistgast'])])
                    sistgast = id_sistgast[0]
                    sistgaststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": sistgast.id_atribute,
                                       "\"name\"": "\"" + str(sistgast.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sistgaststr)

                fuentluz = self.fuentluz
                if vals.get('fuentluz'):
                    id_fuentluz = self.env['fuentluz.zeigen'].search([('id', '=', vals['fuentluz'])])
                    fuentluz = id_fuentluz[0]
                    fuentluzstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": fuentluz.id_atribute,
                                       "\"name\"": "\"" + str(fuentluz.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(fuentluzstr)

                camdig = self.camdig
                if vals.get('camdig'):
                    id_camdig = self.env['camdig.zeigen'].search([('id', '=', vals['camdig'])])
                    camdig = id_camdig[0]
                    camdigstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": camdig.id_atribute,
                            "\"name\"": "\"" + str(camdig.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(camdigstr)

                filt = self.filt
                if vals.get('filt'):
                    id_filt = self.env['filt.zeigen'].search([('id', '=', vals['filt'])])
                    filt = id_filt[0]
                    filtstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": filt.id_atribute,
                            "\"name\"": "\"" + str(filt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(filtstr)

                voltout = self.voltout
                if vals.get('voltout'):
                    id_voltout = self.env['voltout.zeigen'].search([('id', '=', vals['voltout'])])
                    voltout = id_voltout[0]
                    voltoutstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": voltout.id_atribute,
                                      "\"name\"": "\"" + str(voltout.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(voltoutstr)

                sisturog = self.sisturog
                if vals.get('sisturog'):
                    id_sisturog = self.env['sisturog.zeigen'].search([('id', '=', vals['sisturog'])])
                    sisturog = id_sisturog[0]
                    sisturogstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": sisturog.id_atribute,
                                       "\"name\"": "\"" + str(sisturog.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sisturogstr)

                cuidpacien = self.cuidpacien
                if vals.get('cuidpacien'):
                    id_cuidpacien = self.env['cuidpacien.zeigen'].search([('id', '=', vals['cuidpacien'])])
                    cuidpacien = id_cuidpacien[0]
                    cuidpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": cuidpacien.id_atribute,
                                         "\"name\"": "\"" + str(cuidpacien.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(cuidpacienstr)

                poten = self.poten
                if vals.get('poten'):
                    id_poten = self.env['poten.zeigen'].search([('id', '=', vals['poten'])])
                    poten = id_poten[0]
                    potenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": poten.id_atribute,
                            "\"name\"": "\"" + str(poten.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(potenstr)

                opccamposc = self.opccamposc
                if vals.get('opccamposc'):
                    id_opccamposc = self.env['opccamposc.zeigen'].search([('id', '=', vals['opccamposc'])])
                    opccamposc = id_
                    opccamposc[0]
                    opccamposcstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": opccamposc.id_atribute,
                                         "\"name\"": "\"" + str(opccamposc.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(opccamposcstr)

                sistnerv = self.sistnerv
                if vals.get('sistnerv'):
                    id_sistnerv = self.env['sistnerv.zeigen'].search([('id', '=', vals['sistnerv'])])
                    sistnerv = id_sistnerv[0]
                    sistnervstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": sistnerv.id_atribute,
                                       "\"name\"": "\"" + str(sistnerv.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sistnervstr)

                sistmet = self.sistmet
                if vals.get('sistmet'):
                    id_sistmet = self.env['sistmet.zeigen'].search([('id', '=', vals['sistmet'])])
                    sistmet = id_sistmet[0]
                    sistmetstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": sistmet.id_atribute,
                                      "\"name\"": "\"" + str(sistmet.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sistmetstr)

                opcepiflo = self.opcepiflo
                if vals.get('opcepiflo'):
                    id_opcepiflo = self.env['opcepiflo.zeigen'].search([('id', '=', vals['opcepiflo'])])
                    opcepiflo = id_opcepiflo[0]
                    opcepiflostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                    "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                    "\"specification_attribute_option\"": {
                                        "\"specification_attribute_id\"": opcepiflo.id_atribute,
                                        "\"name\"": "\"" + str(opcepiflo.display_name) + "\"",
                                        "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(opcepiflostr)

                opccontfas = self.opccontfas
                if vals.get('opccontfas'):
                    id_opccontfas = self.env['opccontfas.zeigen'].search([('id', '=', vals['opccontfas'])])
                    opccontfas = id_opccontfas[0]
                    opccontfasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                     "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                     "\"specification_attribute_option\"": {
                                         "\"specification_attribute_id\"": opccontfas.id_atribute,
                                         "\"name\"": "\"" + str(opccontfas.display_name) + "\"",
                                         "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(opccontfasstr)

                monidesem = self.monidesem
                if vals.get('monidesem'):
                    id_monidesem = self.env['monidesem.zeigen'].search([('id', '=', vals['monidesem'])])
                    monidesem = id_monidesem[0]
                    monidesemstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                    "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                    "\"specification_attribute_option\"": {
                                        "\"specification_attribute_id\"": monidesem.id_atribute,
                                        "\"name\"": "\"" + str(monidesem.display_name) + "\"",
                                        "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(monidesemstr)

                disttrab = self.disttrab
                if vals.get('disttrab'):
                    id_disttrab = self.env['disttrab.zeigen'].search([('id', '=', vals['disttrab'])])
                    disttrab = id_disttrab[0]
                    disttrabstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": disttrab.id_atribute,
                                       "\"name\"": "\"" + str(disttrab.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(disttrabstr)

                sistelev = self.sistelev
                if vals.get('sistelev'):
                    id_sistelev = self.env['sistelev.zeigen'].search([('id', '=', vals['sistelev'])])
                    sistelev = id_sistelev[0]
                    sistelevstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": sistelev.id_atribute,
                                       "\"name\"": "\"" + str(sistelev.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sistelevstr)

                garantia = self.garantia
                if vals.get('garantia'):
                    id_garantia = self.env['garantia.zeigen'].search([('id', '=', vals['garantia'])])
                    garantia = id_garantia[0]
                    garantiastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": garantia.id_atribute,
                                       "\"name\"": "\"" + str(garantia.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(garantiastr)

                zoom = self.zoom
                if vals.get('zoom'):
                    id_zoom = self.env['zoom.zeigen'].search([('id', '=', vals['zoom'])])
                    zoom = id_zoom[0]
                    zoomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": zoom.id_atribute,
                            "\"name\"": "\"" + str(zoom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(zoomstr)

                observaciones = self.observaciones
                if vals.get('observaciones'):
                    id_observaciones = self.env['observaciones.zeigen'].search([('id', '=', vals['observaciones'])])
                    observaciones = id_observaciones[0]
                    observacionesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                        "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                        "\"specification_attribute_option\"": {
                                            "\"specification_attribute_id\"": observaciones.id_atribute,
                                            "\"name\"": "\"" + str(observaciones.display_name) + "\"",
                                            "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(observacionesstr)

                capaci = self.capaci
                if vals.get('capaci'):
                    id_capaci = self.env['capaci.zeigen'].search([('id', '=', vals['capaci'])])
                    capaci = id_capaci[0]
                    capacistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": capaci.id_atribute,
                            "\"name\"": "\"" + str(capaci.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(capacistr)

                software = self.software
                if vals.get('software'):
                    id_software = self.env['software.zeigen'].search([('id', '=', vals['software'])])
                    software = id_software[0]
                    softwarestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                   "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                   "\"specification_attribute_option\"": {
                                       "\"specification_attribute_id\"": software.id_atribute,
                                       "\"name\"": "\"" + str(software.display_name) + "\"",
                                       "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(softwarestr)

                video = self.video
                if vals.get('video'):
                    id_video = self.env['video.zeigen'].search([('id', '=', vals['video'])])
                    video = id_video[0]
                    videostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": video.id_atribute,
                            "\"name\"": "\"" + str(video.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(videostr)

                resolus = self.resolus
                if vals.get('resolus'):
                    id_resolus = self.env['resolus.zeigen'].search([('id', '=', vals['resolus'])])
                    resolus = id_resolus[0]
                    resolusstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": resolus.id_atribute,
                                      "\"name\"": "\"" + str(resolus.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(resolusstr)

                fuentalim = self.fuentalim
                if vals.get('fuentalim'):
                    id_fuentalim = self.env['fuentalim.zeigen'].search([('id', '=', vals['fuentalim'])])
                    fuentalim = id_fuentalim[0]
                    fuentalimstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                    "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                    "\"specification_attribute_option\"": {
                                        "\"specification_attribute_id\"": fuentalim.id_atribute,
                                        "\"name\"": "\"" + str(fuentalim.display_name) + "\"",
                                        "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(fuentalimstr)

                sonidos = self.sonidos
                if vals.get('sonidos'):
                    id_sonidos = self.env['sonidos.zeigen'].search([('id', '=', vals['sonidos'])])
                    sonidos = id_sonidos[0]
                    sonidosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false', "\"show_on_product_page\"": 'true',
                                  "\"display_order\"": 1, "\"attribute_type\"": "\"Option\"",
                                  "\"specification_attribute_option\"": {
                                      "\"specification_attribute_id\"": sonidos.id_atribute,
                                      "\"name\"": "\"" + str(sonidos.display_name) + "\"",
                                      "\"color_squares_rgb\"": 'null', "\"display_order\"": 0}}

                    atributstr.append(sonidosstr)

                atributstr_ = str(atributstr)

                atributstr_ = atributstr_.replace("'", "")

                atributstrl_ = atributstr_.replace('"','\"')

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
                                "specification_attributes": atributstrl_
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
    iva = fields.Float('IVA')

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
                'iva': (amount_untaxed + amount_tax)*.16,
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


