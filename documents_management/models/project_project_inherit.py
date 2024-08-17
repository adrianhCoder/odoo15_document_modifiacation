from odoo import models, fields, api

class ProjectProject(models.Model):
    _inherit = 'project.project'

    #custom_field = fields.Char(string="Custom Field")
    allowed_users_from_project = fields.Many2many('res.users',string='Acceso permitido a',default=lambda self: self.env.user)

    @api.model
    def create(self, vals):
        # Llamamos al método 'create' original
        record = super(ProjectProject, self).create(vals)
        
        # Preparar y enviar el mensaje de notificación
        message = f"¡El proyecto '{record.name}' ha creado un folder con su mismo nombre y sus respectivas subcarpetas!"
        self.env['bus.bus']._sendone(
            record.env.user.partner_id, 
            'simple_notification', 
            {
                'title': 'Creación de Proyecto',
                'message': message,
                'type': 'success',
            }
        )

        # Crear la carpeta principal
        folder = self.env['documents.folder'].create({'name': record.name})

        # Lista de nombres de subcarpetas
        subfolders = [
            'Red Hidraulica',
            'Planos Energia',
            'Certificados de calidad de ....',
            'Certificados de trabajadores',
            'Pruebas de calidad',
            'Certificados de calidad',
            'Certificados Cliente',
            'Reporte fotografico',
            'Salidas'


        ]

        # Crear las subcarpetas
        for subfolder_name in subfolders:
            self.env['documents.folder'].create({
                'name': subfolder_name,
                'parent_folder_id': folder.id
            })

        return record
