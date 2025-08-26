from odoo import  api, fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Book'
    _rec_name = 'name'

    name = fields.Char('The title of the book',required=True, tracking=True)
    isbn = fields.Char('ISBN', tracking=True)
    author_ids = fields.Many2many('library.author', tracking=True)
    published_date = fields.Date('Published Date', tracking=True)
    cover_image = fields.Binary(string='Cover Image', tracking=True)
    summary = fields.Text(string='Summary', tracking=True)
    is_available = fields.Boolean(string='Is Available',compute='_compute_is_available', tracking=True)
    rental_ids = fields.One2many('library.rental','book_id',string='Rentals', tracking=True)
    active_rental_count = fields.Integer(string="Active Rentals",compute="_compute_active_rental_count", tracking=True)

    @api.depends('rental_ids.state')
    def _compute_is_available(self):
        for book in self:
            rented = any(rental.state == 'rented' for rental in book.rental_ids)
            book.is_available = not rented


    @api.depends('rental_ids.state')
    def _compute_active_rental_count(self):
        for book in self:
            book.active_rental_count = sum(
                1 for rental in book.rental_ids if rental.state == 'rented'
            )

    def action_view_active_rentals(self):
        self.ensure_one()
        return {
            'name': 'Active Rentals',
            'type': 'ir.actions.act_window',
            'res_model': 'library.rental',
            'view_mode': 'list,form',
            'domain': [
                ('book_id', '=', self.id),
                ('state', '=', 'rented')
            ],
            'context': {'default_book_id': self.id}
        }


