# models/recruitment.py

from odoo import models, fields

class RecruitmentJob(models.Model):
    _name = 'recruitment.job'
    _description = 'Recruitment Job'

    name = fields.Char(string='Job Title', required=True)
    description = fields.Text(string='Description')
    requirements = fields.Text(string='Requirements')
    recruit_id = fields.Many2one('recruitment.recruiteur', string='recruit_id')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed')],
        string='Status', default='draft')

    def start_recruitment(self):
        self.write({'status': 'in_progress'})

    def complete_recruitment(self):
        self.write({'status': 'completed'})

class RecruitmentCandidate(models.Model):
    _name = 'recruitment.candidate'
    _description = 'Recruitment Candidate'

    name = fields.Char(string='Name', required=True)
    job_id = fields.Many2one('recruitment.job', string='Job')
    email = fields.Char(string='Email')
    phone = fields.Char(string='Phone')
    experience = fields.Char(string='Experience')
    resume = fields.Binary(string='Resume')


class Department(models.Model):
    _name = 'recruitment.department'
    _description = 'Department'

    name = fields.Char(string='Name', required=True)
    departmentjob=fields.Many2many('recruitment.job', string='jobdepartment')





