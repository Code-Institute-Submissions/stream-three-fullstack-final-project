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



    //-------------------------------------------------//
    
    const selectOneMonth = document.getElementById('id_start_date_month');
    const selectOneDay = document.getElementById('id_start_date_day');
    const selectOneYear = document.getElementById('id_start_date_year');
    const selectTwoMonth = document.getElementById('id_end_date_month');
    const selectTwoDay = document.getElementById('id_end_date_day');
    const selectTwoYear = document.getElementById('id_end_date_year');
    const cyclesFormSelect = document.getElementById('id_jobs');
    const selectArray = [];

    // POPULATE ARRAY WITH ELEMENTS, COULD NOT GET ELEMENTS BY TAG AS IT //
    // WOULD PULL IN AN UNWANTED SELECTS //
    selectArray.push(selectOneMonth, selectOneDay, selectOneYear,
                    selectTwoMonth, selectTwoDay, selectTwoYear);


    // WRAPS DATE SELECTS IN A DIV AND GIVE DIV A CLASS FOR STYLING //
    const wrapSelectsWithDiv = (selects) => {

        for (let i = 0; i < selects.length; i++) {

            let parent = selects[i].parentElement;
            parent.insertAdjacentHTML('beforeend', '<div></div>');
            parent.lastChild.appendChild(selects[i]);
            addStylesToSelectParent(selects[i],'manage-cycles-form__date-select');
            
                                               

        }
    }

    //------------------- FUNCTION CALLS ------------------------------//

    showHideDeleteDiv(manageDeleteItemButtons);
    addBgColorToBody('body-color');

    // JOBS VIEW SPECIFIC //
    if (jobsFormSelect) {

        addClassToElement(jobsFormSelect, 'profile__select');
        addStylesToSelectParent(jobsFormSelect, 'profile-filter-styled');
    }

    // CYCLES VIEW SPECIFIC //

    if (selectOneMonth) {

        wrapSelectsWithDiv(selectArray);
        addClassToElement(cyclesFormSelect, 'profile__select');
        addStylesToSelectParent(cyclesFormSelect, 'profile-filter-styled');
        
    }
    
    addClassToCollection(jobsFormInput, 'register-form__input');
    
    
})();