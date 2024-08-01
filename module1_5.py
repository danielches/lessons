immutable_var = ("hello", 1 , 1.5, ["hello", 1, 1.5],("hello", 1, 1.5))
print(immutable_var)
mutable_list = list(immutable_var)
#кортеж неизменяемый тип данных

mutable_list[0] ="goodbye"
print(mutable_list)