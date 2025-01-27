# Comparison of Substring Search Algorithms

| Article  | Substring Type | Algorithm    | Time (seconds) |
|----------|----------------|--------------|----------------|
| text1.txt | existing | boyer_moore | 0.000118 |
| text1.txt | existing | kmp | 0.000512 |
| text1.txt | existing | rabin_karp | 0.000682 |
| text1.txt | non_existing | boyer_moore | 0.000065 |
| text1.txt | non_existing | kmp | 0.000436 |
| text1.txt | non_existing | rabin_karp | 0.000647 |
| text2.txt | existing | boyer_moore | 0.000104 |
| text2.txt | existing | kmp | 0.000376 |
| text2.txt | existing | rabin_karp | 0.000518 |
| text2.txt | non_existing | boyer_moore | 0.000201 |
| text2.txt | non_existing | kmp | 0.001757 |
| text2.txt | non_existing | rabin_karp | 0.003014 |

## Conclusions
Based on the measured times, we can conclude the following:
- For text1.txt with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000118 seconds.
- For text1.txt with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000065 seconds.
- For text2.txt with a existing substring, the fastest algorithm is boyer_moore with a time of 0.000104 seconds.
- For text2.txt with a non_existing substring, the fastest algorithm is boyer_moore with a time of 0.000201 seconds.

Overall, the fastest algorithm is boyer_moore with a time of 0.000065 seconds.
