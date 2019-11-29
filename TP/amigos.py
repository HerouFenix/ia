
from constraintsearch import *


def friend_constraint(friend_1, tuple_1, friend_2, tuple_2):
    hat_1, bike_1 = tuple_1
    hat_2, bike_2 = tuple_2

    if friend_1 in tuple_1 or friend_2 in tuple_2:
        return False

    if hat_1 == bike_1 or hat_2 == bike_2:
        return False

    if hat_1 == hat_2 or bike_1 == bike_2:
        return False

    if hat_1 == 'C' and bike_1 != 'B':
        return False

    return True


def make_constraint_graph(friends):
    return {(X, Y): friend_constraint for X in friends for Y in friends if X != Y}


def make_domains(friends):
    return {friend: [(hat, bike) for hat in friends for bike in friends] for friend in friends}

friends = [chr(65+i) for i in range(3)]
cs = ConstraintSearch(make_domains(friends), make_constraint_graph(friends))

print(cs.search())
print(cs.count)