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