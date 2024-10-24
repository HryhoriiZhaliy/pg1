def levensteinova_vzdalenost(dotaz1, dotaz2):
    m = len(dotaz1)
    n = len(dotaz2)
    prev_row = [j for j in range(n + 1)]
    curr_row = [0] * (n + 1)
 
    # Dynamic programming to fill the matrix
    for i in range(1, m + 1):
        # Initialize the first element of the current row
        curr_row[0] = i
 
        for j in range(1, n + 1):
            if dotaz1[i - 1] == dotaz2[j - 1]:
                # Characters match, no operation needed
                curr_row[j] = prev_row[j - 1]
            else:
                # Choose the minimum cost operation
                curr_row[j] = 1 + min(
                    curr_row[j - 1],  # Insert
                    prev_row[j],      # Remove
                    prev_row[j - 1]    # Replace
                )
 
        # Update the previous row with the current row
        prev_row = curr_row.copy()
 
    # The final element in the last row contains the Levenshtein distance
    return curr_row[n]




if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost(query1, query2))
    print(levensteinova_vzdalenost(query2, query3))
    print(levensteinova_vzdalenost(query1, query3))