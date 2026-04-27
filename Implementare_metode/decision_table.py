def calculate_loan_days_table(has_penalties, is_new_release, is_student):
    """
    Data-Driven Approach: The dictionary represents the exact Decision Table
    (All 8 theoretical rules).
    The dictionary key is a tuple representing the combination:
    (has_penalties, is_new_release, is_student)
    """
    decision_table = {
        (True, True, True): 0,  # R1: Has penalties, other conditions don't matter
        (True, True, False): 0,  # R2: Has penalties
        (True, False, True): 0,  # R3: Has penalties
        (True, False, False): 0,  # R4: Has penalties
        (False, True, True): 7,  # R5: No penalties, New release, Student
        (False, True, False): 14,  # R6: No penalties, New release, Standard user
        (False, False, True): 30,  # R7: No penalties, Old book, Student
        (False, False, False): 21  # R8: No penalties, Old book, Standard user
    }

    # Lookup in the table (O(1) time complexity)
    current_condition = (has_penalties, is_new_release, is_student)
    approved_days = decision_table.get(current_condition, -1)

    return approved_days


# --- Test Case Execution ---
print("Table Result (Penalties=False, NewRelease=True, Student=False):",
      calculate_loan_days_table(False, True, False), "days")