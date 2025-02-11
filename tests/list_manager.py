# Lista global que almacenará los elementos
my_list = []

def initialize_list():
    """Inicializa la lista vacía."""
    global my_list
    my_list = []

def get_list():
    """Retorna la lista actual."""
    return my_list

def add_to_list(item):
    """Agrega un elemento a la lista."""
    my_list.append(item)

def remove_from_list(item):
    """Elimina un elemento de la lista si existe, de lo contrario lanza un ValueError."""
    if item in my_list:
        my_list.remove(item)
    else:
        raise ValueError(f"Item '{item}' not found in list.")

def replace_item_in_list(item, replacement):
    """Reemplaza un elemento en la lista con otro."""
    if item in my_list:
        index = my_list.index(item)
        my_list[index] = replacement
    else:
        raise ValueError(f"Item '{item}' not found in list.")

def get_item_at_position(position):
    """Retorna el elemento en la posición indicada (1-based index)."""
    if position < 1 or position > len(my_list):
        raise ValueError("Position out of range.")
    return my_list[position - 1]
