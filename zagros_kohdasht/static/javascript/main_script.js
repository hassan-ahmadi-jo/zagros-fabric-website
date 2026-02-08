// Hidden Boxs: Boxes that are activated and deactivated by clicking a button. 
// if each box activation button has an ID equal to "btn" Each box must have the ID: "btn_box"
let is_menu_open = { 'os': 0, 'basic': 0 }; // all filter types
let did_menu_just_open = { 'os': false, 'basic': false };

const hidden_box_function_with_os_box = function (btn_id) {
    const box_el = toggle_menu_box_El[btn_id];
    const os_el = toggle_menu_os_El[btn_id];

    box_el.classList.toggle('opacity-70');
    box_el.classList.toggle('opacity-100');

    box_el.classList.toggle('scale-95');
    box_el.classList.toggle('scale-100');

    os_el.classList.toggle('opacity-0');
    os_el.classList.toggle('opacity-100');

    os_el.classList.toggle('pointer-events-none');
    os_el.classList.toggle('pointer-events-auto');

    // Personalization
    if (btn_id == 'header_bars') {
        toggle_menu_btn_El['header_bars'].classList.toggle('rotate-90');
        header_bars_close_El.classList.toggle('rotate-90');
    }

    if (btn_id == 'filter_bars') {
        filter_bars_close_El.classList.toggle('rotate-90');
    }
}

const hidden_box_function_basic = function (btn_id) {
    toggle_menu_box_El[btn_id].classList.toggle('hidden')
}


const hidden_show_toggle_menu_function = function (btn_id, menu_type) {
    const run = function (btn_id) {
        if (menu_type == 'os') {
            hidden_box_function_with_os_box(btn_id)
        } else if (menu_type == 'basic') {
            hidden_box_function_basic(btn_id)
        }
        if (is_menu_open[menu_type]) {
            is_menu_open[menu_type] = 0
        } else {
            is_menu_open[menu_type] = btn_id;
            did_menu_just_open[menu_type] = true;
        }
    }
    if (is_menu_open[menu_type] != btn_id && is_menu_open[menu_type] != 0) {
        run(is_menu_open[menu_type]);
        is_menu_open[menu_type] = 0;
    }
    run(btn_id);
}

const toggle_menu_btn_El = {};
const toggle_menu_box_El = {};
const toggle_menu_close_El = {};
const toggle_menu_os_El = {};


const aply_toggle_menu = function (btn_id, menu_type) {
    btn_El = document.getElementById(btn_id);
    box_El = document.getElementById(btn_id + '_box');
    if (menu_type == 'os') {
        os_El = document.getElementById(btn_id + '_os');
        toggle_menu_os_El[btn_id] = os_El
    }
    toggle_menu_btn_El[btn_id] = btn_El
    toggle_menu_box_El[btn_id] = box_El
    toggle_menu_btn_El[btn_id].addEventListener('click', () => hidden_show_toggle_menu_function(btn_id, menu_type));
}
const header_menu_btn_os_type_id_list = ['header_ul_1', 'header_ul_2', 'header_bars', 'header_serch'];
const header_menu_btn_basic_type_id_list = ['header_ul_1_mobile', 'header_ul_2_mobile', 'header_serch_mobile'];
for (let btn_id of header_menu_btn_os_type_id_list){    
    aply_toggle_menu(btn_id, 'os');
}
for (let btn_id of header_menu_btn_basic_type_id_list){    
    aply_toggle_menu(btn_id, 'basic');
}


header_bars_close_El = document.getElementById('header_bars_close');
header_bars_close_El.addEventListener('click', () => hidden_show_toggle_menu_function('header_bars', 'os'))


// price display from 120000 to 120,000 for class price
const price_element = document.querySelectorAll('.price');
const price_display = function (price) {
    const price_len = price.length;
    let price_str = '';
    for (let i in price) {
        price_str += price[i];
        if ((price_len - i - 1) % 3 === 0 & i != (price_len - 1)) {
            price_str += ',';
        }
    }
    return price_str;
}

const price_display_elements = function (el) {
    const text = el.textContent;
    el.textContent = price_display(text);
}

price_element.forEach(el => {
    price_display_elements(el);
})

// If clicked outside the menu, the menu will close.
const hidden_menu_click_listener = function (event) {
    for (let menu_type of Object.keys(is_menu_open)) {
        if (is_menu_open[menu_type]) {
            if (!did_menu_just_open[menu_type]) {
                let element_in_box = false
                id = '#' + is_menu_open[menu_type] + '_box'
                if (event.target.closest(id)) {
                    element_in_box = true;
                }
                if (!element_in_box) {
                    hidden_show_toggle_menu_function(is_menu_open[menu_type], menu_type);
                    is_menu_open[menu_type] = 0;
                }
            }
            did_menu_just_open[menu_type] = false;
        }
    }
}
document.addEventListener('click', (event) => hidden_menu_click_listener(event));


// serch box
// header_clear_serch.addEventListener('click', () => document.getElementById('header_serch_box_text').value = '');
const header_clear_serch_desktop = document.getElementById('header_clear_serch_desktop');
const header_serch_box_text_desktop = document.getElementById('header_serch_box_text_desktop');
header_clear_serch_desktop.addEventListener('click', () => header_serch_box_text_desktop.value = '');
header_serch_box_text_desktop.addEventListener('input', function(){
    if (header_serch_box_text_desktop.value == ''){
        header_clear_serch_desktop.classList.add('!hidden');
    } else{
        header_clear_serch_desktop.classList.remove('!hidden');
    }
});

const header_clear_serch_mobile = document.getElementById('header_clear_serch_mobile');
const header_serch_box_text_mobile = document.getElementById('header_serch_box_text_mobile');
header_clear_serch_mobile.addEventListener('click', () => header_serch_box_text_mobile.value = '');
header_serch_box_text_mobile.addEventListener('input', function(){
    if (header_serch_box_text_mobile.value == ''){
        header_clear_serch_mobile.classList.add('!hidden');
    } else{
        header_clear_serch_mobile.classList.remove('!hidden');
    }
})