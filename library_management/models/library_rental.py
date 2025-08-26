from odoo import models, fields, api
from odoo.exceptions import ValidationError



class LibraryRental(models.Model):
    _name = 'library.rental'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Library Rental'

    book_id = fields.Many2one('library.book', string='Book',required=True, tracking=True)
    borrower_id = fields.Many2one('res.partner', string='Borrower',required=True, tracking=True)
    rental_date = fields.Datetime(string='Rental Date',default=fields.Datetime.now(), tracking=True)
    return_date = fields.Datetime(string='Return Date', tracking=True)
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('rented', 'Rented'),
            ('returned', 'Returned'),
            ('lost', 'Lost'),
        ],default='draft', tracking=True
    )


    def action_draft(self):
        for record in self:
            record.state = 'draft'

    def action_rented(self):
        for record in self:
            record.state = 'rented'

    def action_returned(self):
        for record in self:
            record.state = 'returned'

    def action_lost(self):
        for record in self:
            record.state = 'lost'

    @api.constrains('book_id', 'state', 'return_date')
    def _check_book_availability(self):
        for rental in self:
            if rental.state == 'rented' and not rental.return_date:
                conflict = self.search([
                    ('id', '!=', rental.id),
                    ('book_id', '=', rental.book_id.id),
                    ('state', '=', 'rented'),
                    ('return_date', '=', False),
                ], limit=1)
                if conflict:
                    raise ValidationError(
                        f"The book '{rental.book_id.name}' is already rented and must be returned before renting it again."
                    )

