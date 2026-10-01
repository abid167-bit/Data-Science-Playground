# Build the LCS (Longest Common Subsequence) DP matrix
def build_lcs_matrix(text1, text2):
    # Get the length of both texts
    m = len(text1)
    n = len(text2)

    # Create a 2D matrix filled with 0
    # Extra row and column are used for the base case
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the DP matrix
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            # If characters are the same, add 1 to diagonal value
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            # If characters are different, take the larger value
            # from the top or left cell
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Return the completed DP matrix
    return dp


# Find the actual LCS by tracing backward through the DP matrix
def backtrack_lcs(text1, text2, dp):
    # Start from the bottom-right corner of the matrix
    i = len(text1)
    j = len(text2)

    # Store LCS characters
    lcs = []

    # Store text differences/alignment
    diff = []

    # Trace backward until we reach the first row or column
    while i > 0 and j > 0:

        # If characters match, they are part of the LCS
        if text1[i - 1] == text2[j - 1]:
            lcs.append(text1[i - 1])
            diff.append(f"  {text1[i - 1]}")

            # Move diagonally
            i -= 1
            j -= 1

        # If top value is greater or equal, take character from text1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            diff.append(f"- {text1[i - 1]}")
            i -= 1

        # Otherwise, take character from text2
        else:
            diff.append(f"+ {text2[j - 1]}")
            j -= 1

    # Add remaining characters from text1
    while i > 0:
        diff.append(f"- {text1[i - 1]}")
        i -= 1

    # Add remaining characters from text2
    while j > 0:
        diff.append(f"+ {text2[j - 1]}")
        j -= 1

    # We found characters backward, so reverse them
    lcs.reverse()
    diff.reverse()

    # Return the LCS and the difference list
    return "".join(lcs), diff


# Display the DP matrix in a readable format
def display_matrix(text1, text2, dp):
    print("\n2D DP Matrix:")

    # Print the characters of the second text as column headers
    print("      ", end="")

    for char in text2:
        print(f"{char:3}", end="")

    print()

    # Print each row of the matrix
    for i in range(len(text1) + 1):

        # First row represents the empty string
        if i == 0:
            print("  Ø ", end="")

        # Other rows represent characters from text1
        else:
            print(f"{text1[i - 1]:3}", end="")

        # Print DP values
        for value in dp[i]:
            print(f"{value:3}", end="")

        print()


# Main function of the program
def main():

    # Display program title
    print("=" * 55)
    print("      LCS TEXT DIFFERENCE & ALIGNMENT GENERATOR")
    print("=" * 55)

    # Take two texts as input from the user
    text1 = input("\nEnter first text: ").strip()
    text2 = input("Enter second text: ").strip()

    # Check if either text is empty
    if not text1 or not text2:
        print("\nError: Both texts must contain at least one character.")
        return

    # Build the LCS DP matrix
    dp = build_lcs_matrix(text1, text2)

    # Find the LCS and text differences
    lcs, diff = backtrack_lcs(text1, text2, dp)

    # Display the DP matrix
    display_matrix(text1, text2, dp)

    # Display the final results
    print("\n" + "=" * 55)
    print("RESULT")
    print("=" * 55)

    print(f"First Text       : {text1}")
    print(f"Second Text      : {text2}")
    print(f"LCS              : {lcs}")
    print(f"LCS Length       : {len(lcs)}")

    # Display text differences/alignment
    print("\n--- Text Diff / Alignment ---")

    for line in diff:
        print(line)

    print("=" * 55)


# Run the main function when this file is executed
if __name__ == "__main__":
    main()