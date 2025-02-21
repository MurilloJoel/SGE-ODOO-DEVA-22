from odoo import models, fields

class Category(models.Model):
    _name = 'jmm_gestion_restaurantes.category'
    _description = 'Product Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    parent_id = fields.Many2one(
        'jmm_gestion_restaurantes.category', 
        string='Parent Category'
    )
    dish_ids = fields.One2many(
        'jmm_gestion_restaurantes.dish', 
        'category_id', 
        string='Dishes'
    )
    ingredient_ids = fields.One2many(
        'jmm_gestion_restaurantes.ingredient', 
        'category_id', 
        string='Ingredients'
    )
    active = fields.Boolean(string='Active', default=True)