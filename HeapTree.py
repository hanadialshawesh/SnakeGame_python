class HeapTree:
    def __init__(self):
        self.array = []

    def get_root(self):
        if not self.array:
            return -1
        return self.array[0]

    def heappify_max(self, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.array) and self.array[left] > self.array[largest]:
            largest = left
        if right < len(self.array) and self.array[right] > self.array[largest]:
            largest = right
        if largest != i:
            self.array[i], self.array[largest] = self.array[largest], self.array[i]
            self.heappify_max(largest)

    def heappify_min(self, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        if left < len(self.array) and self.array[left] < self.array[smallest]:
            smallest = left
        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right
        if smallest != i:
            self.array[i], self.array[smallest] = self.array[smallest], self.array[i]
            self.heappify_min(smallest)

    def add(self, e):
        self.array.append(e)
        for i in range(len(self.array)//2 - 1, -1, -1):
            self.heappify_max(i)

    def add_min(self, e):
        self.array.append(e)
        for i in range(len(self.array)//2 - 1, -1, -1):
            self.heappify_min(i)

    def print_heap(self):
        for item in self.array:
            print(item, end=" ")
        print()

    def heappify_max_all(self):
        for i in range(len(self.array)//2 - 1, -1, -1):
            self.heappify_max(i)

    def heappify_min_all(self):
        for i in range(len(self.array)//2 - 1, -1, -1):
            self.heappify_min(i)

    def search(self, e):
        found = -1
        for i in range(len(self.array)):
            if e == self.array[i]:
                found = i
        return found

    def remove(self, e):
        index = self.search(e)
        if index != -1:
            self.array[index], self.array[-1] = self.array[-1], self.array[index]
        self.array.pop()
        print(" ")
        self.print_heap()
        print(" ")

        for i in range(len(self.array)):
            self.heappify_max(i)
