// JS FOR ALL 3 TEMPLATES MANAGE CLIENT, JOBS AND CYCLES //

(() => {

    const manageClientInput = document.getElementsByClassName('register-form__input');
    const jobsFormInput = document.getElementsByTagName('input');
    const manageDeleteItemButtons = document.getElementsByClassName('manage-delete');
    const jobsFormSelect = document.getElementById('id_client');

    // GET ALL THE DELETE BUTTONS BY CLASS, LOOK FOR BUTTONS WITH DATA-ID ATTR, 
    // TRAVERSE TO DIV TO SHOW/HIDE AND CALL UTILITY addRemoveClassOnClick FUNCTION
    // AND CALL insertHTMLonClick TO ALTER BUTTON DISPLAY
    const showHideDeleteDiv = (buttons) => {
        for (let i = 0; i < buttons.length; i++) {

            let deleteButtonDataId = buttons[i].getAttribute('data-id');
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
            
            if (deleteButtonDataId == 'Delete Job') {
                
                insertCancelOnClick(buttons[i], deleteButtonDataId);
       
            } else if (deleteButtonDataId == 'Delete Client')

                insertCancelOnClick(buttons[i], deleteButtonDataId);

            else if (deleteButtonDataId == 'Delete Cycle')

                insertCancelOnClick(buttons[i], deleteButtonDataId);

        }

    }
    
    // ADD REQUIRED ATTRIBUTE TO RENDERED INPUT //
    for (let i = 0; i < manageClientInput.length; i++) {

        manageClientInput[i].setAttribute('required','true');
    }


    showHideDeleteDiv(manageDeleteItemButtons);
    addBgColorToBody('body-color');

    // JOBS VIEW SPECIFIC //
    addClassToElement(jobsFormSelect, 'profile__select');
    addClassToCollection(jobsFormInput, 'register-form__input');
    addStylesToFormSelect(jobsFormSelect, 'profile-filter-styled');
    
})();