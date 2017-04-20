class BinarySearch:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.length = 0
        self.list_to_return = [b]
        self.position = 0

    def create_small_list(self):

        for i in range(0, (self.a - 1)):
            self.list_to_return.append((self.list_to_return[i] + self.b))

        self.length = len(self.list_to_return)

        print (self.list_to_return)

    def search(self, target):

        array = self.list_to_return
        lower = 0
        upper = len(array)
        count = 0

        while lower < upper:

            x = lower + (upper - lower) // 2

            val = array[x]

            count += 1

            if target == val:

                return {x: count}

            elif target > val:
                if lower == x:
                    break

                lower = x

            elif target < val:
                upper = x



