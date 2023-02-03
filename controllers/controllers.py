# -*- coding: utf-8 -*-
# from odoo import http


# class Salespop(http.Controller):
#     @http.route('/salespop/salespop', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/salespop/salespop/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('salespop.listing', {
#             'root': '/salespop/salespop',
#             'objects': http.request.env['salespop.salespop'].search([]),
#         })

#     @http.route('/salespop/salespop/objects/<model("salespop.salespop"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('salespop.object', {
#             'object': obj
#         })
