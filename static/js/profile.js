// PROFILE TEMPLATE JS //

(() => {

    const profileSelect = document.getElementById('id_country');
    // ADD CLASS TO SELECT BOX FOR STYLING //
    addClassToSelect(profileSelect, 'profile__select');

    // ADD CLASSES TO PARENT ELEMENT OF SELECT BOX //
    profileSelect.parentElement.setAttribute('class', 'profile-filter-styled');
    // INSERT ICON INOT SELECT BOX //
    profileSelect.parentElement.insertAdjacentHTML('beforeend',
                        '<i class="fas fa-sort-down profile-filter-arrow" aria-hidden="true"></i>');


})();