// PROFILE TEMPLATE JS //

(() => {

    const profileSelect = document.getElementById('id_country');
    const phone = document.getElementById('id_phone');

    // ADD CLASS TO SELECT BOX FOR STYLING //
    addClassToElement(profileSelect, 'profile__select');
    addStylesToSelectParent(profileSelect, 'profile-filter-styled');
    addIconToSelect(profileSelect, 'profile-filter-arrow');

    addTitleAttribute(phone, 'Make sure to include the country code. For example +44 for the UK.')
    tippy(phone, toolTipRight);
    hideToolTipsOnScroll();

})();