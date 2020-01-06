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

{
    'name': 'OpenEagleEdu Classroom',
    'version': '13.0',
    'license': 'LGPL-3',
    'category': 'Education',
    "sequence": 3,
    'summary': 'Manage Classroom',
    'complexity': "easy",
    'author': 'Eagle ERP',
    'website': 'http://www.eagle-erp.com',
    'depends': ['openeagleedu_core', 'openeagleedu_facility', 'product'],
    'data': [
        'security/ir.model.access.csv',
        'views/classroom_view.xml',
        'menus/op_menu.xml',
    ],
    'demo': [
        'demo/classroom_demo.xml',
        'demo/facility_line_demo.xml'
    ],
    'images': [
        'static/description/openeagleedu_classroom_banner.jpg',
    ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
