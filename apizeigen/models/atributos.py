# -*- coding: utf-8 -*-
import itertools

import requests


from odoo import api, fields, models, tools, _, SUPERUSER_ID
from odoo.exceptions import ValidationError, RedirectWarning, UserError
from odoo.osv import expression
from odoo.tools import pycompat
from requests.auth import HTTPBasicAuth
import json


class Tags(models.Model):
    _name = 'tags.zeigen'

    name = fields.Char('Nombre')

class marcazeigen(models.Model):
    _name = 'marca.zeigen'
    _description = 'marca_zeigen'
    _rec_name = 'nombre'

    id_atribute = fields.Integer('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class subcategoriazeigen(models.Model):
    _name = 'subcategoria.zeigen'
    _description = 'subcategoria_zeigen'
    _rec_name = 'nombre'

    id_atribute = fields.Integer('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class marcazeigen(models.Model):
    _name = 'marca.zeigen'
    _description = 'marca_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class subcategoriazeigen(models.Model):
    _name = 'subcategoria.zeigen'
    _description = 'subcategoria_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class marcasanatomzeigen(models.Model):
    _name = 'marcasanatom.zeigen'
    _description = 'marcasanatom_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class materialeszeigen(models.Model):
    _name = 'materiales.zeigen'
    _description = 'materiales_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ojoszeigen(models.Model):
    _name = 'ojos.zeigen'
    _description = 'ojos_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class tipozeigen(models.Model):
    _name = 'tipo.zeigen'
    _description = 'tipo_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class nivelzeigen(models.Model):
    _name = 'nivel.zeigen'
    _description = 'nivel_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class pulsozeigen(models.Model):
    _name = 'pulso.zeigen'
    _description = 'pulso_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class respiracionzeigen(models.Model):
    _name = 'respiracion.zeigen'
    _description = 'respiracion_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class incluyezeigen(models.Model):
    _name = 'incluye.zeigen'
    _description = 'incluye_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class cuerpozeigen(models.Model):
    _name = 'cuerpo.zeigen'
    _description = 'cuerpo_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class cabezalzeigen(models.Model):
    _name = 'cabezal.zeigen'
    _description = 'cabezal_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class velocidadzeigen(models.Model):
    _name = 'velocidad.zeigen'
    _description = 'velocidad_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class desfibrilaciozeigen(models.Model):
    _name = 'desfibrilacio.zeigen'
    _description = 'desfibrilacio_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class pechozeigen(models.Model):
    _name = 'pecho.zeigen'
    _description = 'pecho_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class rtempzeigen(models.Model):
    _name = 'rtemp.zeigen'
    _description = 'rtemp_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class tipcabezalzeigen(models.Model):
    _name = 'tipcabezal.zeigen'
    _description = 'tipcabezal_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class inccabezalzeigen(models.Model):
    _name = 'inccabezal.zeigen'
    _description = 'inccabezal_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class platozeigen(models.Model):
    _name = 'plato.zeigen'
    _description = 'plato_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class auscultzeigen(models.Model):
    _name = 'auscult.zeigen'
    _description = 'auscult_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class rcpzeigen(models.Model):
    _name = 'rcp.zeigen'
    _description = 'rcp_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class tiempozeigen(models.Model):
    _name = 'tiempo.zeigen'
    _description = 'tiempo_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class cabgirzeigen(models.Model):
    _name = 'cabgir.zeigen'
    _description = 'cabgir_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ajusdiotzeigen(models.Model):
    _name = 'ajusdiot.zeigen'
    _description = 'ajusdiot_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class rangozeigen(models.Model):
    _name = 'rango.zeigen'
    _description = 'rango_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class pressangzeigen(models.Model):
    _name = 'pressang.zeigen'
    _description = 'pressang_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class reflejoszeigen(models.Model):
    _name = 'reflejos.zeigen'
    _description = 'reflejos_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class reproduczeigen(models.Model):
    _name = 'reproduc.zeigen'
    _description = 'reproduc_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ajusinterpuzeigen(models.Model):
    _name = 'ajusinterpu.zeigen'
    _description = 'ajusinterpu_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class oculareszeigen(models.Model):
    _name = 'oculares.zeigen'
    _description = 'oculares_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class errlinzeigen(models.Model):
    _name = 'errlin.zeigen'
    _description = 'errlin_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sindromzeigen(models.Model):
    _name = 'sindrom.zeigen'
    _description = 'sindrom_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class fichpacienzeigen(models.Model):
    _name = 'fichpacien.zeigen'
    _description = 'fichpacien_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class pothotzeigen(models.Model):
    _name = 'pothot.zeigen'
    _description = 'pothot_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ocpriszeigen(models.Model):
    _name = 'ocpris.zeigen'
    _description = 'ocpris_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class revolzeigen(models.Model):
    _name = 'revol.zeigen'
    _description = 'revol_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class dimtinazeigen(models.Model):
    _name = 'dimtina.zeigen'
    _description = 'dimtina_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class cianzeigen(models.Model):
    _name = 'cian.zeigen'
    _description = 'cian_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class bombinfuzeigen(models.Model):
    _name = 'bombinfu.zeigen'
    _description = 'bombinfu_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class bombinfuzeigen(models.Model):
    _name = 'bombinfu.zeigen'
    _description = 'bombinfu_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class rotorzeigen(models.Model):
    _name = 'rotor.zeigen'
    _description = 'rotor_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class opticazeigen(models.Model):
    _name = 'optica.zeigen'
    _description = 'optica_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class objectzeigen(models.Model):
    _name = 'object.zeigen'
    _description = 'object_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class motorzeigen(models.Model):
    _name = 'motor.zeigen'
    _description = 'motor_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sudazeigen(models.Model):
    _name = 'suda.zeigen'
    _description = 'suda_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class llorazeigen(models.Model):
    _name = 'llora.zeigen'
    _description = 'llora_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class dimmantizeigen(models.Model):
    _name = 'dimmanti.zeigen'
    _description = 'dimmanti_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class aumenzeigen(models.Model):
    _name = 'aumen.zeigen'
    _description = 'aumen_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class enfozeigen(models.Model):
    _name = 'enfo.zeigen'
    _description = 'enfo_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class contremzeigen(models.Model):
    _name = 'contrem.zeigen'
    _description = 'contrem_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class tablezeigen(models.Model):
    _name = 'table.zeigen'
    _description = 'table_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class anchbandzeigen(models.Model):
    _name = 'anchband.zeigen'
    _description = 'anchband_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class platinazeigen(models.Model):
    _name = 'platina.zeigen'
    _description = 'platina_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class tamplatzeigen(models.Model):
    _name = 'tamplat.zeigen'
    _description = 'tamplat_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sistoptzeigen(models.Model):
    _name = 'sistopt.zeigen'
    _description = 'sistopt_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class compuzeigen(models.Model):
    _name = 'compu.zeigen'
    _description = 'compu_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class procsimuzeigen(models.Model):
    _name = 'procsimu.zeigen'
    _description = 'procsimu_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class rangfotozeigen(models.Model):
    _name = 'rangfoto.zeigen'
    _description = 'rangfoto_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class topezeigen(models.Model):
    _name = 'tope.zeigen'
    _description = 'tope_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class condenzeigen(models.Model):
    _name = 'conden.zeigen'
    _description = 'conden_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class alcalongzeigen(models.Model):
    _name = 'alcalong.zeigen'
    _description = 'alcalong_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class conectzeigen(models.Model):
    _name = 'conect.zeigen'
    _description = 'conect_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class puntionzeigen(models.Model):
    _name = 'puntion.zeigen'
    _description = 'puntion_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class alcafotozeigen(models.Model):
    _name = 'alcafoto.zeigen'
    _description = 'alcafoto_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class diafrazeigen(models.Model):
    _name = 'diafra.zeigen'
    _description = 'diafra_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class portfiltzeigen(models.Model):
    _name = 'portfilt.zeigen'
    _description = 'portfilt_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class prefotozeigen(models.Model):
    _name = 'prefoto.zeigen'
    _description = 'prefoto_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ecgzeigen(models.Model):
    _name = 'ecg.zeigen'
    _description = 'ecg_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class traqzeigen(models.Model):
    _name = 'traq.zeigen'
    _description = 'traq_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class preslongondzeigen(models.Model):
    _name = 'preslongond.zeigen'
    _description = 'preslongond_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class contilumzeigen(models.Model):
    _name = 'contilum.zeigen'
    _description = 'contilum_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class ilumzeigen(models.Model):
    _name = 'ilum.zeigen'
    _description = 'ilum_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class reprodlongondazeigen(models.Model):
    _name = 'reprodlongonda.zeigen'
    _description = 'reprodlongonda_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class descompzeigen(models.Model):
    _name = 'descomp.zeigen'
    _description = 'descomp_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class vozzeigen(models.Model):
    _name = 'voz.zeigen'
    _description = 'voz_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class luzdispzeigen(models.Model):
    _name = 'luzdisp.zeigen'
    _description = 'luzdisp_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class kohlerzeigen(models.Model):
    _name = 'kohler.zeigen'
    _description = 'kohler_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class alimenelectzeigen(models.Model):
    _name = 'alimenelect.zeigen'
    _description = 'alimenelect_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class arrastzeigen(models.Model):
    _name = 'arrast.zeigen'
    _description = 'arrastelect_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class manviaszeigen(models.Model):
    _name = 'manvias.zeigen'
    _description = 'manvias_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sistgastzeigen(models.Model):
    _name = 'sistgast.zeigen'
    _description = 'sistgast_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class fuentluzzeigen(models.Model):
    _name = 'fuentluz.zeigen'
    _description = 'fuentluz_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class camdigzeigen(models.Model):
    _name = 'camdig.zeigen'
    _description = 'camdig_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class filtzeigen(models.Model):
    _name = 'filt.zeigen'
    _description = 'filt_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class voltoutzeigen(models.Model):
    _name = 'voltout.zeigen'
    _description = 'voltout_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sisturogzeigen(models.Model):
    _name = 'sisturog.zeigen'
    _description = 'sisturog_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class cuidpacienzeigen(models.Model):
    _name = 'cuidpacien.zeigen'
    _description = 'cuidpacien_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class potenzeigen(models.Model):
    _name = 'poten.zeigen'
    _description = 'poten_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class opccamposczeigen(models.Model):
    _name = 'opccamposc.zeigen'
    _description = 'opccamposc_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sistnervzeigen(models.Model):
    _name = 'sistnerv.zeigen'
    _description = 'sistnerv_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sistmetzeigen(models.Model):
    _name = 'sistmet.zeigen'
    _description = 'sistmet_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class opcepiflozeigen(models.Model):
    _name = 'opcepiflo.zeigen'
    _description = 'opcepiflo_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class opccontfaszeigen(models.Model):
    _name = 'opccontfas.zeigen'
    _description = 'opccontfas_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class monidesemzeigen(models.Model):
    _name = 'monidesem.zeigen'
    _description = 'monidesem_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class disttrabzeigen(models.Model):
    _name = 'disttrab.zeigen'
    _description = 'disttrab_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sistelevzeigen(models.Model):
    _name = 'sistelev.zeigen'
    _description = 'sistelev_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class garantiazeigen(models.Model):
    _name = 'garantia.zeigen'
    _description = 'garantia_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class zoomzeigen(models.Model):
    _name = 'zoom.zeigen'
    _description = 'zoom_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class observacioneszeigen(models.Model):
    _name = 'observaciones.zeigen'
    _description = 'observaciones_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class capacizeigen(models.Model):
    _name = 'capaci.zeigen'
    _description = 'capaci_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class softwarezeigen(models.Model):
    _name = 'software.zeigen'
    _description = 'software_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class videozeigen(models.Model):
    _name = 'video.zeigen'
    _description = 'video_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class resoluszeigen(models.Model):
    _name = 'resolus.zeigen'
    _description = 'resolus_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class fuentalimzeigen(models.Model):
    _name = 'fuentalim.zeigen'
    _description = 'fuentalim_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')


class sonidoszeigen(models.Model):
    _name = 'sonidos.zeigen'
    _description = 'sonidos_zeigen'
    _rec_name = 'nombre'
    id_atribute = fields.Char('Id')
    nombre = fields.Char('Nombre')
    order = fields.Integer('Orden')
    show_on_product_page = fields.Boolean('Ver en pagina')

