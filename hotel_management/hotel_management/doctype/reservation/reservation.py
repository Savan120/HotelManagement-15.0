# Copyright (c) 2024, Savan and contributors
# For license information, please see license.txt

import frappe
import base64
from frappe import _
import json
from frappe.model.document import Document
from datetime import datetime, date
from dateutil.relativedelta import relativedelta
from frappe import get_all
import frappe.utils
from frappe.utils.print_format import download_pdf
from frappe.utils.pdf import get_pdf
import frappe.utils.print_format
from PyPDF2 import PdfMerger
import io


class Reservation(Document):
    pass
    
    
@frappe.whitelist()
def update_room_status_on_reservation(doc, method):
    print("Triggered for document::::::::::::::::::", doc, "with method:::::::::::::::::::::::::::::", method)
    
    if method == "on_submit":
        if doc.hotel_room:
            room = frappe.get_doc("Hotel Rooms", doc.hotel_room)
            print("Current room status before update:", room.status)
            if room.status == 'Available':
                room.status = 'Reserved'
                room.save()
                print("Room status updated to::::::::::::::::::::::::::::", room.status)
            else:
                print(f"The room {room.name} is not available for reservation.")
    elif method == "Checkout":
        if doc.hotel_room:
            room = frappe.get_doc("Hotel Rooms", doc.hotel_room)
            room.status = 'Available'
            room.save()
            print("Room status reverted to:", room.status)

# @frappe.whitelist()
# def update_room_status_on_reservation(doc, method):
#     # Fetch the document using the name
#     docs = frappe.get_doc("Reservation:::::::::::::::::::::::::::::::::", doc)
    
#     if method == "on_submit":
#         if doc.hotel_room:
#             room = frappe.get_doc("Hotel Rooms", doc.hotel_room)
#             frappe.logger().info("Current room status before update: {}".format(room.status))
#             if room.status == 'Available':
#                 room.status = 'Reserved'
#                 room.save()
#                 frappe.logger().info("Room status updated to: {}".format(room.status))
#             else:
#                 frappe.logger().info("The room {} is not available for reservation.".format(room.name))
#     elif method == "Checkout":
#         if doc.hotel_room:
#             room = frappe.get_doc("Hotel Rooms", doc.hotel_room)
#             room.status = 'Available'
#             room.save()
#             frappe.logger().info("Room status reverted to: {}".format(room.status))



@frappe.whitelist()
def send_mail(doc):
    filter_dict = json.loads(doc)
    email_address = filter_dict.get('email')

    # print ("\n doc :::::::::", doc, filter_dict)
    
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
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>",filter)
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
    # print(">response::::::::::::::::::::::::::::::::::",response)

    return response


@frappe.whitelist()
def create_invoice(reservation_id, customer_name, rate, capacity, hotel_room):
    # Fetch the default company name
    # print("Reservation Id::::::::::::::::::::::::::::",reservation_id)
    # print("Guest Name::::::::::::::::::::::::::::::::::::",customer_name)
    # print("Room_rate::::::::::::::::::::::::::::::",rate)
    # print("Capacity::::::::::::::::::::::::::::::::::::",capacity)
    # print("Hotel Room:::::::::::::::::::::::::::::::::::;",hotel_room)
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


# @frappe.whitelist()
# def get_reservation_report(from_date, to_date):
#     print("From Date>>>>>>>>>>>>>>>>>>",from_date,"To date:::::::::::::::::::::::::::::::::::::::", to_date)
#     reservations = get_all('Reservation', filters=[
#         ['arrival_date', '>=', from_date],
#         ['expected_depature', '<=', to_date]
#     ])
#     print("Reservation::::::::::::::::::::::::::::::::::::::::::::::::::::",reservations)
    
#     if reservations:
#         reservation_names = [reservation.name for reservation in reservations]
#         print("Reservation in for loop::::::::::::::::::::::::::::::::::::::::::::;;",reservation_names)
#         return reservation_names
#     else:
#         frappe.throw("No reservations found in the specified date range.")



# @frappe.whitelist()
# def get_reservation_report(from_date, to_date):
#     print("From Date::::::::::::::::::", from_date, "To Date::::::::::::::::::::::::::", to_date)
    
#     reservations = frappe.get_all('Reservation', filters=[
#         ['arrival_date', '>=', from_date],
#         ['expected_depature', '<=', to_date]
#     ])
    
#     print("Reservations Found:::::::::::::::::::::::::::::::::::::", reservations)
    
#     if reservations:
#         return reservations[0].name
#     else:
#         frappe.throw(_("No reservations found in the specified date range."))


# @frappe.whitelist()
# def download_combined_pdf(from_date, to_date):
#     # Fetch reservation records within the given date range
#     reservation_records = get_all('Reservation', filters=[
#         ['arrival_date', '>=', from_date],
#         ['expected_depature', '<=', to_date]
#     ])
    
#     print("Reservation records:", reservation_records)

#     if not reservation_records:
#         frappe.throw("No reservations found for the selected date range.")

#     pdf_merger = PdfMerger()

#     # Loop through each reservation record and fetch its PDF
#     for reservation in reservation_records:
#         reservation_name = reservation.name
#         print("Processing reservation ID:", reservation_name)  # Extract the reservation ID
#         try:
#             # Fetch the PDF for the reservation as Base64
#             pdf_content = download_pdf(
#                 doctype="Reservation", 
#                 name=reservation_name,  # Pass a single reservation name
#                 format="Reservation List", 
#                 no_letterhead=0
#             )

#             # Check if pdf_content is None or empty
#             if not pdf_content:
#                 frappe.throw(f"No PDF content returned for Reservation ID {reservation_name}.")

#             print("PDF content for {}: {}".format(reservation_name, pdf_content))

#             # Decode the Base64 content
#             decoded_pdf_content = base64.b64decode(pdf_content)
            
#             # Append the decoded PDF content to the merger
#             pdf_merger.append(io.BytesIO(decoded_pdf_content))

#         except Exception as e:
#             frappe.throw(f"Failed to download PDF for Reservation ID {reservation_name}: {str(e)}")

#     # Save the combined PDF
#     combined_pdf_path = "/tmp/combined_reservations.pdf"
#     with open(combined_pdf_path, "wb") as output_pdf:
#         pdf_merger.write(output_pdf)


#     return combined_pdf_path
