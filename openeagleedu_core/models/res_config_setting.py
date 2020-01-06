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

from eagle import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    module_openeagleedu_activity = fields.Boolean(string="Activity")
    module_openeagleedu_facility = fields.Boolean(string="Facility")
    module_openeagleedu_parent = fields.Boolean(string="Parent")
    module_openeagleedu_assignment = fields.Boolean(string="Assignment")
    module_openeagleedu_classroom = fields.Boolean(string="Classroom")
    module_openeagleedu_fees = fields.Boolean(string="Fees")
    module_openeagleedu_admission = fields.Boolean(string="Admission")
    module_openeagleedu_timetable = fields.Boolean(string="Timetable")
    module_openeagleedu_exam = fields.Boolean(string="Exam")
    module_openeagleedu_library = fields.Boolean(string="Library")
    module_openeagleedu_attendance = fields.Boolean(string="Attendance")
    module_openeagleedu_quiz = fields.Boolean(string="Quiz Enterprise")
    module_openeagleedu_discipline = fields.Boolean(
        string="Discipline Enterprise")
    module_openeagleedu_health_enterprise = fields.Boolean(
        string="Health Enterprise")
    module_openeagleedu_achievement_enterprise = fields.Boolean(
        string="Achievement Enterprise")
    module_openeagleedu_activity_enterprise = fields.Boolean(
        string="Activity Enterprise")
    module_openeagleedu_admission_enterprise = fields.Boolean(
        string="Admission Enterprise")
    module_openeagleedu_alumni_enterprise = fields.Boolean(
        string="Alumni Enterprise")
    module_openeagleedu_assignment_enterprise = fields.Boolean(
        string="Assignment Enterprise")
    module_openeagleedu_attendance_enterprise = fields.Boolean(
        string="Attendance Enterprise")
    module_openeagleedu_bigbluebutton = fields.Boolean(
        string="Bigbluebutton Enterprise")
    module_openeagleedu_campus_enterprise = fields.Boolean(
        string="Campus Enterprise")
    module_openeagleedu_classroom_enterprise = fields.Boolean(
        string="Classroom Enterprise")
    module_openeagleedu_exam_enterprise = fields.Boolean(
        string="Exam Enterprise")
    module_openeagleedu_facility_enterprise = fields.Boolean(
        string="Facility Enterprise")
    module_openeagleedu_fees_enterprise = fields.Boolean(
        string="Fees Enterprise")
    module_openeagleedu_library_barcode = fields.Boolean(
        string="Library Barcode Enterprise")
    module_openeagleedu_library_enterprise = fields.Boolean(
        string="Library Enterprise")
    module_openeagleedu_lms = fields.Boolean(string="LMS Enterprise")
    module_openeagleedu_lms_blog = fields.Boolean(string="LMS Blog Enterprise")
    module_openeagleedu_lms_forum = fields.Boolean(
        string="LMS Forum Enterprise")
    module_openeagleedu_lms_gamification = fields.Boolean(
        string="LMS Gamification Enterprise")
    module_openeagleedu_lms_sale = fields.Boolean(string="LMS Sale Enterprise")
    module_openeagleedu_lms_survey = fields.Boolean(
        string="LMS Survey Enterprise")
    module_openeagleedu_meeting_enterprise = fields.Boolean(
        string="Meeting Enterprise")
    module_openeagleedu_online_admission = fields.Boolean(
        string="Online Admission Enterprise")
    module_openeagleedu_parent_enterprise = fields.Boolean(
        string="Parent Enterprise")
    module_openeagleedu_placement_enterprise = fields.Boolean(
        string="Placement Enterprise")
    module_openeagleedu_scholarship_enterprise = fields.Boolean(
        string="Scholarship Enterprise")
    module_openeagleedu_timetable_enterprise = fields.Boolean(
        string="Timetable Enterprise")
    module_openeagleedu_transportation_enterprise = fields.Boolean(
        string="Transportation Enterprise")
    module_openeagleedu_lesson = fields.Boolean(string="Lesson Enterprise")
