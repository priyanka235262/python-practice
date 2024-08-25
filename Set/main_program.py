def main():
    """
    Demonstrates set operations and functionality in Python.
    """

    # Create sets
    set1 = {1, 2, 3, 4}
    set2 = {3, 4, 5, 6}

    # Set operations
    union_set = set1.union(set2)
    intersection_set = set1.intersection(set2)
    difference_set = set1.difference(set2)
    symmetric_difference_set = set1.symmetric_difference(set2)

    # Check for subset and superset
    is_subset = set1.issubset(set2)
    is_superset = set1.issuperset(set2)

    # Add and remove elements
    set1.add(5)
    set1.remove(2)  # Raises KeyError if element not present
    set1.discard(7)  # Does not raise error if element not present

    # Update a set with another set
    set1.update(set2)

    # Clear a set
    set1.clear()

    # Print results
    print("Union:", union_set)
    print("Intersection:", intersection_set)
    print("Difference:", difference_set)
    print("Symmetric difference:", symmetric_difference_set)
    print("Is subset:", is_subset)
    print("Is superset:", is_superset)
    print("Set1 after updates:", set1)

if __name__ == "__main__":
    main()