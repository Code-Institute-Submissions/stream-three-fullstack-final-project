// PROFILE TEMPLATE JS //

(() => {

    const profileSelect = document.getElementById('id_country');

    // ADD CLASS TO SELECT BOX FOR STYLING //
    addClassToElement(profileSelect, 'profile__select');
   // addBgColorToBody('body-color');
    addStylesToSelectParent(profileSelect, 'profile-filter-styled');
    addIconToSelect(profileSelect, 'profile-filter-arrow');

})();