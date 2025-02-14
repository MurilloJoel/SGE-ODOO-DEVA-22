# -*- coding: utf-8 -*-

from odoo import models,fields

class libro(models.Model):
    # Estos atributos vienen heredados de la clase madre models.Model
    # El valor _name condiciona el nombre de la tabla y es interno de Odoo
    # conviene siempre que usemos como prefijo el nombre técnico de nuestro módulo seguido de un punto
    # Debemos usar siempre minúsculas
    _name = 'libreria.libro'
    # El valor _description es un texto legible en algunas partes de la aplicación
    # por ejemplo desde Ajustes > Técnico > Modelo
    _descrition = 'Libro'

    # Conviene que siempre tengamos un atributo llamado literalmente name
    # Usar atajo oofchar para generar fragmento de código
    name = fields.Char(string = 'Titulo', required = True, help = 'Introduce el titulo del libro')
    # Usar atajo ooffloat para generar fragmento de código
    precio = fields.Float(string = 'Precio', help = 'Introduce el precio')
     # Usar atajo oofinteger para generar fragmento de código
    ejemplares = fields.Integer(string = 'Ejemplares', help = ' Introduce el numero de ejemplares')
    # Usar atajo oofdate para generar fragmento de código
    fecha_compra = fields.Date(string = 'Fecha compra', help = 'Introduce fecha compra')
    # Usar atajo oofboolean para generar fragmento de código
    segmano = fields.Boolean(string = 'segunda mano', help = 'Marca si es de segunda mano')
    # Usar atajo oofselection para generar fragmento de código
    estado = fields.Selection([
        ('0', 'Bueno'),
        ('1', 'Regula'),
        ('2', 'Malo')
    ], string = 'Estado', default = 0)

    categoria_id = fields.Many2one('libreria.categoria', string='Categoría')