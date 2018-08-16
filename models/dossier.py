# -*- coding: utf-8 -*-
import logging

from odoo import _, fields, api
from odoo.exceptions import ValidationError
from odoo.addons.base_geoengine import geo_model
from odoo.addons.base_geoengine import fields as geo_fields

_logger = logging.getLogger(__name__)

class Dossier(geo_model.GeoModel):
    _name = 'irl.dossier'

    ADPNID = fields.Integer(string="Adpnid")
    geometry = geo_fields.GeoMultiPoint(required=True, srid=31370, gist_index=True)
    DETYPED = fields.Integer(string="Detyped")
    PROCEDURE = fields.Text(string="Procedure")
    N_DOSSIER = fields.Integer(string="Num. Dossier")
    GESTIONNAIRE = fields.Char(string="Gestionnaire")
    DATE_PREMIERE_DECISION = fields.Date(string="Date de première décision")
    PREMIERE_DECISION = fields.Text(string="Première decision")
    DATE_DERNIERE_DECISION = fields.Date(string="Date de dernière decision")
    DERNIERE_DECISION = fields.Text(string="Dernière décision")
    RUE = fields.Text(string="Rue")
    N_DE_POLICE_DEBUT = fields.Char(string="Num. Police début")
    N_DE_POLICE_FIN = fields.Char(string="Num. Police fin")
    BOITE = fields.Char(string="Boite")
    ETAGE = fields.Char(string="Etage")
    SITUATION_EXACTE = fields.Text(string="Situation exacte")
    COMMUNE = fields.Char(string="Commune")
    CODE_POSTAL = fields.Char(string="Code postal")
    TYPE_DECISION = fields.Integer(string="Type décision")
    INTERDICTION_ACTUELLE = fields.Char(string="Interdiction actuelle")
