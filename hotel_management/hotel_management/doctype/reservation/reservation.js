frappe.ui.form.on('Reservation', {
    refresh: function (frm) {
        if (!frm.doc.arrival_date) {
            frm.set_value('arrival_date', frappe.datetime.nowdate());
        }
		if (!frm.doc.date_ordered) {
			frm.set_value('order_date', frappe.datetime.nowdate());
		}
    },
	customer_name: function (frm) {
		if (frm.doc.customer_name) {
			frm.set_value('invoice_address', frm.doc.customer_name);
        }
    },
	change_address: function(frm) {
        frappe.set_route('Form', "Address" , frm.doc.address_title);
    },
	change_detail: function(frm) {
        frappe.set_route('Form', "Customer", frm.doc.customer_name);
    },
});


frappe.ui.form.on('Reservation', {
	hotel_room(frm) {
		if (frm.doc.hotel_room) {
			frappe.call({
				method: 'hotel_management.hotel_management.doctype.reservation.reservation.get_hotel_room',
				args: {
					doctype: 'Hotel Rooms',
					filter: {
						name: frm.doc.hotel_room
					}
				},
				callback: function (r) {
					if (r.message) {
						console.log("-------------------------", r.message);
						frm.clear_table('reservation_line')
						r.message.items.forEach(function (item) {
							var child = frm.add_child('reservation_line');
                            child.room_number = item.name1 
							child.room_category = item.room_type
							child.status = item.status
							child.capacity = item.capacity
							child.rate = item.rate
						});
						frm.refresh_field('reservation_line')
					}
				}
			});
		}
	}
});


frappe.ui.form.on('Reservation', {
    refresh: function(frm) {
        frm.add_custom_button(__('Send Mail'), function () {
            frappe.call({
                method: "hotel_management.hotel_management.doctype.reservation.reservation.send_mail",
                args: {
                    doc: frm.doc
                },
            });
        });
    }
});


frappe.ui.form.on('Reservation', {  
	refresh: function (frm) {
		// Add Checkout Button
		frm.add_custom_button(__('Checkout'), function () {
			if (!frm.doc.expected_departure) {
				frm.set_value('expected_departure', frappe.datetime.nowdate());
			}
			frm.set_df_property("section_house_keeping", 'hidden', 0);
			frm.set_df_property('section_break_emp', 'hidden', 0);
			frm.set_df_property("rating", 'hidden', 0);
			
			frm.add_custom_button(__('Create Invoice'), function() {
				frappe.call({
					method: 'hotel_management.hotel_management.doctype.reservation.reservation.create_invoice',
					args: {
						'reservation_id': frm.doc.name,
						'customer_name': frm.doc.customer_name,  // Fix here
						'rate': frm.doc.reservation_line[0].rate,  // Fix here
						'capacity': frm.doc.reservation_line[0].capacity,
						'hotel_room': frm.doc.hotel_room
					},
					callback: function(response) {
						frappe.msgprint("Invoice Created Successfully");
						frappe.set_route('Form', 'Sales Invoice', response.message);
					}
				});
			});
						
		});
	},
	department: function (frm) {
		var department = frm.doc.department;

		frm.fields_dict['employee'].grid.get_field('full_name').get_query = function () {
			return {
				filters: {
					'department': department,
					'status': 'Active',
					
				}
			};
		};
		frm.fields_dict['employee'].grid.refresh();
	}
});




