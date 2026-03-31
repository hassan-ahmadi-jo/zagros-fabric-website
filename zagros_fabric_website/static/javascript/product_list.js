/// make hidden_show_btn_list & type_of_hidden_box
//// filter
const filter_item_list = ['usage', 'color', 'material', 'pattern', 'width', 'thickness'];
const filter_size_type_list = ['_desktop', '_mobile'];
for (let filter_item of filter_item_list) {
    for (let size_type of filter_size_type_list) {
        const btn_id = 'filter_attribute_' + filter_item + size_type;
        aply_toggle_menu(btn_id, 'basic');
    }
}

aply_toggle_menu('filter_bars', 'os');

filter_bars_close_El = document.getElementById('filter_bars_close');
filter_bars_close_El.addEventListener('click', () => hidden_show_toggle_menu_function('filter_bars', 'os'))


// AJAX
const params = new URLSearchParams(window.location.search);
const filterFormEl = document.getElementById('filter_form');
const productListEl = document.getElementById('product_list');
const removeFilterEl = document.getElementById('remove-filter');
let categoryName = [];
let categoryValue = [];
params.forEach((value, key) => {
    categoryName.push(key);
    categoryValue.push(value);
});

const counterHandler = function (input, type) {
    let number = 0;
    if (parseInt(input, 10)) {
        number = parseInt(input, 10);
    } else if (input != '') {
        return ''
    };

    if (type == 'add') {
        return number + 1
    } else if (type == 'subtract') {
        if (number == 0 || number == 1) {
            return ''
        }
        return number - 1
    }
    return ''
}
const filterFormHandler = function (object) {
    const category = object.target;
    let name = category.name;
    let value = category.value;
    const counterEl = document.querySelector('.js-counter-' + name + '_desktop');
    

    if (categoryName.includes(name) && categoryValue.includes(value)) {
        indexOf = categoryValue.indexOf(value);
        categoryName.splice(indexOf, 1);
        categoryValue.splice(indexOf, 1);
        counterEl.textContent = counterHandler(counterEl.textContent, 'subtract');
    } else {
        categoryName.push(name);
        categoryValue.push(value);
        counterEl.textContent = counterHandler(counterEl.textContent, 'add');
    }
    if (categoryValue.length == 0) {
        removeFilterEl.classList.add('hidden');
        removeFilterEl.classList.remove('flex');
    } else {
        removeFilterEl.classList.add('flex');
        removeFilterEl.classList.remove('hidden');
    }

    url = '/product/?'
    for (i in categoryName) {
        url += categoryName[i] + '=' + categoryValue[i] + '&';
    };

    fetch(url, { headers: { "X-Requested-With": "XMLHttpRequest" } })
        .then(response => response.text())
        .then(
            html => { productListEl.innerHTML = html }
        );
}
filterFormEl.addEventListener('change', function (object) { filterFormHandler(object) });

const initCounter = function(el){
    if (el.textContent == '0'){
        el.textContent = '';
    };  
};
const counters = filterFormEl.querySelectorAll('[class*="js-counter-"]');
counters.forEach(el => {initCounter(el)});





