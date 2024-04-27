input_string = input().split(",")
i = input_string.index("boundary")
list = input_string[:i]
exlist = input_string[i+1:]
express_index = [list.index(station) for station in list if station in exlist]
express_index_dif = [express_index[i + 1] - express_index[i] - 1 for i in range(len(express_index) - 1)]
print(express_index_dif)