class stack:
        def __init__(self):
                self.items = []
        def isempty(self):
                if None in self.items:
                        print("Stack is empty")
                else:
                        print("Stack is not empty")
        def push(self,item):
                self.items.append(item)
        def pop(self):
                return self.items.pop()
        def size(self):
                return len(self.items)

class queue:
        def __init__(self):
                self.items = []
        def isempty(self):
                if None in self.items:
                        print("Queue is empty")
                else:
                        print("Queue is not empty")
        def enqueue(self,item):
                self.items.append(item)
        def dequeue(self):
                if len(self.items) < 1:
                        return None
                else:
                        return self.items.pop(0)
        def size(self):
                return len(self.items)

st = stack()
st.push(12)
st.push(23)
st.push(13)
st.push(34)
st.push(24)
st.pop()
st.size()
st.isempty()

qu = queue()
qu.enqueue(12)
qu.enqueue(23)
qu.enqueue(13)
qu.enqueue(34)
qu.enqueue(24)
qu.dequeue()
qu.size()
qu.isempty()
