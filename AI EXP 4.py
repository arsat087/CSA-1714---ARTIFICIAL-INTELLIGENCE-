from itertools import permutations

word1 = input("Enter first word: ").upper()
word2 = input("Enter second word: ").upper()
result = input("Enter result word: ").upper()

letters = []

for ch in word1 + word2 + result:
    if ch not in letters:
        letters.append(ch)

if len(letters) > 10:
    print("More than 10 unique letters. No solution possible.")
else:
    digits = range(10)

    for p in permutations(digits, len(letters)):
        d = {}
        for i in range(len(letters)):
            d[letters[i]] = p[i]

        if d[word1[0]] == 0 or d[word2[0]] == 0 or d[result[0]] == 0:
            continue

        n1 = 0
        for ch in word1:
            n1 = n1 * 10 + d[ch]

        n2 = 0
        for ch in word2:
            n2 = n2 * 10 + d[ch]

        n3 = 0
        for ch in result:
            n3 = n3 * 10 + d[ch]

        if n1 + n2 == n3:
            print("\nSolution Found:")
            for key in sorted(d):
                print(key, "=", d[key])

            print(word1, "=", n1)
            print(word2, "=", n2)
            print(result, "=", n3)
            break
    else:
        print("No solution found.")
