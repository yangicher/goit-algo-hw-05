import timeit

def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0
    last = {}
    for i in range(m):
        last[pattern[i]] = i
    i = m - 1
    k = m - 1
    while i < n:
        if text[i] == pattern[k]:
            if k == 0:
                return i
            else:
                i -= 1
                k -= 1
        else:
            j = last.get(text[i], -1)
            i = i + m - min(k, j + 1)
            k = m - 1
    return -1

def rabin_karp(text, pattern):
    d = 256
    q = 101
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            if text[i : i + m] == pattern:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1

def kmp_search(text, pattern):
    def compute_lps(pattern):
        lps = [0] * len(pattern)
        length = 0
        i = 1
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    m = len(pattern)
    n = len(text)
    lps = compute_lps(pattern)
    i = 0
    j = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def measure_time(text, pattern, algorithm):
    print(
        f"{algorithm} pattern {pattern}"
    )
    if algorithm == "boyer_moore":
        return timeit.timeit(lambda: boyer_moore(text, pattern), number=1)
    elif algorithm == "kmp":
        return timeit.timeit(lambda: kmp_search(text, pattern), number=1)
    elif algorithm == "rabin_karp":
        return timeit.timeit(lambda: rabin_karp(text, pattern), number=1)


def main():
    with open(file_name_1, "rb") as file:
        text1 = file.read().decode("utf-8", errors="ignore")
    
    with open(file_name_2, "rb") as file:
        text2 = file.read().decode("utf-8", errors="ignore")

    existing_substring = "алгоритм" 
    non_existing_substring = "nonexistentpattern"

    algorithms = ["boyer_moore", "kmp", "rabin_karp"]

    results = []

    for text, text_name in [(text1, file_name_1), (text2, file_name_2)]:
        for substring, substring_type in [
            (existing_substring, "existing"),
            (non_existing_substring, "non_existing"),
        ]:
            for algorithm in algorithms:
                time_taken = measure_time(text, substring, algorithm)
                results.append((text_name, substring_type, algorithm, time_taken))

    with open("readme.md", "w", encoding="utf-8") as file:
        file.write("# Comparison of Substring Search Algorithms\n\n")
        file.write("| Article  | Substring Type | Algorithm    | Time (seconds) |\n")
        file.write("|----------|----------------|--------------|----------------|\n")
        for result in results:
            file.write(
                f"| {result[0]} | {result[1]} | {result[2]} | {result[3]:.6f} |\n"
            )

        file.write("\n## Conclusions\n")
        file.write("Based on the measured times, we can conclude the following:\n")
        for text_name in [file_name_1, file_name_2]:
            for substring_type in ["existing", "non_existing"]:
                subset = [
                    r for r in results if r[0] == text_name and r[1] == substring_type
                ]
                fastest = min(subset, key=lambda x: x[3])
                file.write(
                    f"- For {text_name} with a {substring_type} substring, the fastest algorithm is {fastest[2]} with a time of {fastest[3]:.6f} seconds.\n"
                )
        overall_fastest = min(results, key=lambda x: x[3])
        file.write(
            f"\nOverall, the fastest algorithm is {overall_fastest[2]} with a time of {overall_fastest[3]:.6f} seconds.\n"
        )

file_name_1 = "text1.txt"
file_name_2 = "text2.txt"

if __name__ == "__main__":
    main()