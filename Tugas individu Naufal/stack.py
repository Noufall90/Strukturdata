class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

stack = Stack()

initial_elements = [1, 2, 3, 4, 5]
for element in initial_elements:
    stack.push(element)

print("Angka sekarang:", stack.items)

# Tambahkan angka baru
stack.push(6)
stack.push(7)
print("Angka setelah ditambah di belakang:", stack.items)

# Hapus angka dari belakang
out = stack.pop()
print("Angka dihilangkan dari bagian belakang:", out)
print("Angka hasilnya:", stack.items)
