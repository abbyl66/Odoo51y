# -*- coding: utf-8 -*-

from odoo import models, fields, api


class modelo51y(models.Model):
     _name = 'odoo51y.modelo51y'
     _description = 'model modelo51y'

     name = fields.Char('ID', required=True)
     titulo = fields.Char(String = 'titulo', required = True)
     autor = fields.Char(String = 'autor', required=True)
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
