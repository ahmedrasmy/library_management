from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _description = 'Library Author'
    _rec_name = 'name'

    name = fields.Char(string='Name',required=True)
    biography = fields.Text(string='Biography')
