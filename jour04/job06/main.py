example_list = list(range(1, 6))
print(example_list)
example_list[-1], example_list[0] = example_list[0], example_list[-1]
print(example_list)