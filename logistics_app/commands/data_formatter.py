def format_data(data_list, data_type, id_func, info_func):
    formatted_data = []

    if len(data_list) == 0:
        return f'{data_type}: No information\n'
    else:
        for item in data_list:
            item_id = id_func(item)
            item_info = info_func(item)
            formatted_data.append([item_id] + item_info)
        
        final_items = []
        for item_data in formatted_data:
            joined_item = ' - '.join(item_data)
            final_items.append(joined_item)
        
        all_items_joined = ' / '.join(final_items)
        return f"{data_type}: {all_items_joined}\n"