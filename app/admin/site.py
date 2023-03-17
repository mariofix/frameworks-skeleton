from flask import url_for, redirect, request
from flask_admin import Admin
from flask_admin.consts import ICON_TYPE_FONT_AWESOME
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import SecureForm
from app.models import User, Role
from app.database import db
from app.admin.views import UserAdmin, RoleAdmin
from flask_babel import lazy_gettext as _

admin_site = Admin(
    name="Flask Admin",
    template_mode="bootstrap4",
    url="/admin.site",
)


admin_site.add_view(
    UserAdmin(
        User,
        db.session,
        category=_("System"),
        menu_icon_type=ICON_TYPE_FONT_AWESOME,
        menu_icon_value="fa-solid fa-user",
    )
)
admin_site.add_view(
    RoleAdmin(
        Role,
        db.session,
        category=_("System"),
        menu_icon_type=ICON_TYPE_FONT_AWESOME,
        menu_icon_value="fa-solid fa-list",
    )
)
