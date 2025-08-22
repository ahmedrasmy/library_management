from odoo import  api, fields, models


class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'
    _rec_name = 'name'

    name = fields.Char('The title of the book',required=True)
    isbn = fields.Char('ISBN')
    author_ids = fields.Many2many('library.author')
    published_date = fields.Date('Published Date')
    cover_image = fields.Binary(string='Cover Image')
    summary = fields.Text(string='Summary')
    is_available = fields.Boolean(string='Is Available',compute='_compute_is_available')
    rental_ids = fields.One2many('library.rental','book_id',string='Rentals')
    active_rental_count = fields.Integer(string="Active Rentals",compute="_compute_active_rental_count")

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
            'view_mode': 'tree,form',
            'domain': [
                ('book_id', '=', self.id),
                ('state', '=', 'rented')
            ],
            'context': {'default_book_id': self.id}
        }


