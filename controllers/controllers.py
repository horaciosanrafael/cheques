# -*- coding: utf-8 -*-
# from odoo import http


# class /home/horacio/odoo1303/misapps/cheques(http.Controller):
#     @http.route('//home/horacio/odoo1303/misapps/cheques//home/horacio/odoo1303/misapps/cheques/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//home/horacio/odoo1303/misapps/cheques//home/horacio/odoo1303/misapps/cheques/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/home/horacio/odoo1303/misapps/cheques.listing', {
#             'root': '//home/horacio/odoo1303/misapps/cheques//home/horacio/odoo1303/misapps/cheques',
#             'objects': http.request.env['/home/horacio/odoo1303/misapps/cheques./home/horacio/odoo1303/misapps/cheques'].search([]),
#         })

#     @http.route('//home/horacio/odoo1303/misapps/cheques//home/horacio/odoo1303/misapps/cheques/objects/<model("/home/horacio/odoo1303/misapps/cheques./home/horacio/odoo1303/misapps/cheques"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/home/horacio/odoo1303/misapps/cheques.object', {
#             'object': obj
#         })
