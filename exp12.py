# repo-1
class Node:
def __init__(self,data):
self.data=data
self.next=self.prev=None
class DLinkedList:
def __init__(self):
self.head=None
self.ctr=0
def insert_beg(self,data):
node=Node(data)
if self.head==None:
self.head=node
else:
node.next=self.head
self.head.prev=node
self.head=node
self.ctr +=1
print(&quot;Nodes inserted&quot;,data)
return
def insert_end(self,data):
node=Node(data)
if self.head==None:
self.head=node
else:
temp=self.head
while(temp.next is not None):
temp=temp.next
temp.next=node
node.prev=temp
self.ctr +=1
print(&quot;Node inserted&quot;,data)
return

def delete_beg(self):
if self.head==None:
print(&quot;No node exist&quot;)
else:
print(&quot;Node deleted&quot;,self.head.data)
self.head=self.head.next
self.head.prev=None
self.ctr -=1
return
def delete_end(self):
if self.head==None:
print(&quot;No nodes exist&quot;)
elif self.ctr==1:
self.ctr=0
print (&quot;Node deleted&quot;,self.head.data)
self.head=None
else:
temp=self.head
while temp.next is not None:
temp=temp.next
print(&quot;Node deleted&quot;,temp.data)
temp=temp.prev
temp.next=None
self.ctr -=1
return
def insert_pos(self,pos,data):
if pos==0:
self.insert_beg(data)
elif pos==self.ctr:
self.insert_end(data)
else:
node=Node(data)
temp=self.head
i=1
while i&lt;pos-1:
temp=temp.next
i +=1
node.next=temp.next
temp.next.prev=node
temp.next=node
node.prev=temp
self.ctr +=1
print(&quot;Node inserted&quot;,data)
return

def delete_pos(self,pos):
if self.head==None:
print(&quot;Node is empty&quot;)
else:
if pos==0:
self.delete_beg()
elif pos==self.ctr:
self.delete_end()
else:
temp=self.head
i=0
while i&lt;pos:
temp=temp.next
i+=1
print(&quot;node deleted&quot;,temp.data)
temp.prev.next=temp.next
temp.next.prev=temp.prev
temp.next=None
temp.preve=None
self.ctr -=1
return
def traverse_f(self):
if self.head==None:
print(&quot;No nodes exist&quot;)
temp=self.head
i=0
while i&lt;self.ctr:
print(temp.data)
temp=temp.next
i+=1
return
def traverse_r(self):
if self.head==None:
print(&quot;No nodes exist&quot;)
temp=self.head
while temp.next is not None:
temp=temp.next
while temp is not None:
print(temp.data)
temp=temp.prev
def menu():
print(&quot;1.Insert at beginning&quot;)
print(&quot;2.Insert at position&quot;)

print(&quot;3.Insert at end&quot;)
print(&quot;4.Delete at beginning&quot;)
print(&quot;5.Delete at position&quot;)
print(&quot;6.Delete at end&quot;)
print(&quot;7.Count no of nodes&quot;)
print(&quot;8.Traverse forward&quot;)
print(&quot;9.Traverse reverse&quot;)
print(&quot;10.Quit&quot;)
ch=eval(input(&quot;Enter choice:&quot;))
return ch
print(&quot;******************Double linked list**************&quot;)
d=DLinkedList()
while True :
ch=menu()
if ch==1:
data=eval(input(&quot;Enter data:&quot;))
d.insert_beg(data)
elif ch==2:
data=eval(input(&quot;Enter data:&quot;))
pos=int(input(&quot;Enter position:&quot;))
d.insert_pos(pos,data)
elif ch==3:
data=eval(input(&quot;Enter data:&quot;))
d.insert_end(data)
elif ch==4:
d.delete_beg()
elif ch==5:
pos=int(input(&quot;Enter position:&quot;))
d.delete_pos(pos)
elif ch==6:
d.delete_end()
elif ch==7:
print(&quot;Number of nodes&quot;,d.ctr)
elif ch==8:
d.traverse_f()
elif ch==9:
d.traverse_r()
else:
print(&quot;Exit&quot;)
break
