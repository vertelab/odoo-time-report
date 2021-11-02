# -*- coding: utf-8 -*-
##############################################################################
#
#    Odoo, Open Source Enterprise Management Solution, third party addon
#    Copyright (C) 2021- Vertel AB (<http://vertel.se>).
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
from dateutil.relativedelta import relativedelta
from odoo.modules.registry import Registry
from odoo import models, fields, api, _
import datetime
import logging
_logger = logging.getLogger(__name__)



class hr_employee(models.Model):
    _inherit = 'hr.employee'

    should_time_report = fields.Boolean('Should Time Report', default=False)

    def create_time_sheet_for_current_week_all_employes(self, number_of_weeks = 1):
        self.env['hr.employee'].search([]).create_time_sheet_for_current_week(number_of_weeks)

    def create_time_sheet_for_current_week(self, number_of_weeks = 1):
        for record in self:
            #Skip if the employee doesn't have a res.user or if should_time_report is false
            if not record.should_time_report or not record.user_id:
                continue
            today = datetime.date.today()
            number_of_weeks_iteration = 0
            while number_of_weeks_iteration < number_of_weeks:
                current_weeks_monday = today + datetime.timedelta(days=-today.weekday(), weeks=number_of_weeks_iteration)
                current_weeks_friday = today + datetime.timedelta(days=-today.weekday() + 6, weeks=number_of_weeks_iteration)
               
               #Can be used to limit the running until the end of the current month
                #iter_month = current_weeks_monday.month
                # ~ if current_month != iter_month:
                    # ~ break
                    
                rec = record.env['hr_timesheet.sheet'].search([('employee_id', '=', record.id), ('date_start', '=', current_weeks_monday), ('date_end','=',current_weeks_friday)])
                if not rec:
                    record.env['hr_timesheet.sheet'].create(
                    {
                    'employee_id':record.id,
                    'date_start':current_weeks_monday,
                    'date_end':current_weeks_friday
                    })
 

                number_of_weeks_iteration+=1
