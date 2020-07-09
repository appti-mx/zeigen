# -*- coding: utf-8 -*-
from odoo import http

# class Apizeigen(http.Controller):
#     @http.route('/apizeigen/apizeigen/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/apizeigen/apizeigen/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('apizeigen.listing', {
#             'root': '/apizeigen/apizeigen',
#             'objects': http.request.env['apizeigen.apizeigen'].search([]),
#         })

#     @http.route('/apizeigen/apizeigen/objects/<model("apizeigen.apizeigen"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('apizeigen.object', {
#             'object': obj
#         })