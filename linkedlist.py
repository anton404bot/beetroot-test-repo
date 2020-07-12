class LinkedList:

    def __init__(self, nodes=None):
        self.head = None
        if nodes is not None:
            node = Node(data=nodes.pop(0))
            self.head = node
            for elem in nodes:
                node.next = Node(data=elem)
                node = node.next

    def add_first(self, node):
        node.next = self.head
        self.head = node

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(node.data)
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)

    def __iter__(self):
        node = self.head    
        while node is not None:
            yield node
            node = node.next

    def remove_node(self, target_node_data):
        if not self.head:
            raise Exception('List is empty')
        if self.head.data == target_node_data:
            self.head = self.head.next
            return 
        previous_node = self.head
        for node in self:
            if node.data == target_node_data:
                previous_node.next = node.next
                return
            previous_node = node    
        raise Exception(f'Node with data {target_node_data} not found')
                
                

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data


llist = LinkedList()
llist.add_first(Node('pervyi'))
llist.add_first(Node('vtoroi'))
print(llist)

llist.remove_node('vtoroi')
print(llist)

llist.remove_node('tretiy')