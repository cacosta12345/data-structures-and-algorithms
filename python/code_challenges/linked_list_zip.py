from data_structures.linked_list import LinkedList, Node

def zip_lists(list1, list2):
    if not list1.head:
        return list2
    if not list2.head:
        return list1

    current1 = list1.head
    current2 = list2.head
    while current1 and current2:
        next1 = current1.next
        next2 = current2.next

        current1.next = current2
        if next1:  # Check if there are remaining nodes in list1
            current2.next = next1
        else:
            break  # If list1 is shorter, break the loop

        current1 = next1
        current2 = next2

    return list1

