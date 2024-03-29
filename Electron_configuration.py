import math

# Calculates the electron configuration of atoms

Atomic_number =____     # number of electrons


o_name = ['s', 'p', 'd', 'f', 'g']
o_value = [2, 6, 10, 14, 18]
output_string = ""
end_period = 1
while Atomic_number > 0:
    for i in range(math.floor((end_period-1)/2), -1, -1):
        if(Atomic_number > o_value[i]):
            output_string += "{0}{1}({2})".format(end_period -
                                                  i, o_name[i], o_value[i])
        else:
            output_string += "{0}{1}({2})".format(end_period -
                                                  i, o_name[i], Atomic_number)
            Atomic_number = 0
            break
        Atomic_number -= o_value[i]
    end_period += 1
print(output_string)
