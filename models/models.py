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

    isUserPop = fields.Boolean(default = False)

class product(models.Model):
    _name = 'salespop.product'
    _description = 'salespop products'

    seller = fields.Many2one('res.partner', ondelete = "cascade")
    onSale = fields.One2many('salespop.product', 'seller')#odoo.fields.Selection
    name = fields.Char()
    description = fields.Char()
    publicationDate = fields.Datetime(readonly=True, default=fields.Datetime.now)
    label = fields.Many2one('salespop.label')
    image = fields.One2many('salespop.photo', 'product')
    price = fields.Integer()
    ubication = fields.Char()
  
    fav = fields.Many2one('res.partner')
    message = fields.One2many('salespop.message', 'product')
   

class category(models.Model):
    _name = 'salespop.category'
    _description = 'salespop categories'

    name = fields.Char()
    product = fields.One2many('salespop.product', 'category')
    image = fields.Image(size_width=200, max_height = 200, required = False)


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


class label(models.Model):
    _name = 'salespop.label'
    _description = 'salespop label'

    name = fields.Char()
    product = fields.One2many('salespop.product', 'label')

class message(models.Model):
    _name = 'salespop.message'
    _description = 'salespop mensaje'

    content = fields.Char()
    product = fields.Many2one('selpop.product', ondelete = "cascade")

class employee(models.Model):
    _name = 'salespop.message'
    _description = 'salespop mensaje'

    name = fields.Char()


class photo(models.Model):
    _name = 'salespop.photo'
    _description = 'salespop photo articulo'

    photo = fields.Image(size_width=200, max_height = 200, required = True)
    product = fields.Many2one('salespop.product', ondelete = "cascade")