# Gender Facts
male = {"john", "paul", "mike", "tom"}
female = {"mary", "lisa", "susan", "anna"}

# Parent Facts: A dictionary where each parent points to a list of their children
parent = {
    "john": ["mary", "paul"],
    "mary": ["susan", "mike"],
    "paul": ["tom"],
    "susan": ["anna"]
}

# Check if someone is a parent of another
def is_parent(parent_name, child_name):
    return child_name in parent.get(parent_name, [])

# Sibling Relationship
def siblings(x, y):
    for p in parent:
        if x in parent[p] and y in parent[p] and x != y:
            return True
    return False

# Grandparent Relationship
def is_grandparent(grandparent, grandchild):
    for child in parent.get(grandparent, []):
        if is_parent(child, grandchild):
            return True
    return False

# Aunt or Uncle Relationship
def aunt_or_uncle(aunt_uncle, niece_nephew):
    for p in parent:
        if siblings(aunt_uncle, p) and is_parent(p, niece_nephew):
            return True
    return False

# Cousin Relationship
def cousins(cousin1, cousin2):
    for p1 in parent:
        for p2 in parent:
            if p1 != p2 and siblings(p1, p2) and is_parent(p1, cousin1) and is_parent(p2, cousin2):
                return True
    return False

# Ancestor Relationship
def ancestor(ancestor_name, descendant):
    if is_parent(ancestor_name, descendant):
        return True
    for child in parent.get(ancestor_name, []):
        if ancestor(child, descendant):
            return True
    return False

# Testing Queries
print("Is Mary and Paul siblings?", siblings("mary", "paul"))
print("Is John grandparent of Susan?", is_grandparent("john", "susan"))
print("Is Mary aunt or uncle of Tom?", aunt_or_uncle("mary", "paul"))
print("Are Susan and Tom cousins?", cousins("susan", "tom"))
print("Is John an ancestor of Anna?", ancestor("john", "anna"))
