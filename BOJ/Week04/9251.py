# Longest Common Subsequences
import sys
input = sys.stdin.readline

first_sentences = list(input().strip())
second_sentences = list(input().strip())

rows = len(first_sentences)
cols = len(second_sentences)

dp_table = [[0] * (cols+1) for _ in range(rows + 1)]

for i in range(1, rows+1):
    for j in range(1, cols+1):
        if first_sentences[i - 1] == second_sentences[j - 1]:
            dp_table[i][j] = dp_table[i - 1][j - 1] + 1
        else:
            dp_table[i][j] = max(dp_table[i][j - 1], dp_table[i - 1][j])

print(dp_table[-1][-1])
