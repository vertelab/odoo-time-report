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
{
    'name': 'Time Report Automation',
    'summary': "Automates time report generation.",
    'category': 'Payroll',
    'author': 'Vertel AB',
    'depends': ['hr_timesheet','hr_timesheet_sheet'],
    'version': '18.0.1.0.0',
    'license': 'AGPL-3',
    'description': '''
Time Report Automation
======================

    Adds a cron job that creates time sheets for all employees that have the field shoud_time_report set to true.

    Features:

        - Automation: Scheduled jobs: Create time sheets for company.
        - UI Integration: Extends 2 view(s) in the Odoo interface.
        - Extends Odoo: Builds on hr.employee, hr.employee.public.
    ''',

    'auto_install': False,
    'website': 'https://vertel.se/apps/odoo-time-report/time_report_automation',
    'data':[
        'data/create_time_report.xml',
        'views/hr_employee.xml',
    ],
    'installable': True
}
