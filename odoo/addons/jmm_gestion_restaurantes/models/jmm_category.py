from odoo import models, fields, api, exceptions

class Category(models.Model):
    _name = 'jmm_gestion_restaurantes.category'
    _description = 'Product Category'
    _parent_store = True
    _parent_name = "parent_id"
    
    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string='Description')
    parent_id = fields.Many2one(
        'jmm_gestion_restaurantes.category', 
        string='Parent Category',
        index=True
    )
    parent_path = fields.Char(index=True)
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

    _sql_constraints = [
        ('unique_category_name', 'UNIQUE(name)', '¡El nombre de la categoría debe ser único!'),
        ('check_parent_not_self', 'CHECK (parent_id != id)', '¡Una categoría no puede ser padre de sí misma!')
    ]

    @api.constrains('parent_id')
    def _check_category_recursion(self):
        if not self._check_recursion():
            raise exceptions.ValidationError('¡No puedes crear jerarquías de categorías recursivas!')