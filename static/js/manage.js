// JS FOR ALL 3 TEMPLATES MANAGE CLIENT, JOBS AND CYCLES //

(() => {

    const manageClientInput = document.getElementsByClassName('register-form__input');
    const manageDeleteClientsButtons = document.getElementsByClassName('manage-button__button');

    // GET ALL THE DELETE BUTTONS BY CLASS, LOOK FOR BUTTONS WITH DATA-ID ATTR, 
    // TRAVERSE TO DIV TO SHOW/HIDE AND CALL UTILITY addRemoveClassOnClick FUNCTION
    // AND CALL insertHTMLonClick TO ALTER BUTTON DISPLAY
    const showHideDeleteDiv = (buttons, condition, html) => {
        for (let i = 0; i < buttons.length; i++) {

            let deleteButton = buttons[i].getAttribute('data-id')
            
            if (deleteButton == 'manage-delete') {

                let showDeleteDiv = buttons[i].
                                        parentElement.
                                        parentElement.
                                        parentElement.
                                        nextElementSibling;

                addRemoveClassOnClick(buttons[i], 
                                        showDeleteDiv, 
                                        'manage-delete__button--show' );

                addRemoveClassOnClick(buttons[i], 
                                        buttons[i], 
                                        'manage-button__button--delete-click' );
                
                insertHTMLonClick(buttons[i], condition, html);
       
            }

        }

    }
    
    // ADD REQUIRED ATTRIBUTE TO RENDERED INPUT //
    for (let i = 0; i < manageClientInput.length; i++) {

        manageClientInput[i].setAttribute('required','true');
    }

    showHideDeleteDiv(manageDeleteClientsButtons, 'Delete Client', 'Cancel');
    addBgColorToBody('body-color');
    
})();