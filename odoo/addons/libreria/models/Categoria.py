# -*- coding: utf-8 -*-

from odoo import models, fields

class Categoria(models.model):
    _name = 'libreria.categoria'
    _description = 'Categoría'
    
    name = fields.Char(string='Nombre',required=True,help='Introduce el nombre de la categoria')
    description = fields.Text(string='Descripcion',help='Introduce una descripcion')