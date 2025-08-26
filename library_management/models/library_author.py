from odoo import models, fields, api


class LibraryAuthor(models.Model):
    _name = 'library.author'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Author'
    _rec_name = 'name'

    name = fields.Char(string='Name',required=True, tracking=True)
    biography = fields.Text(string='Biography', tracking=True)
