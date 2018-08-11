// JS FOR ALL 3 TEMPLATES MANAGE CLIENT, JOBS AND CYCLES //

(() => {
    // COMMON TO CLIENTS, JOBS AND CYCLES TEMPLATES //
    const manageDeleteItemButtons = document.getElementsByClassName('manage-delete');
    const hiddenDeleteDiv = document.getElementById('manage-show-delete');

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
    const hiddenResetDiv = document.getElementById('manage-show-reset');
    const manageResetItemButtons = document.getElementsByClassName('manage-reset');
    const selectArray = [];

    // GET ALL THE DELETE BUTTONS BY CLASS, LOOK FOR BUTTONS WITH DATA-ID ATTR, 
    // TRAVERSE TO DIV TO SHOW/HIDE AND CALL UTILITY addRemoveClassOnClick FUNCTION
    // AND CALL insertHTMLonClick TO ALTER BUTTON DISPLAY

    const addRemoveManageButtonClasses = (hiddenDiv, buttons, showClass, clickClass) => {

        
        for (let i = 0; i < buttons.length; i++) {

            addRemoveClassOnClick(buttons[i], 
                                    hiddenDiv, 
                                    showClass);
    
            addRemoveClassOnClick(buttons[i], 
                                buttons[i], 
                                clickClass);

        }

    }


    const showHideDiv = (buttons) => {

        for (let i = 0; i < buttons.length; i++) {

            let dataId = buttons[i].getAttribute('data-id');
            
            if (dataId == 'Delete Job') {
                
                insertNotSureOnClick(buttons[i], dataId);
       
            } else if (dataId == 'Delete Client'){

                insertNotSureOnClick(buttons[i], dataId);

            } else if (dataId == 'Delete Cycle') {

                
                insertNotSureOnClick(buttons[i], dataId);

            } else if (dataId == 'Reset Cycle') {
                
                insertNotSureOnClick(buttons[i], dataId);
            }
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
    showHideDiv(manageDeleteItemButtons);
    addBgColorToBody('body-color');
    addRemoveManageButtonClasses(hiddenDeleteDiv, 
                                manageDeleteItemButtons,
                                'manage-delete__button--show',
                                'manage-button__button--delete-click');
    

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

        // SELECT AND DE-SELECT DELETE AND RESET BUTTON ELEMENT STYLES //
        for (let i = 0; i < manageResetItemButtons.length; i++) {
            
            manageResetItemButtons[i].addEventListener('click', function() {

                if (manageDeleteItemButtons[i].classList.contains('manage-button__button--delete-click')) {
                    
                    manageDeleteItemButtons[i].classList.remove('manage-button__button--delete-click');
                    hiddenDeleteDiv.classList.remove('manage-delete__button--show');
                    insertNotSureOnOtherButtonClick(manageResetItemButtons[i], 
                                                    'Delete Cycle', 
                                                    manageDeleteItemButtons[i]);

                }
            });

            manageDeleteItemButtons[i].addEventListener('click', function() {

                if (manageResetItemButtons[i].classList.contains('manage-button__button--reset-click')) {
                    
                    manageResetItemButtons[i].classList.remove('manage-button__button--reset-click');
                    hiddenResetDiv.classList.remove('manage-reset__button--show');
                    insertNotSureOnOtherButtonClick(manageDeleteItemButtons[i], 
                                                    'Reset Cycle', 
                                                    manageResetItemButtons[i]);

                }
            });

        }

    // POPULATE ARRAY WITH ELEMENTS, COULD NOT GET ELEMENTS BY TAG OR CLASS AS IT //
    // WILL PULL IN UNWANTED SELECTS //
        selectArray.push(selectOneMonth, selectOneDay, selectOneYear,
                        selectTwoMonth, selectTwoDay, selectTwoYear);
        
        wrapSelectsWithDiv(selectArray);
        
        addClassToElement(cyclesFormSelect, 'profile__select');
        addClassToElement(startDateSelectContainer, 'manage-cycles-form__start-date');
        addClassToElement(endDateSelectContainer, 'manage-cycles-form__end-date');
        addStylesToSelectParent(cyclesFormSelect, 'profile-filter-styled');
        addIconToSelect(cyclesFormSelect, 'profile-filter-arrow');    
        showHideDiv(manageResetItemButtons);
        addRemoveManageButtonClasses(hiddenResetDiv, 
                                    manageResetItemButtons,
                                    'manage-reset__button--show',
                                    'manage-button__button--reset-click');
        
    }
    
})();