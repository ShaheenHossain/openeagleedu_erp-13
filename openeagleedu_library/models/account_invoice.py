# -*- coding: utf-8 -*-
###############################################################################
#
#    Eagle ERP
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.eagle-erp.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.
#
#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################


from eagle import models


class AccountInvoice(models.Model):
    _inherit = "account.move"

    def action_invoice_paid(self):
        paid_invoice = super(AccountInvoice, self).action_invoice_paid()
        if self:
            movement = self.env['op.media.movement'].search(
                [('invoice_id', '=', self.id)])
            if movement and movement.invoice_id.state == 'paid':
                movement.state = 'return_done'
        return paid_invoice
