# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2014- Vertel AB (<http://vertel.se>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
# ~ from odoo.modules.registry import RegistryManager
from dateutil.relativedelta import relativedelta
from odoo.modules.registry import Registry
from odoo.exceptions import except_orm, Warning, RedirectWarning
from odoo import models, fields, api, _
from odoo import http
from odoo.http import request
from odoo import tools
import random

import logging
_logger = logging.getLogger(__name__)

from odoo.tools import DEFAULT_SERVER_DATE_FORMAT, DEFAULT_SERVER_DATETIME_FORMAT
import datetime

import odoo.addons.decimal_precision as dp

class hr_employee(models.Model):
    _inherit = 'hr.employee'

    should_time_report = fields.Boolean('Should Time Report', default=False)

    def create_time_sheet_for_current_week_all_employes(self):
        self.env['hr.employee'].search([]).create_time_sheet_for_current_week()

    def create_time_sheet_for_current_week(self):
        for record in self:
            today = datetime.date.today()
            week_number_from_start_date = 0
            while week_number_from_start_date < 1:
                current_weeks_monday = today + datetime.timedelta(days=-today.weekday(), weeks=week_number_from_start_date)
                current_weeks_friday = today + datetime.timedelta(days=-today.weekday() + 6, weeks=week_number_from_start_date)
                iter_month = current_weeks_monday.month
                        
                # ~ if current_month != iter_month:
                    # ~ break
                    
                rec = record.env['hr_timesheet.sheet'].search([('employee_id', '=', record.id), ('date_start', '=', current_weeks_monday), ('date_end','=',current_weeks_friday)])
                
                if not rec:
                    try:
                        record.env['hr_timesheet.sheet'].create(
                        {
                        'employee_id':record.id,
                        'date_start':current_weeks_monday,
                        'date_end':current_weeks_friday
                        })
                    except Exception as e:
                        _logger.warning(e)

                week_number_from_start_date+=1
