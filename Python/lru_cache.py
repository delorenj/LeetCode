class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

    def __str__(self) -> str:
        return f'Node: (key={self.key}, val={self.val})'


class LRUC:
    def __init__(self, capacity: int) -> None:
       self.capacity = capacity
       self.cache = {}
       self.head = None
       self.tail = None

    def _decorator(self, node: Node) -> str:
        if node == self.head == self.tail: return '<--- HEAD & TAIL'
        if node == self.head: return '<--- HEAD'
        if node == self.tail: return '<--- TAIL'
        return ''

    def __str__(self) -> str:
        node = self.head
        s = f'List Nodes\n'
        if not node:
           return s+f'--- Empty ---'

        s += str(node) + self._decorator(node) + '\n'
        while node.prev:
           node = node.prev
           s += str(node) + self._decorator(node) + '\n'

        s += f'\nCache Entries\n'
        s += '\n'.join(str(self.cache[key]) for key in self.cache)
        return s

    def _remove(self, node: Node) -> None:
        if node.prev: node.prev.next = node.next
        if node.next: node.next.prev = node.prev
        if node == self.head: self.head = node.prev
        if node == self.tail: self.tail = node.next

    def _insert(self, node: Node) -> None:
        if not self.tail: self.tail = node
        if self.head:
            self.head.next = node
            node.prev = self.head
        self.head = node

    def put(self, key, val) -> None:
        # if cache full
        #   remove existing key OR
        #   remove tail
        # insert new key val at heac
        if len(self.cache) >= self.capacity and key not in self.cache and self.tail:
            self.cache[self.tail.key] = None
            self._remove(self.tail)
        if key in self.cache:
            self._remove(self.cache[key])
        node = Node(key, val)
        self._insert(node)
        self.cache[key] = node

lruc = LRUC(3)
lruc.put('Tonny', 1)
lruc.put('Tonny', 2)
lruc.put('Tonny', 3)
lruc.put('Peelshoo', 'Atall')
lruc.put('Pongmatic', 'Reem')
lruc.put('Attrociousbirds', 'Atall')
lruc.put('lroo', 'man')
lruc.put('Attrociousbirds', 'PREEM')

print(lruc)

