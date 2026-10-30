General Backtracking Structure

def dfs(...):

    # Check whether the current choice is valid

    # Make a choice

    # Explore recursively

    # Undo the choice

Local State vs. Shared State

Integers and Strings are immutable, so changes do not affect the parent
- this is preferred vs. having a global variable

Local State: No restoration needed because each revursive call maintains its own variables
Shared State: Restore Changes when necessary so other branches start with the correct state