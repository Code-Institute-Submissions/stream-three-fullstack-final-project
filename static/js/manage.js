// JS FOR ALL 3 TEMPLATES MANAGE CLIENT, JOBS AND CYCLES //

(() => {
    // COMMON TO CLIENTS, JOBS AND CYCLES TEMPLATES //
    const manageDeleteItemButtons = document.getElementsByClassName('manage-delete');

    // SPECIFIC TO CLIENT TEMPLATE //
    const manageClientInput = document.getElementsByClassName('register-form__input');
    
    // SPECFIC TO JOB TEMPLATE //
    const jobsFormSelect = document.getElementById('id_client');
    const jobsFormInput = document.getElementsByTagName('input');

    // SPECIFIC TO CYCLES TEMPLATE //
    const selectOneMonth = document.getElementById('id_start_date_month');
    const selectOneDay = document.getElementById('id_start_date_day');
    const selectOneYear = document.getElementById('id_start_date_year');
    const selectTwoMonth = document.getElementById('id_end_date_month');
    const selectTwoDay = document.getElementById('id_end_date_day');
    const selectTwoYear = document.getElementById('id_end_date_year');
    const cyclesFormSelect = document.getElementById('id_jobs');
    const selectArray = [];

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
    
    // WRAPS DATE SELECTS IN A DIV AND ADD STYLES //
    const wrapSelectsWithDiv = (selects) => {

        for (let i = 0; i < selects.length; i++) {

            let parent = selects[i].parentElement;
            parent.insertAdjacentHTML('beforeend', '<div></div>');
            parent.lastChild.appendChild(selects[i]);
            addStylesToSelectParent(selects[i],'manage-cycles-form__date-select');
            addIconToSelect(selects[i],'manage-cycles-form__icon');                                      

        }
    }

    //------------------- FUNCTION CALLS ------------------------------//

    // COMMON TO CLIENTS, JOBS AND CYCLES TEMPLATES //
    showHideDeleteDiv(manageDeleteItemButtons);
    addBgColorToBody('body-color');

    // CLIENTS TEMPLATE SPECIFIC //

    if (manageClientInput) {

        addRequiredAttribute(manageClientInput);
    }


    // JOBS TEMPLATE SPECIFIC //
    if (jobsFormSelect) {

        addClassToElement(jobsFormSelect, 'profile__select');
        addStylesToSelectParent(jobsFormSelect, 'profile-filter-styled');
        addIconToSelect(jobsFormSelect, 'profile-filter-arrow');
        addClassToCollection(jobsFormInput, 'register-form__input');
    }

    // CYCLES TEMPLATE SPECIFIC //

    // RESTRUCTURE DOM SELECT DATES LAYOUT //
    if (selectOneMonth) {

        const startDateSelectContainer = selectOneMonth.parentElement;
        const endDateSelectContainer = selectTwoMonth.parentElement;

    // POPULATE ARRAY WITH ELEMENTS, COULD NOT GET ELEMENTS BY TAG OR CLASS AS IT //
    // WOULD PULL IN UNWANTED SELECTS //
        selectArray.push(selectOneMonth, selectOneDay, selectOneYear,
                        selectTwoMonth, selectTwoDay, selectTwoYear);
        
        wrapSelectsWithDiv(selectArray);
        addClassToElement(cyclesFormSelect, 'profile__select');
        addClassToElement(startDateSelectContainer, 'manage-cycles-form__start-date');
        addClassToElement(endDateSelectContainer, 'manage-cycles-form__end-date');
        addStylesToSelectParent(cyclesFormSelect, 'profile-filter-styled');
        addIconToSelect(cyclesFormSelect, 'profile-filter-arrow');
        
    }
    
})();