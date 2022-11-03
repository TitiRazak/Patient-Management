# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class PatientList(models.Model):
    _name = 'patient.list'
    _inherit = 'mail.thread'
    _description = 'wolf_training.wolf_training'

    name = fields.Char(compute="_compute_name", store=True)
    firstname = fields.Char()
    lastname = fields.Char()
    age = fields.Integer(string="Age", track_visibility='onchange')
    state = fields.Selection([('new', 'Nouveau'), ('consulted', 'Consutler'),
                              ('canceled', 'Annuler'), ('done', 'Traiter')], default='new')

    @api.depends('firstname', 'lastname')
    def _compute_name(self):
        for record in self:
            record.name = record.firstname + " " + record.lastname

    def set_consulted(self):
        self.state = 'consulted'

    def set_canceled(self):
        self.state = 'canceled'

    def set_new(self):
        self.state = 'new'

    def set_done(self):
        self.state = 'done'

    def calcul_age(self):
        return {
            'name': _('Calcul Age'),
            'view_mode': 'form',
            'res_model': 'age.popup',
            'type': 'ir.actions.act_window',
            'target': 'new',
        }
