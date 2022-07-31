//Image slides in Login page
let index = 0;
carousel();

function carousel() {
    let i;
    let x = document.querySelectorAll('.slideImages');
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }

    index++;

    if (index > x.length) {
        index = 1
    }
    x[index - 1].style.display = "block";
    setTimeout(carousel, 2200)

}