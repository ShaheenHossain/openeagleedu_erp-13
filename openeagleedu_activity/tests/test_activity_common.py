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

from eagle.tests import common


class TestActivityCommon(common.SavepointCase):
    def setUp(self):
        super(TestActivityCommon, self).setUp()
        self.op_activity_type = self.env['op.activity.type']
        self.op_activity = self.env['op.activity']
        self.op_student_migrate_wizard = self.env['student.migrate']