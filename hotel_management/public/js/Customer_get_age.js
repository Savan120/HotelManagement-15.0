frappe.ui.form.on('Customer', {
    custom_dob: function(frm) {
        console.log("FRM:::::::::::::::::::::::::::::::", frm);
        console.log("Dob::::::::::::::::::::::::::::::::::::::", frm.doc.custom_dob);

        let today = new Date();
        let dob = new Date(frm.doc.custom_dob)

        let age = today.getFullYear() - dob.getFullYear();let monthDiff = today.getMonth() - dob.getMonth();
        if (monthDiff < 0 || (monthDiff === 0 && today.getDate() < dob.getDate())) {
            age--;
        }
        frm.set_value("custom_age", age)
    }
});
