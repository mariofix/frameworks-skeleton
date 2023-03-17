from flask_admin import BaseView, expose
from app.admin.mixins import AdminModelView
from app.models import User, Role
from flask_admin.contrib.sqla import ModelView
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin.form import BaseForm
from flask_admin.babel import lazy_gettext as _
from wtforms import fields, validators
from wtforms.widgets import TextArea
from flask_security import hash_password
from flask import current_app


class AppAdmin:
    form_widget_args = {
        "created_at": {
            "readonly": True,
        },
        "modified_at": {
            "readonly": True,
        },
    }
    page_size = 50
    save_as = True
    save_as_continue = True
    can_export = False
    can_view_details = True


class UserAdmin(AppAdmin, AdminModelView):
    name = _("User")
    name_plural = _("Users")
    icon = "fa-solid fa-user"
    form_excluded_columns = [User.password]
    column_list = [User.username, User.email, User.active, "roles"]

    def scaffold_form(self):
        form_class = super(UserAdmin, self).scaffold_form()
        form_class.password2 = fields.PasswordField(_("New Password"))
        return form_class

    def on_model_change(self, form, model, is_created):
        if len(model.password2):
            model.password = hash_password(model.password2)


class RoleAdmin(AppAdmin, AdminModelView):
    name = _("Role")
    name_plural = _("Roles")
    icon = "fa-solid fa-list"
    column_list = [Role.name, Role.description, Role.permissions]
