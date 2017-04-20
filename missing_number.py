def diff(list1, list2):
    list_to_return = []
    c = set(list1).union(set(list2))
    d = set(list1).intersection(set(list2))

    list_to_return = list(c - d)

    if set(list1) == set(list2):
        return "0"

    else:

        if(len(list_to_return)) == 0:

            return "0"

        else:
            return list(c - d)