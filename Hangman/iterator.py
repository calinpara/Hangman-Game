class CountTo:

    def __init__(self, value):
        self.value = value
        self.maximum = 26
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.maximum:
            vr = self.index
            self.index += 1
            return vr
        else:
            raise StopIteration


count_to_max = CountTo(25)
count_to_max = list(count_to_max)
