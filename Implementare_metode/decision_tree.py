def calculate_loan_days_tree(has_penalties, is_new_release, is_student):
    """
    Control-Flow Approach: The code structure visually represents the branches
    of the decision tree. It leverages the "Fast-fail" / "Don't care" concept
    intrinsic to the tree logic.
    """
    # ROOT NODE: The most critical condition
    if has_penalties == True:
        return 0  # LEAF NODE: The path ends here (Loan rejected)
    else:
        # INTERNAL NODE 1: Check the type of the book
        if is_new_release == True:

            # INTERNAL NODE 2 (Left Branch): Check user subscription
            if is_student == True:
                return 7  # LEAF NODE
            else:
                return 14  # LEAF NODE

        else:  # The book is an older release

            # INTERNAL NODE 2 (Right Branch): Check user subscription
            if is_student == True:
                return 30  # LEAF NODE
            else:
                return 21  # LEAF NODE


# --- Test Case Execution ---
print("Tree Result (Penalties=False, NewRelease=True, Student=False):",
      calculate_loan_days_tree(False, True, False), "days")