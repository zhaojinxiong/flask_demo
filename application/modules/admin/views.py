from . import admin_blue

@admin_blue.route("/admin")
def admin():
    return "welcom admin chuanpu"