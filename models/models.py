# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class /home/horacio/odoo1303/misapps/cheques(models.Model):
#     _name = '/home/horacio/odoo1303/misapps/cheques./home/horacio/odoo1303/misapps/cheques'
#     _description = '/home/horacio/odoo1303/misapps/cheques./home/horacio/odoo1303/misapps/cheques'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
