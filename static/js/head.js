(() => {

    const dropDown = document.getElementById("drop-down-menu");
    const dropDownIcon = document.getElementById("drop-down-icon");
    const moreIcons = document.getElementsByClassName("more__icon");
    const navIcons = document.getElementsByClassName("nav__icons");

                            // Click Element, Affected Element, Class //
    addRemoveClassOnClick(dropDownIcon, dropDown, "drop-down-menu--show");
    addRemoveClassOnClick(dropDownIcon, dropDownIcon, "more--rotate")


    for (let i = 0; i < moreIcons.length; i++ ) {
       
        addRemoveClassOnClick(dropDownIcon, moreIcons[i], "more--clicked-color");

    }

    /*for (let i = 0; i < navIcons.length; i++) {

        addRemoveClassOnClick(navIcons[i], navIcons[i], "mobile-nav__icons--clicked");
    }*/
    
})();