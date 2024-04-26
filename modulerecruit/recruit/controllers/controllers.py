# -*- coding: utf-8 -*-
# from odoo import http


# class Recruit(http.Controller):
#     @http.route('/recruit/recruit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/recruit/recruit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('recruit.listing', {
#             'root': '/recruit/recruit',
#             'objects': http.request.env['recruit.recruit'].search([]),
#         })

#     @http.route('/recruit/recruit/objects/<model("recruit.recruit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('recruit.object', {
#             'object': obj
#         })
