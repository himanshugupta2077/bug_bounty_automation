def extract_after_asterisk_dot(target):
    # Find the index of the first occurrence of "*." in the input string
    asterisk_dot_index = target.find("*.")
    
    # Check if "*." is present in the input string
    if asterisk_dot_index != -1:
        # Extract the substring after "*."
        result_string = target[asterisk_dot_index + 2:]
        return result_string
    else:
        return None  # Return None if "*." is not found in the input string

# Test the function with a sample input
target = input("Enter a string: ")
result = extract_after_asterisk_dot(target)

if result:
    print(f"Substring after '*.' is: {result}")
else:
    print("The input string does not contain '*.'")
