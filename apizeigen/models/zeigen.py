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
    short_description = fields.Text(string='Descripción corta')
    full_description = fields.Text(string='Descripción larga sitio')
    stock_quantity = fields.Float(string='Cantidad en Inventario', related='qty_available')
    disable_buy_button = fields.Boolean('Habilita botón de compra')
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
    special_price = fields.Float(string='Precio especial')
    product_cost = fields.Float(string='Precio al costo del producto.')
    tag_ids = fields.Many2many('tags.zeigen')

    price = fields.Float(
        'Price', compute='_compute_product_price',
        digits='Product Price', inverse='_set_product_price', related='list_price')
    # price_extra: catalog extra value only, sum of variant extra attributes

    marca = fields.Many2one('marca.zeigen', 'Marca')
    subcategoria = fields.Many2one('subcategoria.zeigen','Subcategoría')
    marcasanatom = fields.Many2one('marcasanatom.zeigen', '	Marcas anatómicas')
    materiales = fields.Many2one('materiales.zeigen', 'Materiales')
    ojos = fields.Many2one('ojos.zeigen', 'Ojos')
    tipo = fields.Many2one('tipo.zeigen', '	Tipo')
    nivel = fields.Many2one('nivel.zeigen', 'Nivel')
    pulso = fields.Many2one('pulso.zeigen', 'Pulso')
    respiracion = fields.Many2one('respiracion.zeigen', 'Respiración')
    incluye = fields.Text('Incluye')
    cuerpo = fields.Many2one('cuerpo.zeigen', 'Cuerpo')
    cabezal = fields.Many2one('cabezal.zeigen', 'Cabezal')
    velocidad = fields.Many2one('velocidad.zeigen', 'Velocidad')
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
    reproduc = fields.Many2one('reproduc.zeigen', 'Reproductibilidad')
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
    bombinfu = fields.Many2one('bombinfu.zeigen', 'Bompa de infusión')
    rotor = fields.Many2one('rotor.zeigen', 'Rotor')
    optica = fields.Many2one('optica.zeigen', 'Óptica')
    object = fields.Many2one('object.zeigen', 'Objetivos')
    motor = fields.Many2one('motor.zeigen', 'Motor')
    suda = fields.Many2one('suda.zeigen', 'Suda')
    llora = fields.Many2one('llora.zeigen', 'Llora')
    dimmanti = fields.Many2one('dimmanti.zeigen', 'Dimensiones de mantilla')
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
    rangfoto = fields.Many2one('rangfoto.zeigen', '	Rango fotométrico')
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
    kohler = fields.Many2one('kohler.zeigen', 'Kohler')
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
    observaciones = fields.Text('Observaciones')
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

                raise UserError('error')

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

    @api.onchange('x_familia')
    def _onchange_budget(self):
        self.category_name = str(self.x_familia)

    # @api.multi
    def write(self, vals):
        sitio = []

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

                name=[]
                name = str(self.name)
                if vals.get('name'):
                    name = vals['name']

                short_description = []
                short_description = str(self.short_description)
                if vals.get('short_description'):
                    short_description = vals['short_description']

                full_description = []
                full_description = str(self.full_description)
                if vals.get('full_description'):
                    full_description = vals['full_description']

                stock_quantity=[]
                stock_quantity = self.qty_available
                if vals.get('stock_quantity'):
                    stock_quantity = vals['stock_quantity']


                if vals.get('qty_available'):
                    stock_quantity = vals['qty_available']

                if vals.get('qty_available')==0:
                    stock_quantity = 0

                disable_buy_button = []
                disable_buy_button = str(self.disable_buy_button)
                if vals.get('disable_buy_button'):
                    disable_buy_button = vals['disable_buy_button']

                price = []
                price = str(self.price)
                if vals.get('price'):
                    price = vals['price']

                old_price= []
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
                else:
                    category_name = ''

                sitio=[]
                sitio = str(self.sitio)
                if vals.get('sitio'):
                    sitio = vals['sitio']

                sku = []
                sku = str(self.sku)
                if vals.get('sku'):
                    sku = vals['sku']

                product_cost = []
                product_cost = str(self.product_cost)
                if vals.get('product_cost'):
                    product_cost = vals['product_cost']

                tags = []
                if self.tag_ids != False:
                    for tag_ in self.tag_ids:
                        tags.append(str(tag_.name))


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

                    if marca.nombre == False:
                        marca.nombre = ''

                    if marca.show_on_product_page:
                        marca_show = "true"
                    else:
                        marca_show = "false"

                    marcastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": marca_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 2,
                            "\"name\"": "\"" + str(marca.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(marcastr)

                if vals.get('marca') == False:

                    marca.nombre = ''

                    if marca.show_on_product_page:
                        marca_show = "true"
                    else:
                        marca_show = "false"

                    marcastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": marca_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 2,
                            "\"name\"": "\"" + str(marca.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(marcastr)

                subcategoria = self.subcategoria
                if vals.get('subcategoria'):
                    if vals.get('subcategoria'):
                        id_subcategoria = self.env['subcategoria.zeigen'].search([('id', '=', vals['subcategoria'])])
                    subcategoria = id_subcategoria[0]

                    subcategoria_show = ''

                    if subcategoria.nombre == False:
                        subcategoria.nombre = ''

                    if subcategoria.show_on_product_page:
                        subcategoria_show = "true"
                    else:
                        subcategoria_show = "false"

                    subcategoriastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false',
                                       "\"show_on_product_page\"": subcategoria_show, "\"display_order\"": 1,
                                       "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 3,
                            "\"name\"": "\"" + str(subcategoria.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(subcategoriastr)

                if vals.get('subcategoria') == False:

                    subcategoria.nombre = ''

                    if subcategoria.show_on_product_page:
                        subcategoria_show = "true"
                    else:
                        subcategoria_show = "false"

                    subcategoriastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false',
                                       "\"show_on_product_page\"": subcategoria_show, "\"display_order\"": 1,
                                       "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 3,
                            "\"name\"": "\"" + str(subcategoria.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(subcategoriastr)

                marcasanatom = self.marcasanatom
                if vals.get('marcasanatom'):
                    id_marcasanatom = self.env['marcasanatom.zeigen'].search([('id', '=', vals['marcasanatom'])])
                    marcasanatom = id_marcasanatom[0]

                    marcasanatom_show = ''

                    if marcasanatom.nombre == False:
                        marcasanatom.nombre = ''

                    if marcasanatom.show_on_product_page:
                        marcasanatom_show = "true"
                    else:
                        marcasanatom_show = "false"

                    marcasanatomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false',
                                       "\"show_on_product_page\"": marcasanatom_show, "\"display_order\"": 1,
                                       "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 4,
                            "\"name\"": "\"" + str(marcasanatom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(marcasanatomstr)

                if vals.get('marcasanatom') == False:

                    marcasanatom.nombre = ''

                    if marcasanatom.show_on_product_page:
                        marcasanatom_show = "true"
                    else:
                        marcasanatom_show = "false"

                    marcasanatomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                       "\"allow_filtering\"": 'false',
                                       "\"show_on_product_page\"": marcasanatom_show, "\"display_order\"": 1,
                                       "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 4,
                            "\"name\"": "\"" + str(marcasanatom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(marcasanatomstr)

                materiales = self.materiales
                if vals.get('materiales'):
                    id_materiales = self.env['materiales.zeigen'].search([('id', '=', vals['materiales'])])
                    materiales = id_materiales[0]

                    materiales_show = ''

                    if materiales.nombre == False:
                        materiales.nombre = ''

                    if materiales.show_on_product_page:
                        materiales_show = "true"
                    else:
                        materiales_show = "false"

                    materialesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": materiales_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 5,
                            "\"name\"": "\"" + str(materiales.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(materialesstr)

                if vals.get('materiales') == False:

                    materiales.nombre = ''

                    if materiales.show_on_product_page:
                        materiales_show = "true"
                    else:
                        materiales_show = "false"

                    materialesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": materiales_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 5,
                            "\"name\"": "\"" + str(materiales.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(materialesstr)

                ojos = self.ojos
                if vals.get('ojos'):
                    id_ojos = self.env['ojos.zeigen'].search([('id', '=', vals['ojos'])])
                    ojos = id_ojos[0]

                    ojos_show = ''

                    if ojos.nombre == False:
                        ojos.nombre = ''

                    if ojos.show_on_product_page:
                        ojos_show = "true"
                    else:
                        ojos_show = "false"

                    ojosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": ojos_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 6,
                            "\"name\"": "\"" + str(ojos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ojosstr)

                if vals.get('ojos') == False:

                    ojos.nombre = ''

                    if ojos.show_on_product_page:
                        ojos_show = "true"
                    else:
                        ojos_show = "false"

                    ojosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": ojos_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 6,
                            "\"name\"": "\"" + str(ojos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ojosstr)

                tipo = self.tipo
                if vals.get('tipo'):
                    id_tipo = self.env['tipo.zeigen'].search([('id', '=', vals['tipo'])])
                    tipo = id_tipo[0]

                    tipo_show = ''

                    if tipo.nombre == False:
                        tipo.nombre = ''

                    if tipo.show_on_product_page:
                        tipo_show = "true"
                    else:
                        tipo_show = "false"

                    tipostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": tipo_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 7,
                            "\"name\"": "\"" + str(tipo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tipostr)

                if vals.get('tipo') == False:

                    tipo_show = ''

                    if tipo.show_on_product_page:
                        tipo_show = "true"
                    else:
                        tipo_show = "false"

                    tipostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": tipo_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 7,
                            "\"name\"": "\"" + str(tipo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tipostr)

                nivel = self.nivel
                if vals.get('nivel'):
                    id_nivel = self.env['nivel.zeigen'].search([('id', '=', vals['nivel'])])
                    nivel = id_nivel[0]

                    nivel_show = ''

                    if nivel.nombre == False:
                        nivel.nombre = ''

                    if nivel.show_on_product_page:
                        nivel_show = "true"
                    else:
                        nivel_show = "false"

                    nivelstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": nivel_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 8,
                            "\"name\"": "\"" + str(nivel.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(nivelstr)

                if vals.get('nivel') == False:

                    nivel_show = ''

                    if nivel.show_on_product_page:
                        nivel_show = "true"
                    else:
                        nivel_show = "false"

                    nivelstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": nivel_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 8,
                            "\"name\"": "\"" + str(nivel.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(nivelstr)

                pulso = self.pulso
                if vals.get('pulso'):
                    id_pulso = self.env['pulso.zeigen'].search([('id', '=', vals['pulso'])])
                    pulso = id_pulso[0]

                    pulso_show = ''

                    if pulso.nombre == False:
                        pulso.nombre = ''

                    if pulso.show_on_product_page:
                        pulso_show = "true"
                    else:
                        pulso_show = "false"

                    pulsostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": pulso_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 10,
                            "\"name\"": "\"" + str(pulso.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pulsostr)

                if vals.get('pulso') == False:

                    pulso_show = ''

                    if pulso.show_on_product_page:
                        pulso_show = "true"
                    else:
                        pulso_show = "false"

                    pulsostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": pulso_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 10,
                            "\"name\"": "\"" + str(pulso.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pulsostr)

                respiracion = self.respiracion
                if vals.get('respiracion'):
                    id_respiracion = self.env['respiracion.zeigen'].search([('id', '=', vals['respiracion'])])
                    respiracion = id_respiracion[0]

                    respiracion_show = ''

                    if respiracion.nombre == False:
                        respiracion.nombre = ''

                    if respiracion.show_on_product_page:
                        respiracion_show = "true"
                    else:
                        respiracion_show = "false"

                    respiracionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": respiracion_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 11,
                            "\"name\"": "\"" + str(respiracion.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(respiracionstr)

                if vals.get('respiracion') == False:

                    respiracion_show = ''

                    if respiracion.show_on_product_page:
                        respiracion_show = "true"
                    else:
                        respiracion_show = "false"

                    respiracionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": respiracion_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 11,
                            "\"name\"": "\"" + str(respiracion.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(respiracionstr)

                incluye = self.incluye
                if vals.get('incluye'):

                    incluye_show = ''

                    if incluye == False:
                        incluye = ''


                    incluyestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Custom Text\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 12,
                            "\"name\"": "\"" + str(incluye) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(incluyestr)

                if vals.get('incluye') == False:


                    incluyestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Custom text\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 12,
                            "\"name\"": "\"" + str(incluye) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(incluyestr)

                cabezal = self.cabezal
                if vals.get('cabezal'):
                    id_cabezal = self.env['cabezal.zeigen'].search([('id', '=', vals['cabezal'])])
                    cabezal = id_cabezal[0]

                    cabezal_show = ''

                    if cabezal.nombre == False:
                        cabezal.nombre = ''

                    if cabezal.show_on_product_page:
                        cabezal_show = "true"
                    else:
                        cabezal_show = "false"

                    cabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": cabezal_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 14,
                            "\"name\"": "\"" + str(cabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cabezalstr)

                if vals.get('cabezal') == False:

                    cabezal_show = ''

                    if cabezal.show_on_product_page:
                        cabezal_show = "true"
                    else:
                        cabezal_show = "false"

                    cabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": cabezal_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 14,
                            "\"name\"": "\"" + str(cabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cabezalstr)

                velocidad = self.velocidad
                if vals.get('velocidad'):
                    id_velocidad = self.env['velocidad.zeigen'].search([('id', '=', vals['velocidad'])])
                    velocidad = id_velocidad[0]

                    velocidad_show = ''

                    if velocidad.nombre == False:
                        velocidad.nombre = ''

                    if velocidad.show_on_product_page:
                        velocidad_show = "true"
                    else:
                        velocidad_show = "false"

                    velocidadstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": velocidad_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 15,
                            "\"name\"": "\"" + str(velocidad.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(velocidadstr)

                if vals.get('velocidad') == False:

                    velocidad_show = ''

                    if velocidad.show_on_product_page:
                        velocidad_show = "true"
                    else:
                        velocidad_show = "false"

                    velocidadstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": velocidad_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 15,
                            "\"name\"": "\"" + str(velocidad.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(velocidadstr)

                desfibrilacio = self.desfibrilacio
                if vals.get('desfibrilacio'):
                    id_desfibrilacio = self.env['desfibrilacio.zeigen'].search([('id', '=', vals['desfibrilacio'])])
                    desfibrilacio = id_desfibrilacio[0]

                    desfibrilacio_show = ''

                    if desfibrilacio.nombre == False:
                        desfibrilacio.nombre = ''

                    if desfibrilacio.show_on_product_page:
                        desfibrilacio_show = "true"
                    else:
                        desfibrilacio_show = "false"

                    desfibrilaciostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false',
                                        "\"show_on_product_page\"": desfibrilacio_show, "\"display_order\"": 1,
                                        "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 16,
                            "\"name\"": "\"" + str(desfibrilacio.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(desfibrilaciostr)

                if vals.get('desfibrilacio') == False:

                    desfibrilacio_show = ''

                    if desfibrilacio.show_on_product_page:
                        desfibrilacio_show = "true"
                    else:
                        desfibrilacio_show = "false"

                    desfibrilaciostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false',
                                        "\"show_on_product_page\"": desfibrilacio_show, "\"display_order\"": 1,
                                        "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 16,
                            "\"name\"": "\"" + str(desfibrilacio.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(desfibrilaciostr)

                pecho = self.pecho
                if vals.get('pecho'):
                    id_pecho = self.env['pecho.zeigen'].search([('id', '=', vals['pecho'])])
                    pecho = id_pecho[0]

                    pecho_show = ''

                    if pecho.nombre == False:
                        pecho.nombre = ''

                    if pecho.show_on_product_page:
                        pecho_show = "true"
                    else:
                        pecho_show = "false"

                    pechostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": pecho_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 17,
                            "\"name\"": "\"" + str(pecho.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pechostr)

                if vals.get('pecho') == False:

                    pecho_show = ''

                    if pecho.show_on_product_page:
                        pecho_show = "true"
                    else:
                        pecho_show = "false"

                    pechostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": pecho_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 17,
                            "\"name\"": "\"" + str(pecho.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pechostr)

                rtemp = self.rtemp
                if vals.get('rtemp'):
                    id_rtemp = self.env['rtemp.zeigen'].search([('id', '=', vals['rtemp'])])
                    rtemp = id_rtemp[0]

                    rtemp_show = ''

                    if rtemp.nombre == False:
                        rtemp.nombre = ''

                    if rtemp.show_on_product_page:
                        rtemp_show = "true"
                    else:
                        rtemp_show = "false"

                    rtempstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rtemp_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 18,
                            "\"name\"": "\"" + str(rtemp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rtempstr)

                if vals.get('rtemp') == False:

                    rtemp.nombre = ''

                    if rtemp.show_on_product_page:
                        rtemp_show = "true"
                    else:
                        rtemp_show = "false"

                    rtempstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rtemp_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 18,
                            "\"name\"": "\"" + str(rtemp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rtempstr)

                tipcabezal = self.tipcabezal
                if vals.get('tipcabezal'):
                    id_tipcabezal = self.env['tipcabezal.zeigen'].search([('id', '=', vals['tipcabezal'])])
                    tipcabezal = id_tipcabezal[0]

                    tipcabezal_show = ''

                    if tipcabezal.nombre == False:
                        tipcabezal.nombre = ''

                    if tipcabezal.show_on_product_page:
                        tipcabezal_show = "true"
                    else:
                        tipcabezal_show = "false"

                    tipcabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": tipcabezal_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 19,
                            "\"name\"": "\"" + str(tipcabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tipcabezalstr)

                if vals.get('tipcabezal') == False:

                    tipcabezal.nombre = ''

                    if tipcabezal.show_on_product_page:
                        tipcabezal_show = "true"
                    else:
                        tipcabezal_show = "false"

                    tipcabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": tipcabezal_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 19,
                            "\"name\"": "\"" + str(tipcabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tipcabezalstr)

                inccabezal = self.inccabezal
                if vals.get('inccabezal'):
                    id_inccabezal = self.env['inccabezal.zeigen'].search([('id', '=', vals['inccabezal'])])
                    inccabezal = id_inccabezal[0]

                    inccabezal_show = ''

                    if inccabezal.nombre == False:
                        inccabezal.nombre = ''

                    if inccabezal.show_on_product_page:
                        inccabezal_show = "true"
                    else:
                        inccabezal_show = "false"

                    inccabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": inccabezal_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 20,
                            "\"name\"": "\"" + str(inccabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(inccabezalstr)

                if vals.get('inccabezal') == False:

                    inccabezal.nombre = ''

                    if inccabezal.show_on_product_page:
                        inccabezal_show = "true"
                    else:
                        inccabezal_show = "false"

                    inccabezalstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": inccabezal_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 20,
                            "\"name\"": "\"" + str(inccabezal.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(inccabezalstr)

                plato = self.plato
                if vals.get('plato'):
                    id_plato = self.env['plato.zeigen'].search([('id', '=', vals['plato'])])
                    plato = id_plato[0]

                    plato_show = ''

                    if plato.nombre == False:
                        plato.nombre = ''

                    if plato.show_on_product_page:
                        plato_show = "true"
                    else:
                        plato_show = "false"

                    platostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": plato_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 21,
                            "\"name\"": "\"" + str(plato.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(platostr)

                if vals.get('plato') == False:

                    plato.nombre = ''

                    if plato.show_on_product_page:
                        plato_show = "true"
                    else:
                        plato_show = "false"

                    platostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": plato_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 21,
                            "\"name\"": "\"" + str(plato.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(platostr)

                auscult = self.auscult
                if vals.get('auscult'):
                    id_auscult = self.env['auscult.zeigen'].search([('id', '=', vals['auscult'])])
                    auscult = id_auscult[0]

                    auscult_show = ''

                    if auscult.nombre == False:
                        auscult.nombre = ''

                    if auscult.show_on_product_page:
                        auscult_show = "true"
                    else:
                        auscult_show = "false"

                    auscultstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": auscult_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 22,
                            "\"name\"": "\"" + str(auscult.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(auscultstr)

                if vals.get('auscult') == False:

                    auscult.nombre = ''

                    if auscult.show_on_product_page:
                        auscult_show = "true"
                    else:
                        auscult_show = "false"

                    auscultstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": auscult_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 22,
                            "\"name\"": "\"" + str(auscult.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(auscultstr)

                rcp = self.rcp
                if vals.get('rcp'):
                    id_rcp = self.env['rcp.zeigen'].search([('id', '=', vals['rcp'])])
                    rcp = id_rcp[0]

                    rcp_show = ''

                    if rcp.nombre == False:
                        rcp.nombre = ''

                    if rcp.show_on_product_page:
                        rcp_show = "true"
                    else:
                        rcp_show = "false"

                    rcpstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": rcp_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 23,
                            "\"name\"": "\"" + str(rcp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rcpstr)

                if vals.get('rcp') == False:

                    rcp.nombre = ''

                    if rcp.show_on_product_page:
                        rcp_show = "true"
                    else:
                        rcp_show = "false"

                    rcpstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": rcp_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 23,
                            "\"name\"": "\"" + str(rcp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rcpstr)

                tiempo = self.tiempo
                if vals.get('tiempo'):
                    id_tiempo = self.env['tiempo.zeigen'].search([('id', '=', vals['tiempo'])])
                    tiempo = id_tiempo[0]

                    tiempo_show = ''

                    if tiempo.nombre == False:
                        tiempo.nombre = ''

                    if tiempo.show_on_product_page:
                        tiempo_show = "true"
                    else:
                        tiempo_show = "false"

                    tiempostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": tiempo_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 24,
                            "\"name\"": "\"" + str(tiempo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tiempostr)

                if vals.get('tiempo') == False:

                    tiempo.nombre = ''

                    if tiempo.show_on_product_page:
                        tiempo_show = "true"
                    else:
                        tiempo_show = "false"

                    tiempostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": tiempo_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 24,
                            "\"name\"": "\"" + str(tiempo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tiempostr)

                cabgir = self.cabgir
                if vals.get('cabgir'):
                    id_cabgir = self.env['cabgir.zeigen'].search([('id', '=', vals['cabgir'])])
                    cabgir = id_cabgir[0]

                    cabgir_show = ''

                    if cabgir.nombre == False:
                        cabgir.nombre = ''

                    if cabgir.show_on_product_page:
                        cabgir_show = "true"
                    else:
                        cabgir_show = "false"

                    cabgirstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": cabgir_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 25,
                            "\"name\"": "\"" + str(cabgir.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cabgirstr)

                if vals.get('cabgir') == False:

                    cabgir.nombre = ''

                    if cabgir.show_on_product_page:
                        cabgir_show = "true"
                    else:
                        cabgir_show = "false"

                    cabgirstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": cabgir_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 25,
                            "\"name\"": "\"" + str(cabgir.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cabgirstr)

                ajusdiot = self.ajusdiot
                if vals.get('ajusdiot'):
                    id_ajusdiot = self.env['ajusdiot.zeigen'].search([('id', '=', vals['ajusdiot'])])
                    ajusdiot = id_ajusdiot[0]

                    ajusdiot_show = ''

                    if ajusdiot.nombre == False:
                        ajusdiot.nombre = ''

                    if ajusdiot.show_on_product_page:
                        ajusdiot_show = "true"
                    else:
                        ajusdiot_show = "false"

                    ajusdiotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": ajusdiot_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 26,
                            "\"name\"": "\"" + str(ajusdiot.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ajusdiotstr)

                if vals.get('ajusdiot') == False:

                    ajusdiot.nombre = ''

                    if ajusdiot.show_on_product_page:
                        ajusdiot_show = "true"
                    else:
                        ajusdiot_show = "false"

                    ajusdiotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": ajusdiot_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 26,
                            "\"name\"": "\"" + str(ajusdiot.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ajusdiotstr)

                rango = self.rango
                if vals.get('rango'):
                    id_rango = self.env['rango.zeigen'].search([('id', '=', vals['rango'])])
                    rango = id_rango[0]

                    rango_show = ''

                    if rango.nombre == False:
                        rango.nombre = ''

                    if rango.show_on_product_page:
                        rango_show = "true"
                    else:
                        rango_show = "false"

                    rangostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rango_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 27,
                            "\"name\"": "\"" + str(rango.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rangostr)

                if vals.get('rango') == False:

                    rango.nombre = ''

                    if rango.show_on_product_page:
                        rango_show = "true"
                    else:
                        rango_show = "false"

                    rangostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rango_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 27,
                            "\"name\"": "\"" + str(rango.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rangostr)

                pressang = self.pressang
                if vals.get('pressang'):
                    id_pressang = self.env['pressang.zeigen'].search([('id', '=', vals['pressang'])])
                    pressang = id_pressang[0]

                    pressang_show = ''

                    if pressang.nombre == False:
                        pressang.nombre = ''

                    if pressang.show_on_product_page:
                        pressang_show = "true"
                    else:
                        pressang_show = "false"

                    pressangstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": pressang_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 28,
                            "\"name\"": "\"" + str(pressang.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pressangstr)

                if vals.get('pressang') == False:

                    pressang.nombre = ''

                    if pressang.show_on_product_page:
                        pressang_show = "true"
                    else:
                        pressang_show = "false"

                    pressangstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": pressang_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 28,
                            "\"name\"": "\"" + str(pressang.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pressangstr)

                reflejos = self.reflejos
                if vals.get('reflejos'):
                    id_reflejos = self.env['reflejos.zeigen'].search([('id', '=', vals['reflejos'])])
                    reflejos = id_reflejos[0]

                    reflejos_show = ''

                    if reflejos.nombre == False:
                        reflejos.nombre = ''

                    if reflejos.show_on_product_page:
                        reflejos_show = "true"
                    else:
                        reflejos_show = "false"

                    reflejosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": reflejos_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 29,
                            "\"name\"": "\"" + str(reflejos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reflejosstr)

                if vals.get('reflejos') == False:

                    reflejos.nombre = ''

                    if reflejos.show_on_product_page:
                        reflejos_show = "true"
                    else:
                        reflejos_show = "false"

                    reflejosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": reflejos_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 29,
                            "\"name\"": "\"" + str(reflejos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reflejosstr)

                reproduc = self.reproduc
                if vals.get('reproduc'):
                    id_reproduc = self.env['reproduc.zeigen'].search([('id', '=', vals['reproduc'])])
                    reproduc = id_reproduc[0]

                    reproduc_show = ''

                    if reproduc.nombre == False:
                        reproduc.nombre = ''

                    if reproduc.show_on_product_page:
                        reproduc_show = "true"
                    else:
                        reproduc_show = "false"

                    reproducstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": reproduc_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 30,
                            "\"name\"": "\"" + str(reproduc.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reproducstr)

                if vals.get('reproduc') == False:

                    reproduc.nombre = ''

                    if reproduc.show_on_product_page:
                        reproduc_show = "true"
                    else:
                        reproduc_show = "false"

                    reproducstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": reproduc_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 30,
                            "\"name\"": "\"" + str(reproduc.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reproducstr)

                ajusinterpu = self.ajusinterpu
                if vals.get('ajusinterpu'):
                    id_ajusinterpu = self.env['ajusinterpu.zeigen'].search([('id', '=', vals['ajusinterpu'])])
                    ajusinterpu = id_ajusinterpu[0]

                    ajusinterpu_show = ''

                    if ajusinterpu.nombre == False:
                        ajusinterpu.nombre = ''

                    if ajusinterpu.show_on_product_page:
                        ajusinterpu_show = "true"
                    else:
                        ajusinterpu_show = "false"

                    ajusinterpustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": ajusinterpu_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 31,
                            "\"name\"": "\"" + str(ajusinterpu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ajusinterpustr)

                if vals.get('ajusinterpu') == False:

                    ajusinterpu.nombre = ''

                    if ajusinterpu.show_on_product_page:
                        ajusinterpu_show = "true"
                    else:
                        ajusinterpu_show = "false"

                    ajusinterpustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": ajusinterpu_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 31,
                            "\"name\"": "\"" + str(ajusinterpu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ajusinterpustr)

                oculares = self.oculares
                if vals.get('oculares'):
                    id_oculares = self.env['oculares.zeigen'].search([('id', '=', vals['oculares'])])
                    oculares = id_oculares[0]

                    oculares_show = ''

                    if oculares.nombre == False:
                        oculares.nombre = ''

                    if oculares.show_on_product_page:
                        oculares_show = "true"
                    else:
                        oculares_show = "false"

                    ocularesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": oculares_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 32,
                            "\"name\"": "\"" + str(oculares.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ocularesstr)

                if vals.get('oculares') == False:

                    oculares.nombre = ''

                    if oculares.show_on_product_page:
                        oculares_show = "true"
                    else:
                        oculares_show = "false"

                    ocularesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": oculares_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 32,
                            "\"name\"": "\"" + str(oculares.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ocularesstr)

                errlin = self.errlin
                if vals.get('errlin'):
                    id_errlin = self.env['errlin.zeigen'].search([('id', '=', vals['errlin'])])
                    errlin = id_errlin[0]

                    errlin_show = ''

                    if errlin.nombre == False:
                        errlin.nombre = ''

                    if errlin.show_on_product_page:
                        errlin_show = "true"
                    else:
                        errlin_show = "false"

                    errlinstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": errlin_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 33,
                            "\"name\"": "\"" + str(errlin.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(errlinstr)

                if vals.get('errlin') == False:

                    errlin.nombre = ''

                    if errlin.show_on_product_page:
                        errlin_show = "true"
                    else:
                        errlin_show = "false"

                    errlinstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": errlin_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 33,
                            "\"name\"": "\"" + str(errlin.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(errlinstr)

                sindrom = self.sindrom
                if vals.get('sindrom'):
                    id_sindrom = self.env['sindrom.zeigen'].search([('id', '=', vals['sindrom'])])
                    sindrom = id_sindrom[0]

                    sindrom_show = ''

                    if sindrom.nombre == False:
                        sindrom.nombre = ''

                    if sindrom.show_on_product_page:
                        sindrom_show = "true"
                    else:
                        sindrom_show = "false"

                    sindromstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sindrom_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 34,
                            "\"name\"": "\"" + str(sindrom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sindromstr)

                if vals.get('sindrom') == False:

                    sindrom.nombre = ''

                    if sindrom.show_on_product_page:
                        sindrom_show = "true"
                    else:
                        sindrom_show = "false"

                    sindromstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sindrom_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 34,
                            "\"name\"": "\"" + str(sindrom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sindromstr)

                fichpacien = self.fichpacien
                if vals.get('fichpacien'):
                    id_fichpacien = self.env['fichpacien.zeigen'].search([('id', '=', vals['fichpacien'])])
                    fichpacien = id_fichpacien[0]

                    fichpacien_show = ''

                    if fichpacien.nombre == False:
                        fichpacien.nombre = ''

                    if fichpacien.show_on_product_page:
                        fichpacien_show = "true"
                    else:
                        fichpacien_show = "false"

                    fichpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": fichpacien_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 35,
                            "\"name\"": "\"" + str(fichpacien.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fichpacienstr)

                if vals.get('fichpacien') == False:

                    fichpacien.nombre = ''

                    if fichpacien.show_on_product_page:
                        fichpacien_show = "true"
                    else:
                        fichpacien_show = "false"

                    fichpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": fichpacien_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 35,
                            "\"name\"": "\"" + str(fichpacien.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fichpacienstr)

                pothot = self.pothot
                if vals.get('pothot'):
                    id_pothot = self.env['pothot.zeigen'].search([('id', '=', vals['pothot'])])
                    pothot = id_pothot[0]

                    pothot_show = ''

                    if pothot.nombre == False:
                        pothot.nombre = ''

                    if pothot.show_on_product_page:
                        pothot_show = "true"
                    else:
                        pothot_show = "false"

                    pothotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": pothot_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 36,
                            "\"name\"": "\"" + str(pothot.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pothotstr)

                if vals.get('pothot') == False:

                    pothot.nombre = ''

                    if pothot.show_on_product_page:
                        pothot_show = "true"
                    else:
                        pothot_show = "false"

                    pothotstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": pothot_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 36,
                            "\"name\"": "\"" + str(pothot.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(pothotstr)

                ocpris = self.ocpris
                if vals.get('ocpris'):
                    id_ocpris = self.env['ocpris.zeigen'].search([('id', '=', vals['ocpris'])])
                    ocpris = id_ocpris[0]

                    ocpris_show = ''

                    if ocpris.nombre == False:
                        ocpris.nombre = ''

                    if ocpris.show_on_product_page:
                        ocpris_show = "true"
                    else:
                        ocpris_show = "false"

                    ocprisstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": ocpris_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 37,
                            "\"name\"": "\"" + str(ocpris.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ocprisstr)

                if vals.get('ocpris') == False:

                    ocpris.nombre = ''

                    if ocpris.show_on_product_page:
                        ocpris_show = "true"
                    else:
                        ocpris_show = "false"

                    ocprisstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": ocpris_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 37,
                            "\"name\"": "\"" + str(ocpris.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ocprisstr)

                revol = self.revol
                if vals.get('revol'):
                    id_revol = self.env['revol.zeigen'].search([('id', '=', vals['revol'])])
                    revol = id_revol[0]

                    revol_show = ''

                    if revol.nombre == False:
                        revol.nombre = ''

                    if revol.show_on_product_page:
                        revol_show = "true"
                    else:
                        revol_show = "false"

                    revolstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": revol_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 38,
                            "\"name\"": "\"" + str(revol.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(revolstr)

                if vals.get('revol') == False:

                    revol.nombre = ''

                    if revol.show_on_product_page:
                        revol_show = "true"
                    else:
                        revol_show = "false"

                    revolstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": revol_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 38,
                            "\"name\"": "\"" + str(revol.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(revolstr)

                dimtina = self.dimtina
                if vals.get('dimtina'):
                    id_dimtina = self.env['dimtina.zeigen'].search([('id', '=', vals['dimtina'])])
                    dimtina = id_dimtina[0]

                    dimtina_show = ''

                    if dimtina.nombre == False:
                        dimtina.nombre = ''

                    if dimtina.show_on_product_page:
                        dimtina_show = "true"
                    else:
                        dimtina_show = "false"

                    dimtinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": dimtina_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 39,
                            "\"name\"": "\"" + str(dimtina.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(dimtinastr)

                if vals.get('dimtina') == False:

                    dimtina.nombre = ''

                    if dimtina.show_on_product_page:
                        dimtina_show = "true"
                    else:
                        dimtina_show = "false"

                    dimtinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": dimtina_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 39,
                            "\"name\"": "\"" + str(dimtina.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(dimtinastr)

                cian = self.cian
                if vals.get('cian'):
                    id_cian = self.env['cian.zeigen'].search([('id', '=', vals['cian'])])
                    cian = id_cian[0]

                    cian_show = ''

                    if cian.nombre == False:
                        cian.nombre = ''

                    if cian.show_on_product_page:
                        cian_show = "true"
                    else:
                        cian_show = "false"

                    cianstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": cian_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 40,
                            "\"name\"": "\"" + str(cian.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cianstr)

                if vals.get('cian') == False:

                    cian.nombre = ''

                    if cian.show_on_product_page:
                        cian_show = "true"
                    else:
                        cian_show = "false"

                    cianstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": cian_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 40,
                            "\"name\"": "\"" + str(cian.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cianstr)

                bombinfu = self.bombinfu
                if vals.get('bombinfu'):
                    id_bombinfu = self.env['bombinfu.zeigen'].search([('id', '=', vals['bombinfu'])])
                    bombinfu = id_bombinfu[0]

                    bombinfu_show = ''

                    if bombinfu.nombre == False:
                        bombinfu.nombre = ''

                    if bombinfu.show_on_product_page:
                        bombinfu_show = "true"
                    else:
                        bombinfu_show = "false"

                    bombinfustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": bombinfu_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 41,
                            "\"name\"": "\"" + str(bombinfu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(bombinfustr)

                if vals.get('bombinfu') == False:

                    bombinfu.nombre = ''

                    if bombinfu.show_on_product_page:
                        bombinfu_show = "true"
                    else:
                        bombinfu_show = "false"

                    bombinfustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": bombinfu_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 41,
                            "\"name\"": "\"" + str(bombinfu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(bombinfustr)

                rotor = self.rotor
                if vals.get('rotor'):
                    id_rotor = self.env['rotor.zeigen'].search([('id', '=', vals['rotor'])])
                    rotor = id_rotor[0]

                    rotor_show = ''

                    if rotor.nombre == False:
                        rotor.nombre = ''

                    if rotor.show_on_product_page:
                        rotor_show = "true"
                    else:
                        rotor_show = "false"

                    rotorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rotor_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 42,
                            "\"name\"": "\"" + str(rotor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rotorstr)

                if vals.get('rotor') == False:

                    rotor.nombre = ''

                    if rotor.show_on_product_page:
                        rotor_show = "true"
                    else:
                        rotor_show = "false"

                    rotorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": rotor_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 42,
                            "\"name\"": "\"" + str(rotor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rotorstr)

                optica = self.optica
                if vals.get('optica'):
                    id_optica = self.env['optica.zeigen'].search([('id', '=', vals['optica'])])
                    optica = id_optica[0]

                    optica_show = ''

                    if optica.nombre == False:
                        optica.nombre = ''

                    if optica.show_on_product_page:
                        optica_show = "true"
                    else:
                        optica_show = "false"

                    opticastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": optica_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 43,
                            "\"name\"": "\"" + str(optica.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opticastr)

                if vals.get('optica') == False:

                    optica.nombre = ''

                    if optica.show_on_product_page:
                        optica_show = "true"
                    else:
                        optica_show = "false"

                    opticastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": optica_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 43,
                            "\"name\"": "\"" + str(optica.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opticastr)

                object = self.object
                if vals.get('object'):
                    id_object = self.env['object.zeigen'].search([('id', '=', vals['object'])])
                    object = id_object[0]

                    object_show = ''

                    if object.nombre == False:
                        object.nombre = ''

                    if object.show_on_product_page:
                        object_show = "true"
                    else:
                        object_show = "false"

                    objectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": object_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 44,
                            "\"name\"": "\"" + str(object.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(objectstr)

                if vals.get('object') == False:

                    object.nombre = ''

                    if object.show_on_product_page:
                        object_show = "true"
                    else:
                        object_show = "false"

                    objectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": object_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 44,
                            "\"name\"": "\"" + str(object.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(objectstr)

                motor = self.motor
                if vals.get('motor'):
                    id_motor = self.env['motor.zeigen'].search([('id', '=', vals['motor'])])
                    motor = id_motor[0]

                    motor_show = ''

                    if motor.nombre == False:
                        motor.nombre = ''

                    if motor.show_on_product_page:
                        motor_show = "true"
                    else:
                        motor_show = "false"

                    motorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": motor_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 45,
                            "\"name\"": "\"" + str(motor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(motorstr)

                if vals.get('motor') == False:

                    motor.nombre = ''

                    if motor.show_on_product_page:
                        motor_show = "true"
                    else:
                        motor_show = "false"

                    motorstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": motor_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 45,
                            "\"name\"": "\"" + str(motor.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(motorstr)

                suda = self.suda
                if vals.get('suda'):
                    id_suda = self.env['suda.zeigen'].search([('id', '=', vals['suda'])])
                    suda = id_suda[0]

                    suda_show = ''

                    if suda.nombre == False:
                        suda.nombre = ''

                    if suda.show_on_product_page:
                        suda_show = "true"
                    else:
                        suda_show = "false"

                    sudastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": suda_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 46,
                            "\"name\"": "\"" + str(suda.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sudastr)

                if vals.get('suda') == False:

                    suda.nombre = ''

                    if suda.show_on_product_page:
                        suda_show = "true"
                    else:
                        suda_show = "false"

                    sudastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": suda_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 46,
                            "\"name\"": "\"" + str(suda.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sudastr)

                llora = self.llora
                if vals.get('llora'):
                    id_llora = self.env['llora.zeigen'].search([('id', '=', vals['llora'])])
                    llora = id_llora[0]

                    llora_show = ''

                    if llora.nombre == False:
                        llora.nombre = ''

                    if llora.show_on_product_page:
                        llora_show = "true"
                    else:
                        llora_show = "false"

                    llorastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": llora_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 47,
                            "\"name\"": "\"" + str(llora.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(llorastr)

                if vals.get('llora') == False:

                    llora.nombre = ''

                    if llora.show_on_product_page:
                        llora_show = "true"
                    else:
                        llora_show = "false"

                    llorastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": llora_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 47,
                            "\"name\"": "\"" + str(llora.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(llorastr)

                dimmanti = self.dimmanti
                if vals.get('dimmanti'):
                    id_dimmanti = self.env['dimmanti.zeigen'].search([('id', '=', vals['dimmanti'])])
                    dimmanti = id_dimmanti[0]

                    dimmanti_show = ''

                    if dimmanti.nombre == False:
                        dimmanti.nombre = ''

                    if dimmanti.show_on_product_page:
                        dimmanti_show = "true"
                    else:
                        dimmanti_show = "false"

                    dimmantistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": dimmanti_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 48,
                            "\"name\"": "\"" + str(dimmanti.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(dimmantistr)

                if vals.get('dimmanti') == False:

                    dimmanti.nombre = ''

                    if dimmanti.show_on_product_page:
                        dimmanti_show = "true"
                    else:
                        dimmanti_show = "false"

                    dimmantistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": dimmanti_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 48,
                            "\"name\"": "\"" + str(dimmanti.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(dimmantistr)

                aumen = self.aumen
                if vals.get('aumen'):
                    id_aumen = self.env['aumen.zeigen'].search([('id', '=', vals['aumen'])])
                    aumen = id_aumen[0]

                    aumen_show = ''

                    if aumen.nombre == False:
                        aumen.nombre = ''

                    if aumen.show_on_product_page:
                        aumen_show = "true"
                    else:
                        aumen_show = "false"

                    aumenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": aumen_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 49,
                            "\"name\"": "\"" + str(aumen.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(aumenstr)

                if vals.get('aumen') == False:

                    aumen.nombre = ''

                    if aumen.show_on_product_page:
                        aumen_show = "true"
                    else:
                        aumen_show = "false"

                    aumenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": aumen_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 49,
                            "\"name\"": "\"" + str(aumen.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(aumenstr)

                enfo = self.enfo
                if vals.get('enfo'):
                    id_enfo = self.env['enfo.zeigen'].search([('id', '=', vals['enfo'])])
                    enfo = id_enfo[0]

                    enfo_show = ''

                    if enfo.nombre == False:
                        enfo.nombre = ''

                    if enfo.show_on_product_page:
                        enfo_show = "true"
                    else:
                        enfo_show = "false"

                    enfostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": enfo_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 50,
                            "\"name\"": "\"" + str(enfo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(enfostr)

                if vals.get('enfo') == False:

                    enfo.nombre = ''

                    if enfo.show_on_product_page:
                        enfo_show = "true"
                    else:
                        enfo_show = "false"

                    enfostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": enfo_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 50,
                            "\"name\"": "\"" + str(enfo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(enfostr)

                contrem = self.contrem
                if vals.get('contrem'):
                    id_contrem = self.env['contrem.zeigen'].search([('id', '=', vals['contrem'])])
                    contrem = id_contrem[0]

                    contrem_show = ''

                    if contrem.nombre == False:
                        contrem.nombre = ''

                    if contrem.show_on_product_page:
                        contrem_show = "true"
                    else:
                        contrem_show = "false"

                    contremstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": contrem_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 51,
                            "\"name\"": "\"" + str(contrem.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(contremstr)

                if vals.get('contrem') == False:

                    contrem.nombre = ''

                    if contrem.show_on_product_page:
                        contrem_show = "true"
                    else:
                        contrem_show = "false"

                    contremstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": contrem_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 51,
                            "\"name\"": "\"" + str(contrem.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(contremstr)

                table = self.table
                if vals.get('table'):
                    id_table = self.env['table.zeigen'].search([('id', '=', vals['table'])])
                    table = id_table[0]

                    table_show = ''

                    if table.nombre == False:
                        table.nombre = ''

                    if table.show_on_product_page:
                        table_show = "true"
                    else:
                        table_show = "false"

                    tablestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": table_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 52,
                            "\"name\"": "\"" + str(table.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tablestr)

                if vals.get('table') == False:

                    table.nombre = ''

                    if table.show_on_product_page:
                        table_show = "true"
                    else:
                        table_show = "false"

                    tablestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": table_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 52,
                            "\"name\"": "\"" + str(table.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tablestr)

                anchband = self.anchband
                if vals.get('anchband'):
                    id_anchband = self.env['anchband.zeigen'].search([('id', '=', vals['anchband'])])
                    anchband = id_anchband[0]

                    anchband_show = ''

                    if anchband.nombre == False:
                        anchband.nombre = ''

                    if anchband.show_on_product_page:
                        anchband_show = "true"
                    else:
                        anchband_show = "false"

                    anchbandstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": anchband_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 53,
                            "\"name\"": "\"" + str(anchband.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(anchbandstr)

                if vals.get('anchband') == False:

                    anchband.nombre = ''

                    if anchband.show_on_product_page:
                        anchband_show = "true"
                    else:
                        anchband_show = "false"

                    anchbandstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": anchband_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 53,
                            "\"name\"": "\"" + str(anchband.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(anchbandstr)

                platina = self.platina
                if vals.get('platina'):
                    id_platina = self.env['platina.zeigen'].search([('id', '=', vals['platina'])])
                    platina = id_platina[0]

                    platina_show = ''

                    if platina.nombre == False:
                        platina.nombre = ''

                    if platina.show_on_product_page:
                        platina_show = "true"
                    else:
                        platina_show = "false"

                    platinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": platina_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 54,
                            "\"name\"": "\"" + str(platina.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(platinastr)

                if vals.get('platina') == False:

                    platina.nombre = ''

                    if platina.show_on_product_page:
                        platina_show = "true"
                    else:
                        platina_show = "false"

                    platinastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": platina_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 54,
                            "\"name\"": "\"" + str(platina.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(platinastr)

                tamplat = self.tamplat
                if vals.get('tamplat'):
                    id_tamplat = self.env['tamplat.zeigen'].search([('id', '=', vals['tamplat'])])
                    tamplat = id_tamplat[0]

                    tamplat_show = ''

                    if tamplat.nombre == False:
                        tamplat.nombre = ''

                    if tamplat.show_on_product_page:
                        tamplat_show = "true"
                    else:
                        tamplat_show = "false"

                    tamplatstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": tamplat_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 55,
                            "\"name\"": "\"" + str(tamplat.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tamplatstr)

                if vals.get('tamplat') == False:

                    tamplat.nombre = ''

                    if tamplat.show_on_product_page:
                        tamplat_show = "true"
                    else:
                        tamplat_show = "false"

                    tamplatstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": tamplat_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 55,
                            "\"name\"": "\"" + str(tamplat.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(tamplatstr)

                sistopt = self.sistopt
                if vals.get('sistopt'):
                    id_sistopt = self.env['sistopt.zeigen'].search([('id', '=', vals['sistopt'])])
                    sistopt = id_sistopt[0]

                    sistopt_show = ''

                    if sistopt.nombre == False:
                        sistopt.nombre = ''

                    if sistopt.show_on_product_page:
                        sistopt_show = "true"
                    else:
                        sistopt_show = "false"

                    sistoptstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sistopt_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 56,
                            "\"name\"": "\"" + str(sistopt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistoptstr)

                if vals.get('sistopt') == False:

                    sistopt.nombre = ''

                    if sistopt.show_on_product_page:
                        sistopt_show = "true"
                    else:
                        sistopt_show = "false"

                    sistoptstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sistopt_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 56,
                            "\"name\"": "\"" + str(sistopt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistoptstr)

                compu = self.compu
                if vals.get('compu'):
                    id_compu = self.env['compu.zeigen'].search([('id', '=', vals['compu'])])
                    compu = id_compu[0]

                    compu_show = ''

                    if compu.nombre == False:
                        compu.nombre = ''

                    if compu.show_on_product_page:
                        compu_show = "true"
                    else:
                        compu_show = "false"

                    compustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": compu_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 57,
                            "\"name\"": "\"" + str(compu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(compustr)

                if vals.get('compu') == False:

                    compu.nombre = ''

                    if compu.show_on_product_page:
                        compu_show = "true"
                    else:
                        compu_show = "false"

                    compustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": compu_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 57,
                            "\"name\"": "\"" + str(compu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(compustr)

                procsimu = self.procsimu
                if vals.get('procsimu'):
                    id_procsimu = self.env['procsimu.zeigen'].search([('id', '=', vals['procsimu'])])
                    procsimu = id_procsimu[0]

                    procsimu_show = ''

                    if procsimu.nombre == False:
                        procsimu.nombre = ''

                    if procsimu.show_on_product_page:
                        procsimu_show = "true"
                    else:
                        procsimu_show = "false"

                    procsimustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": procsimu_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 58,
                            "\"name\"": "\"" + str(procsimu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(procsimustr)

                if vals.get('procsimu') == False:

                    procsimu.nombre = ''

                    if procsimu.show_on_product_page:
                        procsimu_show = "true"
                    else:
                        procsimu_show = "false"

                    procsimustr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": procsimu_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 58,
                            "\"name\"": "\"" + str(procsimu.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(procsimustr)

                rangfoto = self.rangfoto
                if vals.get('rangfoto'):
                    id_rangfoto = self.env['rangfoto.zeigen'].search([('id', '=', vals['rangfoto'])])
                    rangfoto = id_rangfoto[0]

                    rangfoto_show = ''

                    if rangfoto.nombre == False:
                        rangfoto.nombre = ''

                    if rangfoto.show_on_product_page:
                        rangfoto_show = "true"
                    else:
                        rangfoto_show = "false"

                    rangfotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": rangfoto_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 59,
                            "\"name\"": "\"" + str(rangfoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rangfotostr)

                if vals.get('rangfoto') == False:

                    rangfoto.nombre = ''

                    if rangfoto.show_on_product_page:
                        rangfoto_show = "true"
                    else:
                        rangfoto_show = "false"

                    rangfotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": rangfoto_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 59,
                            "\"name\"": "\"" + str(rangfoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(rangfotostr)

                tope = self.tope
                if vals.get('tope'):
                    id_tope = self.env['tope.zeigen'].search([('id', '=', vals['tope'])])
                    tope = id_tope[0]

                    tope_show = ''

                    if tope.nombre == False:
                        tope.nombre = ''

                    if tope.show_on_product_page:
                        tope_show = "true"
                    else:
                        tope_show = "false"

                    topestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": tope_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 60,
                            "\"name\"": "\"" + str(tope.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(topestr)

                if vals.get('tope') == False:

                    tope.nombre = ''

                    if tope.show_on_product_page:
                        tope_show = "true"
                    else:
                        tope_show = "false"

                    topestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": tope_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 60,
                            "\"name\"": "\"" + str(tope.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(topestr)

                conden = self.conden
                if vals.get('conden'):
                    id_conden = self.env['conden.zeigen'].search([('id', '=', vals['conden'])])
                    conden = id_conden[0]

                    conden_show = ''

                    if conden.nombre == False:
                        conden.nombre = ''

                    if conden.show_on_product_page:
                        conden_show = "true"
                    else:
                        conden_show = "false"

                    condenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": conden_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 61,
                            "\"name\"": "\"" + str(conden.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(condenstr)

                if vals.get('conden') == False:

                    conden.nombre = ''

                    if conden.show_on_product_page:
                        conden_show = "true"
                    else:
                        conden_show = "false"

                    condenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": conden_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 61,
                            "\"name\"": "\"" + str(conden.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(condenstr)

                alcalong = self.alcalong
                if vals.get('alcalong'):
                    id_alcalong = self.env['alcalong.zeigen'].search([('id', '=', vals['alcalong'])])
                    alcalong = id_alcalong[0]

                    alcalong_show = ''

                    if alcalong.nombre == False:
                        alcalong.nombre = ''

                    if alcalong.show_on_product_page:
                        alcalong_show = "true"
                    else:
                        alcalong_show = "false"

                    alcalongstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": alcalong_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 62,
                            "\"name\"": "\"" + str(alcalong.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alcalongstr)

                if vals.get('alcalong') == False:

                    alcalong.nombre = ''

                    if alcalong.show_on_product_page:
                        alcalong_show = "true"
                    else:
                        alcalong_show = "false"

                    alcalongstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": alcalong_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 62,
                            "\"name\"": "\"" + str(alcalong.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alcalongstr)

                conect = self.conect
                if vals.get('conect'):
                    id_conect = self.env['conect.zeigen'].search([('id', '=', vals['conect'])])
                    conect = id_conect[0]

                    conect_show = ''

                    if conect.nombre == False:
                        conect.nombre = ''

                    if conect.show_on_product_page:
                        conect_show = "true"
                    else:
                        conect_show = "false"

                    conectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": conect_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 63,
                            "\"name\"": "\"" + str(conect.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(conectstr)

                if vals.get('conect') == False:

                    conect.nombre = ''

                    if conect.show_on_product_page:
                        conect_show = "true"
                    else:
                        conect_show = "false"

                    conectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": conect_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 63,
                            "\"name\"": "\"" + str(conect.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(conectstr)

                puntion = self.puntion
                if vals.get('puntion'):
                    id_puntion = self.env['puntion.zeigen'].search([('id', '=', vals['puntion'])])
                    puntion = id_puntion[0]

                    puntion_show = ''

                    if puntion.nombre == False:
                        puntion.nombre = ''

                    if puntion.show_on_product_page:
                        puntion_show = "true"
                    else:
                        puntion_show = "false"

                    puntionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": puntion_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 64,
                            "\"name\"": "\"" + str(puntion.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(puntionstr)

                if vals.get('puntion') == False:

                    puntion.nombre = ''

                    if puntion.show_on_product_page:
                        puntion_show = "true"
                    else:
                        puntion_show = "false"

                    puntionstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": puntion_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 64,
                            "\"name\"": "\"" + str(puntion.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(puntionstr)

                alcafoto = self.alcafoto
                if vals.get('alcafoto'):
                    id_alcafoto = self.env['alcafoto.zeigen'].search([('id', '=', vals['alcafoto'])])
                    alcafoto = id_alcafoto[0]

                    alcafoto_show = ''

                    if alcafoto.nombre == False:
                        alcafoto.nombre = ''

                    if alcafoto.show_on_product_page:
                        alcafoto_show = "true"
                    else:
                        alcafoto_show = "false"

                    alcafotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": alcafoto_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 65,
                            "\"name\"": "\"" + str(alcafoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alcafotostr)

                if vals.get('alcafoto') == False:

                    alcafoto.nombre = ''

                    if alcafoto.show_on_product_page:
                        alcafoto_show = "true"
                    else:
                        alcafoto_show = "false"

                    alcafotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": alcafoto_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 65,
                            "\"name\"": "\"" + str(alcafoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alcafotostr)

                diafra = self.diafra
                if vals.get('diafra'):
                    id_diafra = self.env['diafra.zeigen'].search([('id', '=', vals['diafra'])])
                    diafra = id_diafra[0]

                    diafra_show = ''

                    if diafra.nombre == False:
                        diafra.nombre = ''

                    if diafra.show_on_product_page:
                        diafra_show = "true"
                    else:
                        diafra_show = "false"

                    diafrastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": diafra_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 66,
                            "\"name\"": "\"" + str(diafra.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(diafrastr)

                if vals.get('diafra') == False:

                    diafra.nombre = ''

                    if diafra.show_on_product_page:
                        diafra_show = "true"
                    else:
                        diafra_show = "false"

                    diafrastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": diafra_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 66,
                            "\"name\"": "\"" + str(diafra.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(diafrastr)

                portfilt = self.portfilt
                if vals.get('portfilt'):
                    id_portfilt = self.env['portfilt.zeigen'].search([('id', '=', vals['portfilt'])])
                    portfilt = id_portfilt[0]

                    portfilt_show = ''

                    if portfilt.nombre == False:
                        portfilt.nombre = ''

                    if portfilt.show_on_product_page:
                        portfilt_show = "true"
                    else:
                        portfilt_show = "false"

                    portfiltstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": portfilt_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 67,
                            "\"name\"": "\"" + str(portfilt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(portfiltstr)

                if vals.get('portfilt') == False:

                    portfilt.nombre = ''

                    if portfilt.show_on_product_page:
                        portfilt_show = "true"
                    else:
                        portfilt_show = "false"

                    portfiltstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": portfilt_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 67,
                            "\"name\"": "\"" + str(portfilt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(portfiltstr)

                prefoto = self.prefoto
                if vals.get('prefoto'):
                    id_prefoto = self.env['prefoto.zeigen'].search([('id', '=', vals['prefoto'])])
                    prefoto = id_prefoto[0]

                    prefoto_show = ''

                    if prefoto.nombre == False:
                        prefoto.nombre = ''

                    if prefoto.show_on_product_page:
                        prefoto_show = "true"
                    else:
                        prefoto_show = "false"

                    prefotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": prefoto_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 68,
                            "\"name\"": "\"" + str(prefoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(prefotostr)

                if vals.get('prefoto') == False:

                    prefoto.nombre = ''

                    if prefoto.show_on_product_page:
                        prefoto_show = "true"
                    else:
                        prefoto_show = "false"

                    prefotostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": prefoto_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 68,
                            "\"name\"": "\"" + str(prefoto.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(prefotostr)

                ecg = self.ecg
                if vals.get('ecg'):
                    id_ecg = self.env['ecg.zeigen'].search([('id', '=', vals['ecg'])])
                    ecg = id_ecg[0]

                    ecg_show = ''

                    if ecg.nombre == False:
                        ecg.nombre = ''

                    if ecg.show_on_product_page:
                        ecg_show = "true"
                    else:
                        ecg_show = "false"

                    ecgstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": ecg_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 69,
                            "\"name\"": "\"" + str(ecg.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ecgstr)

                if vals.get('ecg') == False:

                    ecg.nombre = ''

                    if ecg.show_on_product_page:
                        ecg_show = "true"
                    else:
                        ecg_show = "false"

                    ecgstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": ecg_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 69,
                            "\"name\"": "\"" + str(ecg.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ecgstr)

                traq = self.traq
                if vals.get('traq'):
                    id_traq = self.env['traq.zeigen'].search([('id', '=', vals['traq'])])
                    traq = id_traq[0]

                    traq_show = ''

                    if traq.nombre == False:
                        traq.nombre = ''

                    if traq.show_on_product_page:
                        traq_show = "true"
                    else:
                        traq_show = "false"

                    traqstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": traq_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 70,
                            "\"name\"": "\"" + str(traq.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(traqstr)

                if vals.get('traq') == False:

                    traq.nombre = ''

                    if traq.show_on_product_page:
                        traq_show = "true"
                    else:
                        traq_show = "false"

                    traqstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": traq_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 70,
                            "\"name\"": "\"" + str(traq.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(traqstr)

                preslongond = self.preslongond
                if vals.get('preslongond'):
                    id_preslongond = self.env['preslongond.zeigen'].search([('id', '=', vals['preslongond'])])
                    preslongond = id_preslongond[0]

                    preslongond_show = ''

                    if preslongond.nombre == False:
                        preslongond.nombre = ''

                    if preslongond.show_on_product_page:
                        preslongond_show = "true"
                    else:
                        preslongond_show = "false"

                    preslongondstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": preslongond_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 71,
                            "\"name\"": "\"" + str(preslongond.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(preslongondstr)

                if vals.get('preslongond') == False:

                    preslongond.nombre = ''

                    if preslongond.show_on_product_page:
                        preslongond_show = "true"
                    else:
                        preslongond_show = "false"

                    preslongondstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": preslongond_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 71,
                            "\"name\"": "\"" + str(preslongond.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(preslongondstr)

                contilum = self.contilum
                if vals.get('contilum'):
                    id_contilum = self.env['contilum.zeigen'].search([('id', '=', vals['contilum'])])
                    contilum = id_contilum[0]

                    contilum_show = ''

                    if contilum.nombre == False:
                        contilum.nombre = ''

                    if contilum.show_on_product_page:
                        contilum_show = "true"
                    else:
                        contilum_show = "false"

                    contilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": contilum_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 72,
                            "\"name\"": "\"" + str(contilum.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(contilumstr)

                if vals.get('contilum') == False:

                    contilum.nombre = ''

                    if contilum.show_on_product_page:
                        contilum_show = "true"
                    else:
                        contilum_show = "false"

                    contilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": contilum_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 72,
                            "\"name\"": "\"" + str(contilum.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(contilumstr)

                ilum = self.ilum
                if vals.get('ilum'):
                    id_ilum = self.env['ilum.zeigen'].search([('id', '=', vals['ilum'])])
                    ilum = id_ilum[0]

                    ilum_show = ''

                    if ilum.nombre == False:
                        ilum.nombre = ''

                    if ilum.show_on_product_page:
                        ilum_show = "true"
                    else:
                        ilum_show = "false"

                    ilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": ilum_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 73,
                            "\"name\"": "\"" + str(ilum.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ilumstr)

                if vals.get('ilum') == False:

                    ilum.nombre = ''

                    if ilum.show_on_product_page:
                        ilum_show = "true"
                    else:
                        ilum_show = "false"

                    ilumstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": ilum_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 73,
                            "\"name\"": "\"" + str(ilum.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(ilumstr)

                reprodlongonda = self.reprodlongonda
                if vals.get('reprodlongonda'):
                    id_reprodlongonda = self.env['reprodlongonda.zeigen'].search([('id', '=', vals['reprodlongonda'])])
                    reprodlongonda = id_reprodlongonda[0]

                    reprodlongonda_show = ''

                    if reprodlongonda.nombre == False:
                        reprodlongonda.nombre = ''

                    if reprodlongonda.show_on_product_page:
                        reprodlongonda_show = "true"
                    else:
                        reprodlongonda_show = "false"

                    reprodlongondastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                         "\"allow_filtering\"": 'false',
                                         "\"show_on_product_page\"": reprodlongonda_show, "\"display_order\"": 1,
                                         "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 74,
                            "\"name\"": "\"" + str(reprodlongonda.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reprodlongondastr)

                if vals.get('reprodlongonda') == False:

                    reprodlongonda.nombre = ''

                    if reprodlongonda.show_on_product_page:
                        reprodlongonda_show = "true"
                    else:
                        reprodlongonda_show = "false"

                    reprodlongondastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                         "\"allow_filtering\"": 'false',
                                         "\"show_on_product_page\"": reprodlongonda_show, "\"display_order\"": 1,
                                         "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 74,
                            "\"name\"": "\"" + str(reprodlongonda.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(reprodlongondastr)

                descomp = self.descomp
                if vals.get('descomp'):
                    id_descomp = self.env['descomp.zeigen'].search([('id', '=', vals['descomp'])])
                    descomp = id_descomp[0]

                    descomp_show = ''

                    if descomp.nombre == False:
                        descomp.nombre = ''

                    if descomp.show_on_product_page:
                        descomp_show = "true"
                    else:
                        descomp_show = "false"

                    descompstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": descomp_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 75,
                            "\"name\"": "\"" + str(descomp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(descompstr)

                if vals.get('descomp') == False:

                    descomp.nombre = ''

                    if descomp.show_on_product_page:
                        descomp_show = "true"
                    else:
                        descomp_show = "false"

                    descompstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": descomp_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 75,
                            "\"name\"": "\"" + str(descomp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(descompstr)

                voz = self.voz
                if vals.get('voz'):
                    id_voz = self.env['voz.zeigen'].search([('id', '=', vals['voz'])])
                    voz = id_voz[0]

                    voz_show = ''

                    if voz.nombre == False:
                        voz.nombre = ''

                    if voz.show_on_product_page:
                        voz_show = "true"
                    else:
                        voz_show = "false"

                    vozstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": voz_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 76,
                            "\"name\"": "\"" + str(voz.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(vozstr)

                if vals.get('voz') == False:

                    voz.nombre = ''

                    if voz.show_on_product_page:
                        voz_show = "true"
                    else:
                        voz_show = "false"

                    vozstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                              "\"show_on_product_page\"": voz_show, "\"display_order\"": 1,
                              "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 76,
                            "\"name\"": "\"" + str(voz.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(vozstr)

                luzdisp = self.luzdisp
                if vals.get('luzdisp'):
                    id_luzdisp = self.env['luzdisp.zeigen'].search([('id', '=', vals['luzdisp'])])
                    luzdisp = id_luzdisp[0]

                    luzdisp_show = ''

                    if luzdisp.nombre == False:
                        luzdisp.nombre = ''

                    if luzdisp.show_on_product_page:
                        luzdisp_show = "true"
                    else:
                        luzdisp_show = "false"

                    luzdispstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": luzdisp_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 77,
                            "\"name\"": "\"" + str(luzdisp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(luzdispstr)

                if vals.get('luzdisp') == False:

                    luzdisp.nombre = ''

                    if luzdisp.show_on_product_page:
                        luzdisp_show = "true"
                    else:
                        luzdisp_show = "false"

                    luzdispstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": luzdisp_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 77,
                            "\"name\"": "\"" + str(luzdisp.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(luzdispstr)

                kohler = self.kohler
                if vals.get('kohler'):
                    id_kohler = self.env['kohler.zeigen'].search([('id', '=', vals['kohler'])])
                    kohler = id_kohler[0]

                    kohler_show = ''

                    if kohler.nombre == False:
                        kohler.nombre = ''

                    if kohler.show_on_product_page:
                        kohler_show = "true"
                    else:
                        kohler_show = "false"

                    kohlerstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": kohler_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 78,
                            "\"name\"": "\"" + str(kohler.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(kohlerstr)

                if vals.get('kohler') == False:

                    kohler.nombre = ''

                    if kohler.show_on_product_page:
                        kohler_show = "true"
                    else:
                        kohler_show = "false"

                    kohlerstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": kohler_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 78,
                            "\"name\"": "\"" + str(kohler.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(kohlerstr)

                alimenelect = self.alimenelect
                if vals.get('alimenelect'):
                    id_alimenelect = self.env['alimenelect.zeigen'].search([('id', '=', vals['alimenelect'])])
                    alimenelect = id_alimenelect[0]

                    alimenelect_show = ''

                    if alimenelect.nombre == False:
                        alimenelect.nombre = ''

                    if alimenelect.show_on_product_page:
                        alimenelect_show = "true"
                    else:
                        alimenelect_show = "false"

                    alimenelectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": alimenelect_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 79,
                            "\"name\"": "\"" + str(alimenelect.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alimenelectstr)

                if vals.get('alimenelect') == False:

                    alimenelect.nombre = ''

                    if alimenelect.show_on_product_page:
                        alimenelect_show = "true"
                    else:
                        alimenelect_show = "false"

                    alimenelectstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                      "\"allow_filtering\"": 'false',
                                      "\"show_on_product_page\"": alimenelect_show, "\"display_order\"": 1,
                                      "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 79,
                            "\"name\"": "\"" + str(alimenelect.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(alimenelectstr)

                arrast = self.arrast
                if vals.get('arrast'):
                    id_arrast = self.env['arrast.zeigen'].search([('id', '=', vals['arrast'])])
                    arrast = id_arrast[0]

                    arrast_show = ''

                    if arrast.nombre == False:
                        arrast.nombre = ''

                    if arrast.show_on_product_page:
                        arrast_show = "true"
                    else:
                        arrast_show = "false"

                    arraststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": arrast_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 80,
                            "\"name\"": "\"" + str(arrast.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(arraststr)

                if vals.get('arrast') == False:

                    arrast.nombre = ''

                    if arrast.show_on_product_page:
                        arrast_show = "true"
                    else:
                        arrast_show = "false"

                    arraststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": arrast_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 80,
                            "\"name\"": "\"" + str(arrast.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(arraststr)

                manvias = self.manvias
                if vals.get('manvias'):
                    id_manvias = self.env['manvias.zeigen'].search([('id', '=', vals['manvias'])])
                    manvias = id_manvias[0]

                    manvias_show = ''

                    if manvias.nombre == False:
                        manvias.nombre = ''

                    if manvias.show_on_product_page:
                        manvias_show = "true"
                    else:
                        manvias_show = "false"

                    manviasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": manvias_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 81,
                            "\"name\"": "\"" + str(manvias.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(manviasstr)

                if vals.get('manvias') == False:

                    manvias.nombre = ''

                    if manvias.show_on_product_page:
                        manvias_show = "true"
                    else:
                        manvias_show = "false"

                    manviasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": manvias_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 81,
                            "\"name\"": "\"" + str(manvias.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(manviasstr)

                sistgast = self.sistgast
                if vals.get('sistgast'):
                    id_sistgast = self.env['sistgast.zeigen'].search([('id', '=', vals['sistgast'])])
                    sistgast = id_sistgast[0]

                    sistgast_show = ''

                    if sistgast.nombre == False:
                        sistgast.nombre = ''

                    if sistgast.show_on_product_page:
                        sistgast_show = "true"
                    else:
                        sistgast_show = "false"

                    sistgaststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistgast_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 82,
                            "\"name\"": "\"" + str(sistgast.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistgaststr)

                if vals.get('sistgast') == False:

                    sistgast.nombre = ''

                    if sistgast.show_on_product_page:
                        sistgast_show = "true"
                    else:
                        sistgast_show = "false"

                    sistgaststr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistgast_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 82,
                            "\"name\"": "\"" + str(sistgast.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistgaststr)

                fuentluz = self.fuentluz
                if vals.get('fuentluz'):
                    id_fuentluz = self.env['fuentluz.zeigen'].search([('id', '=', vals['fuentluz'])])
                    fuentluz = id_fuentluz[0]

                    fuentluz_show = ''

                    if fuentluz.nombre == False:
                        fuentluz.nombre = ''

                    if fuentluz.show_on_product_page:
                        fuentluz_show = "true"
                    else:
                        fuentluz_show = "false"

                    fuentluzstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": fuentluz_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 83,
                            "\"name\"": "\"" + str(fuentluz.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fuentluzstr)

                if vals.get('fuentluz') == False:

                    fuentluz.nombre = ''

                    if fuentluz.show_on_product_page:
                        fuentluz_show = "true"
                    else:
                        fuentluz_show = "false"

                    fuentluzstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": fuentluz_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 83,
                            "\"name\"": "\"" + str(fuentluz.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fuentluzstr)

                camdig = self.camdig
                if vals.get('camdig'):
                    id_camdig = self.env['camdig.zeigen'].search([('id', '=', vals['camdig'])])
                    camdig = id_camdig[0]

                    camdig_show = ''

                    if camdig.nombre == False:
                        camdig.nombre = ''

                    if camdig.show_on_product_page:
                        camdig_show = "true"
                    else:
                        camdig_show = "false"

                    camdigstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": camdig_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 84,
                            "\"name\"": "\"" + str(camdig.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(camdigstr)

                if vals.get('camdig') == False:

                    camdig.nombre = ''

                    if camdig.show_on_product_page:
                        camdig_show = "true"
                    else:
                        camdig_show = "false"

                    camdigstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": camdig_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 84,
                            "\"name\"": "\"" + str(camdig.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(camdigstr)

                filt = self.filt
                if vals.get('filt'):
                    id_filt = self.env['filt.zeigen'].search([('id', '=', vals['filt'])])
                    filt = id_filt[0]

                    filt_show = ''

                    if filt.nombre == False:
                        filt.nombre = ''

                    if filt.show_on_product_page:
                        filt_show = "true"
                    else:
                        filt_show = "false"

                    filtstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": filt_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 85,
                            "\"name\"": "\"" + str(filt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(filtstr)

                if vals.get('filt') == False:

                    filt.nombre = ''

                    if filt.show_on_product_page:
                        filt_show = "true"
                    else:
                        filt_show = "false"

                    filtstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": filt_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 85,
                            "\"name\"": "\"" + str(filt.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(filtstr)

                voltout = self.voltout
                if vals.get('voltout'):
                    id_voltout = self.env['voltout.zeigen'].search([('id', '=', vals['voltout'])])
                    voltout = id_voltout[0]

                    voltout_show = ''

                    if voltout.nombre == False:
                        voltout.nombre = ''

                    if voltout.show_on_product_page:
                        voltout_show = "true"
                    else:
                        voltout_show = "false"

                    voltoutstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": voltout_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 86,
                            "\"name\"": "\"" + str(voltout.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(voltoutstr)

                if vals.get('voltout') == False:

                    voltout.nombre = ''

                    if voltout.show_on_product_page:
                        voltout_show = "true"
                    else:
                        voltout_show = "false"

                    voltoutstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": voltout_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 86,
                            "\"name\"": "\"" + str(voltout.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(voltoutstr)

                sisturog = self.sisturog
                if vals.get('sisturog'):
                    id_sisturog = self.env['sisturog.zeigen'].search([('id', '=', vals['sisturog'])])
                    sisturog = id_sisturog[0]

                    sisturog_show = ''

                    if sisturog.nombre == False:
                        sisturog.nombre = ''

                    if sisturog.show_on_product_page:
                        sisturog_show = "true"
                    else:
                        sisturog_show = "false"

                    sisturogstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sisturog_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 87,
                            "\"name\"": "\"" + str(sisturog.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sisturogstr)

                if vals.get('sisturog') == False:

                    sisturog.nombre = ''

                    if sisturog.show_on_product_page:
                        sisturog_show = "true"
                    else:
                        sisturog_show = "false"

                    sisturogstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sisturog_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 87,
                            "\"name\"": "\"" + str(sisturog.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sisturogstr)

                cuidpacien = self.cuidpacien
                if vals.get('cuidpacien'):
                    id_cuidpacien = self.env['cuidpacien.zeigen'].search([('id', '=', vals['cuidpacien'])])
                    cuidpacien = id_cuidpacien[0]

                    cuidpacien_show = ''

                    if cuidpacien.nombre == False:
                        cuidpacien.nombre = ''

                    if cuidpacien.show_on_product_page:
                        cuidpacien_show = "true"
                    else:
                        cuidpacien_show = "false"

                    cuidpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": cuidpacien_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 88,
                            "\"name\"": "\"" + str(cuidpacien.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cuidpacienstr)

                if vals.get('cuidpacien') == False:

                    cuidpacien.nombre = ''

                    if cuidpacien.show_on_product_page:
                        cuidpacien_show = "true"
                    else:
                        cuidpacien_show = "false"

                    cuidpacienstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": cuidpacien_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 88,
                            "\"name\"": "\"" + str(cuidpacien.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(cuidpacienstr)

                poten = self.poten
                if vals.get('poten'):
                    id_poten = self.env['poten.zeigen'].search([('id', '=', vals['poten'])])
                    poten = id_poten[0]

                    poten_show = ''

                    if poten.nombre == False:
                        poten.nombre = ''

                    if poten.show_on_product_page:
                        poten_show = "true"
                    else:
                        poten_show = "false"

                    potenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": poten_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 89,
                            "\"name\"": "\"" + str(poten.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(potenstr)

                if vals.get('poten') == False:

                    poten.nombre = ''

                    if poten.show_on_product_page:
                        poten_show = "true"
                    else:
                        poten_show = "false"

                    potenstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": poten_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 89,
                            "\"name\"": "\"" + str(poten.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(potenstr)

                opccamposc = self.opccamposc
                if vals.get('opccamposc'):
                    id_opccamposc = self.env['opccamposc.zeigen'].search([('id', '=', vals['opccamposc'])])
                    opccamposc = id_opccamposc[0]

                    opccamposc_show = ''

                    if opccamposc.nombre == False:
                        opccamposc.nombre = ''

                    if opccamposc.show_on_product_page:
                        opccamposc_show = "true"
                    else:
                        opccamposc_show = "false"

                    opccamposcstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": opccamposc_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 90,
                            "\"name\"": "\"" + str(opccamposc.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opccamposcstr)

                if vals.get('opccamposc') == False:

                    opccamposc.nombre = ''

                    if opccamposc.show_on_product_page:
                        opccamposc_show = "true"
                    else:
                        opccamposc_show = "false"

                    opccamposcstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": opccamposc_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 90,
                            "\"name\"": "\"" + str(opccamposc.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opccamposcstr)

                sistnerv = self.sistnerv
                if vals.get('sistnerv'):
                    id_sistnerv = self.env['sistnerv.zeigen'].search([('id', '=', vals['sistnerv'])])
                    sistnerv = id_sistnerv[0]

                    sistnerv_show = ''

                    if sistnerv.nombre == False:
                        sistnerv.nombre = ''

                    if sistnerv.show_on_product_page:
                        sistnerv_show = "true"
                    else:
                        sistnerv_show = "false"

                    sistnervstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistnerv_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 91,
                            "\"name\"": "\"" + str(sistnerv.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistnervstr)

                if vals.get('sistnerv') == False:

                    sistnerv.nombre = ''

                    if sistnerv.show_on_product_page:
                        sistnerv_show = "true"
                    else:
                        sistnerv_show = "false"

                    sistnervstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistnerv_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 91,
                            "\"name\"": "\"" + str(sistnerv.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistnervstr)

                sistmet = self.sistmet
                if vals.get('sistmet'):
                    id_sistmet = self.env['sistmet.zeigen'].search([('id', '=', vals['sistmet'])])
                    sistmet = id_sistmet[0]

                    sistmet_show = ''

                    if sistmet.nombre == False:
                        sistmet.nombre = ''

                    if sistmet.show_on_product_page:
                        sistmet_show = "true"
                    else:
                        sistmet_show = "false"

                    sistmetstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sistmet_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 92,
                            "\"name\"": "\"" + str(sistmet.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistmetstr)

                if vals.get('sistmet') == False:

                    sistmet.nombre = ''

                    if sistmet.show_on_product_page:
                        sistmet_show = "true"
                    else:
                        sistmet_show = "false"

                    sistmetstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sistmet_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 92,
                            "\"name\"": "\"" + str(sistmet.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistmetstr)

                opcepiflo = self.opcepiflo
                if vals.get('opcepiflo'):
                    id_opcepiflo = self.env['opcepiflo.zeigen'].search([('id', '=', vals['opcepiflo'])])
                    opcepiflo = id_opcepiflo[0]

                    opcepiflo_show = ''

                    if opcepiflo.nombre == False:
                        opcepiflo.nombre = ''

                    if opcepiflo.show_on_product_page:
                        opcepiflo_show = "true"
                    else:
                        opcepiflo_show = "false"

                    opcepiflostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": opcepiflo_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 93,
                            "\"name\"": "\"" + str(opcepiflo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opcepiflostr)

                if vals.get('opcepiflo') == False:

                    opcepiflo.nombre = ''

                    if opcepiflo.show_on_product_page:
                        opcepiflo_show = "true"
                    else:
                        opcepiflo_show = "false"

                    opcepiflostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": opcepiflo_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 93,
                            "\"name\"": "\"" + str(opcepiflo.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opcepiflostr)

                opccontfas = self.opccontfas
                if vals.get('opccontfas'):
                    id_opccontfas = self.env['opccontfas.zeigen'].search([('id', '=', vals['opccontfas'])])
                    opccontfas = id_opccontfas[0]

                    opccontfas_show = ''

                    if opccontfas.nombre == False:
                        opccontfas.nombre = ''

                    if opccontfas.show_on_product_page:
                        opccontfas_show = "true"
                    else:
                        opccontfas_show = "false"

                    opccontfasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": opccontfas_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 94,
                            "\"name\"": "\"" + str(opccontfas.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opccontfasstr)

                if vals.get('opccontfas') == False:

                    opccontfas.nombre = ''

                    if opccontfas.show_on_product_page:
                        opccontfas_show = "true"
                    else:
                        opccontfas_show = "false"

                    opccontfasstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                     "\"allow_filtering\"": 'false',
                                     "\"show_on_product_page\"": opccontfas_show, "\"display_order\"": 1,
                                     "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 94,
                            "\"name\"": "\"" + str(opccontfas.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(opccontfasstr)

                monidesem = self.monidesem
                if vals.get('monidesem'):
                    id_monidesem = self.env['monidesem.zeigen'].search([('id', '=', vals['monidesem'])])
                    monidesem = id_monidesem[0]

                    monidesem_show = ''

                    if monidesem.nombre == False:
                        monidesem.nombre = ''

                    if monidesem.show_on_product_page:
                        monidesem_show = "true"
                    else:
                        monidesem_show = "false"

                    monidesemstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": monidesem_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 95,
                            "\"name\"": "\"" + str(monidesem.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(monidesemstr)

                if vals.get('monidesem') == False:

                    monidesem.nombre = ''

                    if monidesem.show_on_product_page:
                        monidesem_show = "true"
                    else:
                        monidesem_show = "false"

                    monidesemstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": monidesem_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 95,
                            "\"name\"": "\"" + str(monidesem.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(monidesemstr)

                disttrab = self.disttrab
                if vals.get('disttrab'):
                    id_disttrab = self.env['disttrab.zeigen'].search([('id', '=', vals['disttrab'])])
                    disttrab = id_disttrab[0]

                    disttrab_show = ''

                    if disttrab.nombre == False:
                        disttrab.nombre = ''

                    if disttrab.show_on_product_page:
                        disttrab_show = "true"
                    else:
                        disttrab_show = "false"

                    disttrabstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": disttrab_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 96,
                            "\"name\"": "\"" + str(disttrab.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(disttrabstr)

                if vals.get('disttrab') == False:

                    disttrab.nombre = ''

                    if disttrab.show_on_product_page:
                        disttrab_show = "true"
                    else:
                        disttrab_show = "false"

                    disttrabstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": disttrab_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 96,
                            "\"name\"": "\"" + str(disttrab.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(disttrabstr)

                sistelev = self.sistelev
                if vals.get('sistelev'):
                    id_sistelev = self.env['sistelev.zeigen'].search([('id', '=', vals['sistelev'])])
                    sistelev = id_sistelev[0]

                    sistelev_show = ''

                    if sistelev.nombre == False:
                        sistelev.nombre = ''

                    if sistelev.show_on_product_page:
                        sistelev_show = "true"
                    else:
                        sistelev_show = "false"

                    sistelevstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistelev_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 97,
                            "\"name\"": "\"" + str(sistelev.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistelevstr)

                if vals.get('sistelev') == False:

                    sistelev.nombre = ''

                    if sistelev.show_on_product_page:
                        sistelev_show = "true"
                    else:
                        sistelev_show = "false"

                    sistelevstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": sistelev_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 97,
                            "\"name\"": "\"" + str(sistelev.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sistelevstr)

                garantia = self.garantia
                if vals.get('garantia'):
                    id_garantia = self.env['garantia.zeigen'].search([('id', '=', vals['garantia'])])
                    garantia = id_garantia[0]

                    garantia_show = ''

                    if garantia.nombre == False:
                        garantia.nombre = ''

                    if garantia.show_on_product_page:
                        garantia_show = "true"
                    else:
                        garantia_show = "false"

                    garantiastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": garantia_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 98,
                            "\"name\"": "\"" + str(garantia.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(garantiastr)

                if vals.get('garantia') == False:

                    garantia.nombre = ''

                    if garantia.show_on_product_page:
                        garantia_show = "true"
                    else:
                        garantia_show = "false"

                    garantiastr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": garantia_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 98,
                            "\"name\"": "\"" + str(garantia.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(garantiastr)

                zoom = self.zoom
                if vals.get('zoom'):
                    id_zoom = self.env['zoom.zeigen'].search([('id', '=', vals['zoom'])])
                    zoom = id_zoom[0]

                    zoom_show = ''

                    if zoom.nombre == False:
                        zoom.nombre = ''

                    if zoom.show_on_product_page:
                        zoom_show = "true"
                    else:
                        zoom_show = "false"

                    zoomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": zoom_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 100,
                            "\"name\"": "\"" + str(zoom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(zoomstr)

                if vals.get('zoom') == False:

                    zoom.nombre = ''

                    if zoom.show_on_product_page:
                        zoom_show = "true"
                    else:
                        zoom_show = "false"

                    zoomstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                               "\"show_on_product_page\"": zoom_show, "\"display_order\"": 1,
                               "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 100,
                            "\"name\"": "\"" + str(zoom.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(zoomstr)

                observaciones = self.observaciones
                if vals.get('observaciones'):

                    if observaciones == False:
                        observaciones = ''


                    observacionesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false',
                                        "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                        "\"attribute_type\"": "\"Custom text\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 102,
                            "\"name\"": "\"" + str(observaciones) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(observacionesstr)

                if vals.get('observaciones') == False:

                    observaciones = ''


                    observacionesstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                        "\"allow_filtering\"": 'false',
                                        "\"show_on_product_page\"": 'true', "\"display_order\"": 1,
                                        "\"attribute_type\"": "\"Custom text\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 102,
                            "\"name\"": "\"" + str(observaciones) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(observacionesstr)

                capaci = self.capaci
                if vals.get('capaci'):
                    id_capaci = self.env['capaci.zeigen'].search([('id', '=', vals['capaci'])])
                    capaci = id_capaci[0]

                    capacis_show = ''

                    if capaci.nombre == False:
                        capaci.nombre = ''

                    if capaci.show_on_product_page:
                        capaci_show = "true"
                    else:
                        capaci_show = "false"

                    capacistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": capaci_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 104,
                            "\"name\"": "\"" + str(capaci.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(capacistr)

                if vals.get('capaci') == False:

                    capaci.nombre = ''

                    if capaci.show_on_product_page:
                        capaci_show = "true"
                    else:
                        capaci_show = "false"

                    capacistr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                 "\"show_on_product_page\"": capaci_show, "\"display_order\"": 1,
                                 "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 104,
                            "\"name\"": "\"" + str(capaci.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(capacistr)

                software = self.software
                if vals.get('software'):
                    id_software = self.env['software.zeigen'].search([('id', '=', vals['software'])])
                    software = id_software[0]

                    software_show = ''

                    if software.nombre == False:
                        software.nombre = ''

                    if software.show_on_product_page:
                        software_show = "true"
                    else:
                        software_show = "false"

                    softwarestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": software_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 106,
                            "\"name\"": "\"" + str(software.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(softwarestr)

                if vals.get('software') == False:

                    software.nombre = ''

                    if software.show_on_product_page:
                        software_show = "true"
                    else:
                        software_show = "false"

                    softwarestr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                   "\"allow_filtering\"": 'false',
                                   "\"show_on_product_page\"": software_show, "\"display_order\"": 1,
                                   "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 106,
                            "\"name\"": "\"" + str(software.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(softwarestr)

                video = self.video
                if vals.get('video'):
                    id_video = self.env['video.zeigen'].search([('id', '=', vals['video'])])
                    video = id_video[0]

                    video_show = ''

                    if video.nombre == False:
                        video.nombre = ''

                    if video.show_on_product_page:
                        video_show = "true"
                    else:
                        video_show = "false"

                    videostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": video_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 107,
                            "\"name\"": "\"" + str(video.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(videostr)

                if vals.get('video') == False:

                    video.nombre = ''

                    if video.show_on_product_page:
                        video_show = "true"
                    else:
                        video_show = "false"

                    videostr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null', "\"allow_filtering\"": 'false',
                                "\"show_on_product_page\"": video_show, "\"display_order\"": 1,
                                "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 107,
                            "\"name\"": "\"" + str(video.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(videostr)

                resolus = self.resolus
                if vals.get('resolus'):
                    id_resolus = self.env['resolus.zeigen'].search([('id', '=', vals['resolus'])])
                    resolus = id_resolus[0]

                    resolus_show = ''

                    if resolus.nombre == False:
                        resolus.nombre = ''

                    if resolus.show_on_product_page:
                        resolus_show = "true"
                    else:
                        resolus_show = "false"

                    resolusstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": resolus_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 108,
                            "\"name\"": "\"" + str(resolus.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(resolusstr)

                if vals.get('resolus') == False:

                    resolus.nombre = ''

                    if resolus.show_on_product_page:
                        resolus_show = "true"
                    else:
                        resolus_show = "false"

                    resolusstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": resolus_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 108,
                            "\"name\"": "\"" + str(resolus.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(resolusstr)

                fuentalim = self.fuentalim
                if vals.get('fuentalim'):
                    id_fuentalim = self.env['fuentalim.zeigen'].search([('id', '=', vals['fuentalim'])])
                    fuentalim = id_fuentalim[0]

                    fuentalim_show = ''

                    if fuentalim.nombre == False:
                        fuentalim.nombre = ''

                    if fuentalim.show_on_product_page:
                        fuentalim_show = "true"
                    else:
                        fuentalim_show = "false"

                    fuentalimstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": fuentalim_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 109,
                            "\"name\"": "\"" + str(fuentalim.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fuentalimstr)

                if vals.get('fuentalim') == False:

                    fuentalim.nombre = ''

                    if fuentalim.show_on_product_page:
                        fuentalim_show = "true"
                    else:
                        fuentalim_show = "false"

                    fuentalimstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                    "\"allow_filtering\"": 'false',
                                    "\"show_on_product_page\"": fuentalim_show, "\"display_order\"": 1,
                                    "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 109,
                            "\"name\"": "\"" + str(fuentalim.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(fuentalimstr)

                sonidos = self.sonidos
                if vals.get('sonidos'):
                    id_sonidos = self.env['sonidos.zeigen'].search([('id', '=', vals['sonidos'])])
                    sonidos = id_sonidos[0]

                    sonidos_show = ''

                    if sonidos.nombre == False:
                        sonidos.nombre = ''

                    if sonidos.show_on_product_page:
                        sonidos_show = "true"
                    else:
                        sonidos_show = "false"

                    sonidosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sonidos_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 110,
                            "\"name\"": "\"" + str(sonidos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

                    atributstr.append(sonidosstr)

                if vals.get('sonidos') == False:

                    sonidos.nombre = ''

                    if sonidos.show_on_product_page:
                        sonidos_show = "true"
                    else:
                        sonidos_show = "false"

                    sonidosstr = {'\'attribute_type_id\'': 0, "\"custom_value\"": 'null',
                                  "\"allow_filtering\"": 'false',
                                  "\"show_on_product_page\"": sonidos_show, "\"display_order\"": 1,
                                  "\"attribute_type\"": "\"Option\"", "\"specification_attribute_option\"": {
                            "\"specification_attribute_id\"": 110,
                            "\"name\"": "\"" + str(sonidos.display_name) + "\"", "\"color_squares_rgb\"": 'null',
                            "\"display_order\"": 0}}

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
                                "tags": tags,
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
                            "tags": tags,
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
                incrementable = (vals['price_unit'] * self.incrementables / 100)

                unitario = vals['price_unit'] + incrementable

                subtotal_proveedor = vals['price_unit'] + incrementable

                vals.update(
                    {'price_unit': unitario, 'porcentaje': incrementable, 'subtotal_proveedor': subtotal_proveedor})

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
                'price_subtotal': (subtotal_proveedor * vals['product_qty']),
                # 'price_subtotal': (vals['price_unit'] * vals['product_qty']),
                'subtotal_proveedor': subtotal_proveedor * vals['product_qty'],
            })

            if line.move_ids.ids != []:
                all_records = self.env['stock.valuation.layer'].search(
                    [('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                all_records.value = taxes['total_excluded'] + incrementable + sum(
                    t.get('amount', 0.0) for t in taxes.get('taxes', []))

    @api.depends('order_line.price_total')
    def _amount_all(self):
        # for order in self:
        order = self

        amount_untaxed_a = amount_tax_a = porcentaje_a = subtotal_proveedor_a = 0.0

        for line in order.order_line:
            amount_untaxed = amount_tax = porcentaje = subtotal_proveedor = 0.0
            amount_untaxed += line.price_unit
            amount_tax += line.price_tax
            porcentaje += line.porcentaje
            subtotal_proveedor += line.subtotal_proveedor

            if order.currency_id.id != self.user_id.currency_id:
                amount_untaxed = order.currency_id._convert(amount_untaxed, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                amount_tax = order.currency_id._convert(amount_tax, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                porcentaje = order.currency_id._convert(porcentaje, self.user_id.currency_id, self.user_id.company_id, self.date_order)
                subtotal_proveedor = order.currency_id._convert(subtotal_proveedor, self.user_id.currency_id, self.user_id.company_id, self.date_order)

                # line.price_subtotal =  subtotal_proveedor
                line.price_subtotal = subtotal_proveedor + amount_tax

                amount_untaxed_a += amount_untaxed
                amount_tax_a += amount_tax
                porcentaje_a += porcentaje
                subtotal_proveedor_a += subtotal_proveedor

            if line.move_ids.ids != []:
                all_records = self.env['stock.valuation.layer'].search(
                    [('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                all_records.value = line.price_subtotal

        order.update({
            'amount_untaxed': order.currency_id.round(subtotal_proveedor_a),
            # 'amount_untaxed': order.currency_id.round(subtotal_proveedor_a) + order.currency_id.round(amount_tax_a),
            'amount_tax': order.currency_id.round(amount_tax_a),
            # 'amount_total': subtotal_proveedor_a +((subtotal_proveedor_a)*.16),
            'amount_total': order.currency_id.round(subtotal_proveedor_a) + order.currency_id.round(amount_tax_a),
            # 'iva': (subtotal_proveedor_a)*.16,
            'iva': (order.currency_id.round(subtotal_proveedor_a) + order.currency_id.round(amount_tax_a)) * .16,
        })


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    porcentaje = fields.Float('Porcentaje')
    subtotal_proveedor = fields.Float('Sub Proveedor')

    @api.depends('product_qty', 'price_unit', 'taxes_id')
    def _compute_amount(self):
        incrementable = 0
        subtotal_proveedor = 0

        unitario = 0

        for line in self:

            vals = line._prepare_compute_all_values()

            if self.order_id.incrementables > 0:
                incrementable = (vals['price_unit'] * self.order_id.incrementables / 100)

                unitario = vals['price_unit'] + incrementable

                subtotal_proveedor = vals['price_unit'] + incrementable

                vals.update(
                    {'price_unit': unitario, 'porcentaje': incrementable, 'subtotal_proveedor': subtotal_proveedor})

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
                'price_subtotal': (subtotal_proveedor * vals['product_qty']),
                # 'price_subtotal': (vals['price_unit'] * vals['product_qty']),
                'subtotal_proveedor': subtotal_proveedor * vals['product_qty'],
            })

            if line.move_ids.ids != []:
                all_records = self.env['stock.valuation.layer'].search(
                    [('product_id', '=', line.product_id.id), ('stock_move_id', '=', line.move_ids.ids[0])])

                all_records.value = taxes['total_excluded'] + incrementable + sum(
                    t.get('amount', 0.0) for t in taxes.get('taxes', []))

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
