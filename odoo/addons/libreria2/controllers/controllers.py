# -*- coding: utf-8 -*-
# from odoo import http


# class Libreria2(http.Controller):
#     @http.route('/libreria2/libreria2', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/libreria2/libreria2/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('libreria2.listing', {
#             'root': '/libreria2/libreria2',
#             'objects': http.request.env['libreria2.libreria2'].search([]),
#         })

#     @http.route('/libreria2/libreria2/objects/<model("libreria2.libreria2"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('libreria2.object', {
#             'object': obj
#         })

