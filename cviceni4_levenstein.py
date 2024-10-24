def levensteinova_vzdalenost(dotaz1, dotaz2):
    m = len(dotaz1)
    n = len(dotaz2)
    prev_row = [j for j in range(n + 1)]
    curr_row = [0] * (n + 1)
 
    for i in range(1, m + 1):
        
        curr_row[0] = i
 
        for j in range(1, n + 1):
            if dotaz1[i - 1] == dotaz2[j - 1]:
               
                curr_row[j] = prev_row[j - 1]
            else:
             
                curr_row[j] = 1 + min(
                    curr_row[j - 1],  # Insert
                    prev_row[j],      # Remove
                    prev_row[j - 1]    # Replace
                )
 
        
        prev_row = curr_row.copy()
 
    
    return curr_row[n]

def levensteinova_vzdalenost2(dotaz1, dotaz2):
    levenstein = 0
    length = min(len(dotaz1), len(dotaz2))
    for i in range(length):
        if dotaz1[i] != dotaz2[i]:
            levenstein += 1
    levenstein += abs(len(dotaz1) - len(dotaz2))
    return levenstein

if __name__ == "__main__":

    query1 = "seznam"
    query2 = "seznamka"
    query3 = "sesnam"

    print(levensteinova_vzdalenost2(query1, query2))
    print(levensteinova_vzdalenost2(query2, query3))
    print(levensteinova_vzdalenost2(query1, query3))