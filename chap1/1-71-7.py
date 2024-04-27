input_string = input().split(",")
i = input_string.index("boundary")
yamyanote_list = input_string[:i]
keio_list = input_string[i+1:]
transfer = [station for station in yamyanote_list if station in keio_list]
a = yamyanote_list.index(transfer[0])
b = keio_list.index(transfer[0])
route = yamyanote_list[:a] + keio_list[b:]
print(route)