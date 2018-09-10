// JS FOR ALL 3 TEMPLATES MANAGE CLIENT, JOBS AND CYCLES //
(() => {

    // COMMON TO CLIENTS, JOBS AND CYCLES TEMPLATES //
    const manageDeleteItemButtons = document.getElementsByClassName('manage-delete');
    const clientNavIcon = document.getElementById('nav-clients');
    const jobsNavIcon = document.getElementById('nav-jobs');
    const cyclesNavIcon = document.getElementById('nav-cycles');

    // SPECIFIC TO CLIENT TEMPLATE //
    const manageClientInput = document.getElementsByClassName('register-form__input');
    const manageClients = document.getElementById('manage-clients');
    const noPhoneNumber = document.getElementsByClassName('manage-item__no-client-number');
    const manageClientButton = document.getElementById('manage-client-button');
    const clientFirstName = document.getElementById('id_first_name');
 
    // SPECFIC TO JOB TEMPLATE //
    const jobsFormSelect = document.getElementById('id_client');
    const jobsFormInput = document.getElementsByTagName('input');
    const manageJobs = document.getElementById('manage-jobs');
    const jobTitleInput = document.getElementById('id_job_title');
    const jobNumber = document.getElementById('id_job_number');
    

    // SPECIFIC TO CYCLES TEMPLATE //
    const selectOneMonth = document.getElementById('id_start_date_month');
    const selectOneDay = document.getElementById('id_start_date_day');
    const selectOneYear = document.getElementById('id_start_date_year');
    const selectTwoMonth = document.getElementById('id_end_date_month');
    const selectTwoDay = document.getElementById('id_end_date_day');
    const selectTwoYear = document.getElementById('id_end_date_year');
    const cyclesFormSelect = document.getElementById('id_jobs');
    const manageResetItemButtons = document.getElementsByClassName('manage-reset');
    const selectArray = [];
    const cycleFormButton = document.getElementById('cycle-button');
    const jobsFormButton = document.getElementById('jobs-button');
    const manageCycles = document.getElementById('manage-cycles');
    const manageCyclesPortholeLink = document.getElementsByClassName('manage-items__cycle-link');
    const cycleTitleInput = document.getElementById('id_cycle_title');
    const cycleDescriptionInput = document.getElementById('id_description');
    const cycleLocation = document.getElementById('id_location');
    const cycleStartDate = document.getElementsByClassName('manage-cycles-form__start-date');
    const cycleEndDate = document.getElementsByClassName('manage-cycles-form__end-date');
    const inactivePorholeLink = document.getElementsByClassName('cycles-results__text--grey');


    // SET CYCLE FORM/JOB FORM SELECT TO READONLY IF UPDATING DATA. //
    // JOB/CLIENT CANNOT BE UPDATED OTHERWISE IT CAUSES ISSUES //
    // DOWN THE LINE. //

    const disableUpdateFormSelect = (button, select) => {

        if (button) {

            const disableColor = '#999898';
            select.setAttribute('readonly', 'true');    
            select.style.color = disableColor;
            select.style.cursor = 'default';
            select.nextElementSibling.style.color = disableColor;
        
        }

    }
  
    // GET ALL THE DELETE BUTTONS BY CLASS, LOOK FOR BUTTONS WITH DATA-ID ATTR, 
    // TRAVERSE TO DIV TO SHOW/HIDE AND CALL UTILITY.JS addRemoveClassOnClick FUNCTION
    // AND CALL insertHTMLonClick TO ALTER BUTTON DISPLAY

    const addRemoveManageButtonClasses = (buttons, showClass, clickClass) => {

        for (let i = 0; i < buttons.length; i++) {

            let buttonData = buttons[i].getAttribute('data-id');

            if ( buttonData == 'Delete Cycle' || buttonData == 'Delete Client' || buttonData == 'Delete Job') {

               
                let hiddenDeleteDiv = buttons[i].
                                parentElement.
                                parentElement.
                                parentElement.
                                nextElementSibling;

                addRemoveClassOnClick(buttons[i], 
                                        hiddenDeleteDiv, 
                                        showClass);

            
            } else if (buttonData = 'Reset Cycle') {

                let hiddenResetDiv = buttons[i].
                                    parentElement.
                                    parentElement.
                                    parentElement.
                                    nextElementSibling.
                                    nextElementSibling.
                                    nextElementSibling;

                
                addRemoveClassOnClick(buttons[i], 
                                        hiddenResetDiv, 
                                        showClass);
            }

            addRemoveClassOnClick(buttons[i], 
                                buttons[i], 
                                clickClass);
        }

    }

    // ALTER INNER HTML OF BUTTONS ON CLICK //
    const alterButtonInnerHtml = (buttons) => {

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

    // IF DELETE BUTTON CLICKED, HIDE RESET BUTTON STYLES, IF RESET CLICKED, HIDE DELETE STYLES //
    const hideOtherButtonStylesOnClick = () => {

        for (let i = 0; i < manageResetItemButtons.length; i++) {
            
            manageResetItemButtons[i].addEventListener('click', function() {

                if (manageDeleteItemButtons[i].classList.contains('manage-button__button--delete-click')) {
                    
                    const hiddenDeleteDiv = this.
                                            parentElement.
                                            parentElement.
                                            parentElement.
                                            nextElementSibling.
                                            nextElementSibling;
                    
                
                    manageDeleteItemButtons[i].classList.remove('manage-button__button--delete-click');
                    hiddenDeleteDiv.classList.remove('manage-delete__button--show');
                    insertNotSureOnOtherButtonClick( 'Delete Cycle', 
                                                    manageDeleteItemButtons[i]);

                }
            });

            manageDeleteItemButtons[i].addEventListener('click', function() {

                if (manageResetItemButtons[i].classList.contains('manage-button__button--reset-click')) {
                    
                    const hiddenResetDiv = this.
                                            parentElement.
                                            parentElement.
                                            parentElement.
                                            nextElementSibling.
                                            nextElementSibling;
                    
                    manageResetItemButtons[i].classList.remove('manage-button__button--reset-click');
                    hiddenResetDiv.classList.remove('manage-reset__button--show');
                    insertNotSureOnOtherButtonClick( 'Reset Cycle', 
                                                    manageResetItemButtons[i]);

                }
            });

        }

   } 

    //------------------- FUNCTION CALLS ------------------------------//

    // COMMON TO CLIENTS, JOBS AND CYCLES TEMPLATES //

    alterButtonInnerHtml(manageDeleteItemButtons);
    addRemoveManageButtonClasses(
                                manageDeleteItemButtons,
                                'manage-delete__button--show',
                                'manage-button__button--delete-click');
    

    // CLIENTS TEMPLATE SPECIFIC //

    if (manageClients) {

        addRequiredAttribute(manageClientInput);
        addClassToClassList(clientNavIcon, 'nav__icons--clicked');
        // CREATE TOOL TIPS //
        addTitleAttribute(clientFirstName, `Your client should be the person you 
                                            want to have access to your Quotes and Invoices.`)
        tippy(clientFirstName, toolTipRight);

        if (noPhoneNumber) {

            for (let i =0; i < noPhoneNumber.length; i++) {

                tippy(noPhoneNumber[i], toolTipDefault);

            }
            
        }
         
    }

    // JOBS TEMPLATE SPECIFIC //
    if (manageJobs) {

        addClassToElement(jobsFormSelect, 'profile__select');
        addStylesToSelectParent(jobsFormSelect, 'profile-filter-styled');
        addIconToSelect(jobsFormSelect, 'profile-filter-arrow');
        addClassToCollection(jobsFormInput, 'register-form__input');
        disableUpdateFormSelect(jobsFormButton, jobsFormSelect);
        addClassToClassList(jobsNavIcon, 'nav__icons--clicked');
        // CREATE TOOL TIPS //
        addTitleAttribute(jobTitleInput, `Give the overall job a name.
                                        Many payment cycles can be linked to one job.`)
        addTitleAttribute(jobNumber, `Assign a unique job number. 
                                        You will be able to search for all cycles belonging to this job number.`)
        tippy(jobTitleInput, toolTipRight);
        tippy(jobNumber, toolTipRight);
        
    }

    // CYCLES TEMPLATE SPECIFIC //

    if (manageCycles) {

        const startDateSelectContainer = selectOneMonth.parentElement;
        const endDateSelectContainer = selectTwoMonth.parentElement;
            
        // SELECT AND DE-SELECT DELETE AND RESET BUTTON ELEMENT STYLES //
        hideOtherButtonStylesOnClick()

        selectArray.push(selectOneMonth, selectOneDay, selectOneYear,
                        selectTwoMonth, selectTwoDay, selectTwoYear);
        wrapSelectsWithDiv(selectArray, 
                                    'manage-cycles-form__date-select', 
                                    'manage-cycles-form__icon');
        
        addClassToElement(cyclesFormSelect, 'profile__select');
        addClassToElement(startDateSelectContainer, 'manage-cycles-form__start-date');
        addClassToElement(endDateSelectContainer, 'manage-cycles-form__end-date');
        addStylesToSelectParent(cyclesFormSelect, 'profile-filter-styled');
        addIconToSelect(cyclesFormSelect, 'profile-filter-arrow');    
        alterButtonInnerHtml(manageResetItemButtons);
        addRemoveManageButtonClasses(manageResetItemButtons,
                                    'manage-reset__button--show',
                                    'manage-button__button--reset-click');
        disableUpdateFormSelect(cycleFormButton, cyclesFormSelect);
        addClassToClassList(cyclesNavIcon, 'nav__icons--clicked');
       
        // CREATE TOOL TIPS //
        addTitleAttribute(cycleTitleInput, 'Please, assign a name to this payment cycle.');
        addTitleAttribute(cycleDescriptionInput, `For your reference, describe the work 
                                                to be carried out in relation to this payment cycle.`);
        addTitleAttribute(cycleLocation, 'Again, for reference, where will the work be undertaken?');
        addTitleAttribute(cycleStartDate[0], 'Set the date the work is to begin.');
        addTitleAttribute(cycleEndDate[0], 'Set the date the work is to finish.');
        tippy(cycleTitleInput, toolTipRight);
        tippy(cycleDescriptionInput, toolTipRight);
        tippy(cycleLocation, toolTipRight);
        tippy(cycleStartDate[0], toolTipRight);
        tippy(cycleEndDate[0], toolTipRight);
       

       for (let i = 0; i < manageCyclesPortholeLink.length; i++) {

            tippy(manageCyclesPortholeLink[i], toolTipDefault);
        }

        for (let i = 0; i < inactivePorholeLink.length; i++) {

            tippy(inactivePorholeLink[i], toolTipDefault);
        }
        
    }

    hideToolTipsOnScroll();
    detectTouchAndDisableToolTips();
    
})();