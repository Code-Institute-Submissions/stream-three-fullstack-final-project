// PROFILE TEMPLATE JS //

(() => {

    const profileSelect = document.getElementById('id_country');

    console.log(profileSelect);
    addClassToSelect(profileSelect, 'profile__country-select');


    profileSelect.parentElement.setAttribute('class', 'profile-filter-styled');
    profileSelect.setAttribute('class', 'profile__select');
    profileSelect.parentElement.insertAdjacentHTML('beforeend','<i class="fas fa-sort-down profile-filter-arrow"></i>');


})();