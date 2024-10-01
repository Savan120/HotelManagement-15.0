import frappe


def send_reminder_email():
    
    frappe.sendmail(
    recipients=["y.chavda@serpentcs.com"],
    subject="Test Email",
    message="This is a test email."
    )

    frappe.log_error(">>>>>>>>>>>>>>>>>>>>>>>>>>Email sent successfully", "Email Log")

