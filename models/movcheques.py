from odoo import fields, models, api


class ModelName(models.Model):
    _name = 'movcheques'
    _description = 'Contiene todos los cheques que se utilizarán en la organización'

    nro_orden = fields.Interger()
    banco = fields.Many2one('res.bank')
    domicilio_pago = fields.Char()
    cta_cte = fields.Char()
    librador = fields.Many2one('res.partner')
    monto = fields.Float(Digits = (9,2),string = 'Monto ',required= True)
