def format_data(data_list, data_type, info_func):
    formatted_data = []

    if len(data_list) == 0:
        return f'{data_type}: No information\n'
    else:
        for idx, item in enumerate(data_list, start=1):
            item_info = info_func(item)
            formatted_data.append(f"{idx}. {item_info}")
        
        total_count_customers = len(data_list)
        all_items_joined = '\n'.join(formatted_data)
        return f"{data_type} ({total_count_customers}):\n{all_items_joined}\n"