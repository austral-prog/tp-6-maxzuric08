# Replace the "ANSWER HERE" with your answer

def remove_elements(list_to_remove_elements):
    if len(list_to_remove_elements)-1>=5:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
        del list_to_remove_elements[3]
    elif len(list_to_remove_elements)-1>=4:
        del list_to_remove_elements[0]
        del list_to_remove_elements[3]
    elif len(list_to_remove_elements)-1<4 and list_to_remove_elements!=[]:
        del list_to_remove_elements[0]
    return list_to_remove_elements  # Remove this line and implement


def add_elements(list_to_add_elements):
    list_to_add_elements.insert(0,'Pink')
    list_to_add_elements.append('Yellow')
    return list_to_add_elements  # Remove this line and implement


def is_empty(list_to_check):
    if list_to_check==[]:
        return True
    else:
        return False
      # Remove this line and implement


def check_lists(list_to_compare1, list_to_compare2):
    if (len(list_to_compare1)>=3 and len(list_to_compare2)>=3) and (list_to_compare2[2]==list_to_compare1[2]):
        return True
    else:
        return False
      # Remove this line and implement


def list_of_lists(list_of_lists_to_modify):
    list_of_lists_to_modify[0]=list_of_lists_to_modify[0][0:2]
    list_of_lists_to_modify[1]=list_of_lists_to_modify[1][1:4]
    list_of_lists_to_modify[2]=list_of_lists_to_modify[2][-2:]
    return list_of_lists_to_modify # Remove this line and implement
