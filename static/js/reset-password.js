            // SCRIPTS FOR PASSWORD RESET //
// ADDS PLACEHOLDER AND CLASSES TO INPUT FOR STYLING//

(() => {
    const emailInput = document.getElementById("id_email");
    const newPassword1 = document.getElementById("id_new_password1");
    const newPassword2 = document.getElementById("id_new_password2");
 
    const setAttributeOfInput = (input, attrName, attrValue) => {

        input.setAttribute(attrName, attrValue); 
    }

    if (emailInput) {

        setAttributeOfInput(emailInput, "class", "reset-form__input" );
        setAttributeOfInput(emailInput, "placeholder", "Email");
    }
    
    if (newPassword1 && newPassword2) {

        setAttributeOfInput(newPassword1, "class", "reset-confirm__password1");
        setAttributeOfInput(newPassword1, "placeholder", "New Password");
        setAttributeOfInput(newPassword2, "class", "reset-confirm__password2");
        setAttributeOfInput(newPassword2, "placeholder", "Confirm Password");
    }


})();