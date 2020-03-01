# -*- coding: utf-8 -*-

from odoo import models, fields

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # campo nuevo
    price_2 = fields.Monetary(string="Precio 2")


