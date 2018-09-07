// HEADER RELATED JS //
(() => {

    const dropDown = document.getElementById("drop-down-menu");
    const dropDownIcon = document.getElementById("drop-down-icon");
    const moreIcons = document.getElementsByClassName("more__icon");
    const navIcons = document.getElementsByClassName("nav__icons");
    const headerBannerComplete = document.getElementById("header-banner__complete");
    const headerBannerPending = document.getElementById("header-banner__pending");
    const headerBannerActive = document.getElementById("header-banner__active");
    const headerBannerCancelled = document.getElementById("header-banner__cancelled");
       
    // FUNCTION CALLS FROM UTILITY JS //
                        // Click Element, Affected Element, Class //
    addRemoveClassOnClick(dropDownIcon, dropDown, "drop-down-menu--show");
    addRemoveClassOnClick(dropDownIcon, dropDownIcon, "more--rotate")


    // ADD CLICKED COLOR TO DROP DOWN MENU ICON ON CLICK //
    for (let i = 0; i < moreIcons.length; i++ ) {
       
        addRemoveClassOnClick(dropDownIcon, moreIcons[i], "more--clicked-color");

    }

    // CALL TIPPY TOOL TIP ON NAV ICONS //
    for (let i = 0; i < navIcons.length; i++) {

        tippy(navIcons[i], toolTip);

    }

    tippy(headerBannerComplete, toolTip);
    tippy(headerBannerPending, toolTip);
    tippy(headerBannerActive, toolTip);
    tippy(headerBannerCancelled, toolTip);
    
})();