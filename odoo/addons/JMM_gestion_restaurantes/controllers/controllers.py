# -*- coding: utf-8 -*-
# from odoo import http


# class GestionRestaurantes(http.Controller):
#     @http.route('/gestion__restaurantes/gestion__restaurantes', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/gestion__restaurantes/gestion__restaurantes/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('gestion__restaurantes.listing', {
#             'root': '/gestion__restaurantes/gestion__restaurantes',
#             'objects': http.request.env['gestion__restaurantes.gestion__restaurantes'].search([]),
#         })

#     @http.route('/gestion__restaurantes/gestion__restaurantes/objects/<model("gestion__restaurantes.gestion__restaurantes"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('gestion__restaurantes.object', {
#             'object': obj
#         })

