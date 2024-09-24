# Copyright (c) 2024, Savan and contributors
# For license information, please see license.txt

import frappe
import json
from frappe.model.document import Document


class Reservation(Document):
    pass

    # def send_reminders():
    #     # Custom logic for sending reminders
    #     frappe.logger().info("Reminder: Sending reminders every few minutes...")
    #     # Add your reminder logic here, such as sending emails or notifications
    #     recipients = frappe.get_all("User", filters={"enabled": 1}, fields=["email"])
        
    #     for recipient in recipients:
    #         frappe.sendmail(
    #             recipients=[recipient.email],
    #             subject="Reminder",
    #             message="This is a reminder sent every few minutes."
    #         )
    #     frappe.logger().info("Reminders sent successfully.")

@frappe.whitelist()
def send_mail(doc):
    filter_dict = json.loads(doc)
    email_address = filter_dict.get('email')

    print ("\n doc :::::::::", doc, filter_dict)
    
    if email_address:
        pdf = frappe.attach_print(
            filter_dict.get('doctype'),
            filter_dict.get('name'),
        )
        subject = f"Reservation:{filter_dict.get('name')}"
        message = f"Dear {filter_dict.get('customer_name')}, We are pleased to inform you that your reservation has been successfully confirmed."

        frappe.sendmail(
            recipients=[email_address],
            subject=subject,
            message=message,
            attachments=[pdf]
        )
        frappe.msgprint("Mail sent successfully with PDF attachment.")
    else:
        frappe.msgprint("No recipient email found.")

            
@frappe.whitelist()
def get_hotel_room(doctype, filter):
    print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",filter)
    """
    Get hotel room details based on the provided filter.
    Args:
        doctype (str): The doctype to query.
        filter (str): JSON string containing filter conditions.

    Returns:
        dict: A dictionary containing hotel room details.
    """
    # Convert filter_str from JSON string to dictionary
    filter_dict = json.loads(filter)
    
    # Get the hotel room based on the name
    hotel_room_name = filter_dict['name']
    hotel_room = frappe.get_doc(doctype, hotel_room_name)
    response = {
        "items": []
    }
    
    response["items"].append({
        'name1':hotel_room.room_number,
        "room_category": hotel_room.room_type,
        "status": hotel_room.status,
        "rate": hotel_room.rate,
        "capacity": hotel_room.capacity
    })
    print(">response::::::::::::::::::::::::::::::::::",response)

    return response


@frappe.whitelist()
def create_invoice(reservation_id, customer_name, rate, capacity, hotel_room):
    # Fetch the default company name
    print("Reservation Id::::::::::::::::::::::::::::",reservation_id)
    print("Guest Name::::::::::::::::::::::::::::::::::::",customer_name)
    print("Room_rate::::::::::::::::::::::::::::::",rate)
    print("Capacity::::::::::::::::::::::::::::::::::::",capacity)
    print("Hotel Room:::::::::::::::::::::::::::::::::::;",hotel_room)
    default_company = frappe.defaults.get_user_default('Company')
    
    existing_invoice = frappe.db.exists('Sales Invoice', {
        'customer': customer_name,
        'reservation_id':reservation_id,
        'docstatus': 1
    })

    
    if existing_invoice:
        frappe.throw(f"An invoice already exists for the customer {customer_name} and series {reservation_id}")
        
    # Fetch the default income account for that company
    default_income_account = frappe.db.get_value('Company', default_company, 'default_income_account')
    
    if not default_income_account:
        frappe.throw(f"Please configure a default income account for the company {default_company}.")
    
    # Create the Sales Invoice
    invoice = frappe.get_doc({
        'doctype': 'Sales Invoice', 
        'customer': customer_name,
        'reservation_id':reservation_id,
        'company': default_company, 
        'due_date': frappe.utils.nowdate(),
        'items': [{
            'item_name': hotel_room,
            'description': f'Room: {hotel_room} for {capacity} people',
            'rate': rate,
            'qty': 1,
            'income_account': default_income_account,
        }]
    })
    invoice.insert()
    # invoice.submit()
    return invoice.name


