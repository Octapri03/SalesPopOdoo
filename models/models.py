# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import timedelta, datetime


class user(models.Model):
    _inherit = 'res.partner'
    _name = 'res.partner'
    _description = 'salespop users'

    name = fields.Char()
    userName = fields.Integer()
    mail = fields.Char()
    password = fields.Char()
    numTel = fields.Integer()
    onSale = fields.One2many('salespop.product', 'seller')
    favs = fields.One2many('salespop.product', 'fav')

class product(models.Model):
    _name = 'salespop.product'
    _description = 'salespop products'

    name = fields.Char()
    price = fields.Integer()
    description = fields.Char()
    ubication = fields.Char()
    publicationDate = fields.Datetime(readonly=True, default=fields.Datetime.now)
    seller = fields.Many2one('res.partner', ondelete = "cascade")
    fav = fields.Many2one('res.partner')

class category(models.Model):
    _name = 'salespop.category'
    _description = 'salespop categories'

    name = fields.Char()


#private String name;
#private int price;
#private String description;
#private String ubication;
#private Categoria categoria;
#private Date fechaPubli;
#private Usuario vendedor;
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
