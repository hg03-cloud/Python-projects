let openBtn = document.querySelectorAll('.mob-btn');
let navList = document.querySelectorAll('.list-items-nav');
let closeBtn = document.querySelectorAll('.close-btn');

openBtn.forEach(function (openMenu) {
    openMenu.addEventListener('click', function () {
        navList.forEach(function (navItem) {
            navItem.classList.add("show");
            document.body.style.overflow = "hidden"
        });
    });
});

closeBtn.forEach(function (closeMenu) {
    closeMenu.addEventListener('click', function () {
        navList.forEach(function (navItem) {
            navItem.classList.remove("show");
            document.body.style.overflow = "auto"
        });
    });
});
