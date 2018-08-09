// PROFILE TEMPLATE JS //

(() => {

    const profileSelect = document.getElementById('id_country');

    // ADD CLASS TO SELECT BOX FOR STYLING //
    addClassToElement(profileSelect, 'profile__select');
    addBgColorToBody('body-color');
    addStylesToFormSelect(profileSelect, 'profile-filter-styled');

})();