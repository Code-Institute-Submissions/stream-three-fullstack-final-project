// PAYMENT JS //

(() => {

    const header = document.getElementsByClassName('main-header')[0];
    const footer = document.getElementsByTagName('footer');
    const headerBanner = document.getElementById('header-banner');
    const paymentButton = document.getElementById('payment-button');
    const expiryMonthSelect = document.getElementById('id_expiry_month');
    const expiryYearSelect = document.getElementById('id_expiry_year');
    const selects = document.getElementsByTagName('select');
    const formLabel = document.getElementsByTagName('label');
    const nameOnCard = document.getElementById('id_name_on_card');
    const houseNumber = document.getElementById('id_address1');
    const street = document.getElementById('id_address2');
    const city = document.getElementById('id_city');
    const region = document.getElementById('id_region');
    const postCode =document.getElementById('id_post_code');
    const phone = document.getElementById('id_phone');
    const creditCard = document.getElementById('id_credit_card_number');
    const cvv = document.getElementById('id_cvv');
    const placeholderNames = ['Name on Card', 
                                'House/Flat Number',
                                'Street Address',
                                'Town/City',
                                'Region',
                                'Post Code',
                                'Phone inc country code',
                                'Card Number',
                                'CVV']
    const placeholderInputs = [nameOnCard, houseNumber, street, city, region,
                                postCode, phone, creditCard, cvv ]


    // SET PLACEHOLDERS FOR INPUT //
    const setPlaceholder = () => {

        for (i = 0; i < placeholderNames.length; i++) {
            
            placeholderInputs[i].setAttribute('placeholder', `${placeholderNames[i]}`);
        }

    }
   
    // SET INPUT CLASSES FOR FORM //
    const setInputClass = () =>  {

        for (i = 0; i < placeholderNames.length; i++) {
            
            placeholderInputs[i].setAttribute('class', `payment-form__input`);
        }

    }

    // REMOVE UNWANTED FORM LABELS //
    const removeFormLabels = () => {

        let i = 0;

        while (i < formLabel.length) {

            formLabel[i].style.display = 'none';
            i++;
        }

    }

    // ADDS A BLANK SELECTION TO SELECT BOXES //
    const addBlankSelectToExpiryDates = (select, value) => {

        select.insertAdjacentHTML('afterbegin', `<option value='' selected>Choose Expiry ${value}</option>`);

    }

    // ON PAYMENT COMPLETE CHANGE COLOR OF INPUT/SELECT ELEMENTS AND DISABLE THEM //
    // PREVENTS CLIENT FROM PAYING MORE THAN ONCE //
    const changeFormBgColorOnComplete = () => {

        if (paymentButton.classList.contains('payment-form__button-complete')) {

            for (let i = 0; i < selects.length; i++) {

                selects[i].parentElement.classList.add('payment-form--grey');
                selects [i].setAttribute('disabled', 'true');
            
            }

            for (let i = 0; i < placeholderInputs.length; i++) {

                placeholderInputs[i].classList.add('payment-form--grey');
                placeholderInputs[i].setAttribute('disabled', 'true');

            }

        }
    }
    
    // FUNCTION CALLS //

    addBlankSelectToExpiryDates(expiryMonthSelect, 'Month');
    addBlankSelectToExpiryDates(expiryYearSelect, 'Year');

    // REMOVE RUNNING TOTAL BANNER ON PAYMENT TEMPLATE //
    headerBanner.style.display = 'none';
    header.style.position = 'relative';
    // ----------------------------------------------- //
    removeFormLabels();
    setPlaceholder();
    setInputClass();
    wrapSelectsWithDiv(selects, 
                        'payment-form__select', 
                        'payment-form-select__icon');

    changeFormBgColorOnComplete();

    // CREATE TOOL TIPS //
    
    addTitleAttribute(phone, 'Make sure to include the country code. For example +44 for the UK.')
    tippy(phone, toolTipRight);
    hideToolTipsOnScroll();
    detectTouchAndDisableToolTips();
    

})();

    



