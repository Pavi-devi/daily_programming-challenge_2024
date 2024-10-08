def insert_sorted(stack, element):
    if not stack or stack[-1] <= element:
        stack.append(element)
    else:
        top = stack.pop()
        insert_sorted(stack, element)
        stack.append(top)

def sort_stack(stack):
    if len(stack) <= 1:
        return
    
    top = stack.pop()
    sort_stack(stack)
    
    insert_sorted(stack, top)


stack = [3, 1, 4, 2]
sort_stack(stack)
print("Sorted stack:", stack)
