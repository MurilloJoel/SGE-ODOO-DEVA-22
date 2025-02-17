from odoo import models, fields

class Category(models.Model):
    _name = 'JMM_kitchen.category'
    _description = 'Product Category'

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    parent_id = fields.Many2one(
        'JMM_kitchen.category', 
        string='Parent Category'
    )
    dish_ids = fields.One2many(
        'JMM_kitchen.dish', 
        'category_id', 
        string='Dishes'
    )
    ingredient_ids = fields.One2many(
        'JMM_kitchen.ingredient', 
        'category_id', 
        string='Ingredients'
    )
    active = fields.Boolean(string='Active', default=True)