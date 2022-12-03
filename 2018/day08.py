from aocd import data

ints = [int(x) for x in data.split()]
  
total_meta = 0
def make_node(ints):
  global total_meta
  
  n_children = ints.pop(0)
  n_meta = ints.pop(0)
  children = []
  for _ in range(n_children):
    children.append(make_node(ints))
  meta = [ints.pop(0) for _ in range(n_meta)]
  total_meta += sum(meta)
  return children, meta
  
def node_value(node):
  children, meta = node
  if len(children) == 0:
    return sum(meta)
  val = 0
  for m in meta:
    index = m-1
    if 0 <= index < len(children):
      val += node_value(children[index])
  return val
    

root = make_node(list(ints))
print('part 1', total_meta)
print('part 2', node_value(root))
