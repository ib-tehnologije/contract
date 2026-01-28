# Copyright 2026 IB Tehnologije d.o.o.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import models


class AccountMove(models.Model):
    _inherit = "account.move"

    def button_cancel(self):
        contract_lines = self.line_ids.contract_line_id
        res = super().button_cancel()
        if contract_lines:
            contract_lines._recompute_dates_from_invoices()
        return res

    def unlink(self):
        contract_lines = self.line_ids.contract_line_id
        res = super().unlink()
        if contract_lines:
            contract_lines._recompute_dates_from_invoices()
        return res
