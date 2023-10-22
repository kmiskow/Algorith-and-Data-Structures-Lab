from typing import List


def find(pattern: str, text: str) -> List[int]:
    match_positions = []

    lps = compute_lps(pattern)
    pattern_length = len(pattern)
    text_length = len(text)
    if not lps:
        return match_positions

    text_index = 0
    pattern_index = 0
    while text_index < text_length:
        if text[text_index] == pattern[pattern_index]:
            pattern_index += 1
            text_index += 1
            if pattern_index != pattern_length:
                continue
            match_positions.append(text_index - pattern_index)
            pattern_index = lps[pattern_index - 1]
            continue

        if pattern_index > 0:
            pattern_index = lps[pattern_index - 1]
            continue

        text_index += 1

    return match_positions


def compute_lps(pattern: str) -> List[int]:
    if not len(pattern):
        return []
    lps = [None] * len(pattern)
    lps[0] = 0

    pattern_length = len(pattern)
    prefix_index = 0
    index = 1
    while index < pattern_length:
        if pattern[index] == pattern[prefix_index]:
            prefix_index += 1
            lps[index] = prefix_index
            index += 1
            continue

        if prefix_index > 0:
            prefix_index -= 1
            continue

        lps[index] = 0
        index += 1

    return lps


def main():
    print(find("AABAA", "AABAACAABAABAA"))
    print(find("", "AABAACAABAABAA"))
    print(find("AABAA", ""))
    print(find("", ""))
    print(find("AABAA", "AABAA"))
    print(find("AABAA", "BBBBBBBBBBBBBB"))
    print(find("AABAA", "A"))


if __name__ == "__main__":
    main()
