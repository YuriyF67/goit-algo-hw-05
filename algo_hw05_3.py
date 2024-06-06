import timeit

with open("article1.txt", "r", encoding="utf-8") as file:
    text1 = file.read()

with open("article2.txt", "r", encoding="utf-8") as file:
    text2 = file.read()

existing_substring = text1[:50]  # Перша 50-символьна частина text1, яка точно існує
non_existing_substring = "qwertyuiopasdfghjklzxcvbnm"  # Підрядок, який точно не існує


# Алгоритм Боєра-Мура
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


# Алгоритм Кнута-Морріса-Пратта
def kmp(text, pattern):
    m = len(pattern)
    n = len(text)
    lps = [0] * m
    j = 0
    compute_lps(pattern, m, lps)
    i = 0
    while i < n:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == m:
            return i - j
            j = lps[j - 1]
        elif i < n and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    return -1


def compute_lps(pattern, m, lps):
    length = 0
    lps[0] = 0
    i = 1
    while i < m:
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


# Алгоритм Рабіна-Карпа
def rabin_karp(text, pattern, q=101):
    m = len(pattern)
    n = len(text)
    p = 0
    t = 0
    h = 1
    d = 256
    for i in range(m - 1):
        h = (h * d) % q
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q
    for i in range(n - m + 1):
        if p == t:
            match = True
            for j in range(m):
                if text[i + j] != pattern[j]:
                    match = False
                    break
            if match:
                return i
        if i < n - m:
            t = (d * (t - ord(text[i]) * h) + ord(text[i + m])) % q
            if t < 0:
                t = t + q
    return -1


# Вимірювання часу виконання
def measure_time(func, text, pattern):
    setup_code = f"from __main__ import {func.__name__}, text, pattern"
    stmt = f"{func.__name__}(text, pattern)"
    return timeit.timeit(stmt, setup=setup_code, number=1000, globals=globals())


# Тести для обох текстів і підрядків
results = {}
for text, text_name in [(text1, "text1"), (text2, "text2")]:
    for pattern, pattern_name in [
        (existing_substring, "existing_substring"),
        (non_existing_substring, "non_existing_substring"),
    ]:
        results[(text_name, pattern_name, "Boyer-Moore")] = measure_time(
            boyer_moore, text, pattern
        )
        results[(text_name, pattern_name, "KMP")] = measure_time(kmp, text, pattern)
        results[(text_name, pattern_name, "Rabin-Karp")] = measure_time(
            rabin_karp, text, pattern
        )

# Аналіз результатів
for key, value in results.items():
    print(
        f"Text: {key[0]}, Pattern: {key[1]}, Algorithm: {key[2]}, Time: {value} seconds"
    )

# Визначення найшвидшого алгоритму
summary = {}
for text_name in ["text1", "text2"]:
    for pattern_name in ["existing_substring", "non_existing_substring"]:
        best_algorithm = min(
            [
                (algo, results[(text_name, pattern_name, algo)])
                for algo in ["Boyer-Moore", "KMP", "Rabin-Karp"]
            ],
            key=lambda x: x[1],
        )
        summary[(text_name, pattern_name)] = best_algorithm

for key, value in summary.items():
    print(
        f"Text: {key[0]}, Pattern: {key[1]}, Best Algorithm: {value[0]}, Time: {value[1]} seconds"
    )
