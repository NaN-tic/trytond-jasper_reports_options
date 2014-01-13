#This file is part jasper_reports_options module for Tryton.
#The COPYRIGHT file at the top level of this repository contains
#the full copyright notices and license terms.
from trytond.model import fields
from trytond.pool import PoolMeta

__all__ = ['Company']
__metaclass__ = PoolMeta


class Company:
    __name__ = 'company.company'
    invoice_qty = fields.Boolean('Invoice Qty', help='Show qty without decimals')
    sale_qty = fields.Boolean('Sale Qty', help='Show qty without decimals')
    shipment_qty = fields.Boolean('Shipment Qty', help='Show qty without decimals')
