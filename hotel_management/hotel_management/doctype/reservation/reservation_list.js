// // frappe.listview_settings['Reservation'] = {
// //     onload: function(listview) {
// //         listview.page.add_button(__('Get Report'), function() {
// //             let d = new frappe.ui.Dialog({
// //                 title: 'Reservation Details',
// //                 fields: [
// //                     {
// //                         label: 'From Date',
// //                         fieldname: 'from_date',
// //                         fieldtype: 'Date',
// //                         reqd: 1,
// //                         default: frappe.datetime.now_date()
// //                     },
// //                     {
// //                         label: 'To Date',
// //                         fieldname: 'to_date',
// //                         fieldtype: 'Date',
// //                         reqd: 1
// //                     },
// //                 ],
// //                 primary_action_label: 'Print',
// //                 primary_action(values) {
// //                     frappe.call({
// //                         method: 'hotel_management.hotel_management.doctype.reservation.reservation.get_reservation_report',
// //                         args: {
// //                             from_date: values.from_date,
// //                             to_date: values.to_date,
// //                         },
// //                         callback: function(response) {
// //                             if (response.message) {
// //                                 console.log("Response:::::::::::::::::::::::::::::::::::::::::::::", response.message);                        
// //                                 response.message.forEach(function(reservation_id) {
// //                                     console.log("Reservation_id:::::::::::::::::::::::::::::::::::::::",reservation_id)
// //                                     let pdf_url = '/api/method/frappe.utils.print_format.download_pdf?doctype=Reservation&name=' 
// //                                                 + reservation_id
// //                                                 + '&format=Reservation List&no_letterhead=0';
// //                                     // console.log(">>>>>>>>>>>>>>>>>>>>>>>>>",pdf_url)
// //                                     window.open(pdf_url);
// //                                 });
// //                             }
// //                         }
// //                     });
// //                     d.hide();
// //                 }
// //             });

// //             d.show();
// //         });
// //     }
// // };


// frappe.listview_settings['Reservation'] = {
//     onload: function(listview) {
//         listview.page.add_button(__('Get Report'), function() {
//             let d = new frappe.ui.Dialog({
//                 title: 'Reservation Details',
//                 fields: [
//                     {
//                         label: 'From Date',
//                         fieldname: 'from_date',
//                         fieldtype: 'Date',
//                         reqd: 1,
//                         default: frappe.datetime.now_date()
//                     },
//                     {
//                         label: 'To Date',
//                         fieldname: 'to_date',
//                         fieldtype: 'Date',
//                         reqd: 1
//                     }
//                 ],
//                 primary_action_label: 'Print',
//                 primary_action(values) {
//                     frappe.call({
//                         method: 'hotel_management.hotel_management.doctype.reservation.reservation.download_combined_pdf',
//                         args: {
//                             from_date: values.from_date,
//                             to_date: values.to_date
//                         },
//                         callback: function(pdf_response) {
//                             console.log("PDF Report Response::::::::::::::::::::::::::::::::", pdf_response);
//                             if (pdf_response.message) {
//                                 console.log("PDF_RESPONSE::::::::::::::::::::::::::::::::::",pdf_response)
//                                 let pdf_url = pdf_response.message;
//                                 window.open(pdf_url, '_blank');
//                             } else {
//                                 frappe.msgprint(__('No PDF was generated.'));
//                             }
//                         },
//                         error: function(error) {
//                             console.error("Error generating PDF:", error);
//                             frappe.msgprint(__('An error occurred while generating the PDF.'));
//                         }
//                     });
//                     d.hide();
//                 }
//             });

//             d.show();
//         });
//     }
// };


// // frappe.listview_settings['Reservation'] = {
// //     onload: function(listview) {
// //         listview.page.add_button(__('Get Report'), function() {
// //             let d = new frappe.ui.Dialog({
// //                 title: 'Reservation Details',
// //                 fields: [
// //                     {
// //                         label: 'From Date',
// //                         fieldname: 'from_date',
// //                         fieldtype: 'Date',
// //                         reqd: 1,
// //                         default: frappe.datetime.now_date()
// //                     },
// //                     {
// //                         label: 'To Date',
// //                         fieldname: 'to_date',
// //                         fieldtype: 'Date',
// //                         reqd: 1
// //                     },
// //                 ],
// //                 primary_action_label: 'Print',
// //                 primary_action(values) {
// //                     frappe.call({
// //                         method: 'hotel_management.hotel_management.doctype.reservation.reservation.get_reservation_report',
// //                         args: {
// //                             from_date: values.from_date,
// //                             to_date: values.to_date,
// //                         },
// //                         callback: function(response) {
// //                             if (response.message && response.message.length > 0) {
// //                                 // Log reservation names for debugging
// //                                 console.log("Reservation Names for PDF:", response.message);
// //                                 // const reservation_names = response.message.join(',');
// //                                 let pdf_url = '/api/method/frappe.utils.print_format.download_pdf?doctype=Reservation&name=' + reservation_names + '&format=Reservation List&no_letterhead=0';
// //                                 window.open(pdf_url);
// //                             } else {
// //                                 frappe.msgprint(__('No reservations found for the selected date range.'));
// //                             }
// //                         }
// //                     });
// //                     d.hide();
// //                 }
// //             });

// //             d.show();
// //         });
// //     }
// // };
