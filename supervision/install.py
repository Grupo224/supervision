import frappe

ROLES = [
    "Coordinador de Supervisión",
    "Supervisor Estatal",
    "Supervisor Federal",
    "Consulta Supervisión",
]

def after_install():
    for role in ROLES:
        if not frappe.db.exists("Role", role):
            frappe.get_doc({"doctype": "Role", "role_name": role}).insert(ignore_permissions=True)
    frappe.db.commit()

def after_migrate():
    after_install()
