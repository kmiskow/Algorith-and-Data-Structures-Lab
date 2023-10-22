from typing import List


def find(pattern: str, text: str) -> List[int]:
    match_positions = []
    pattern_length = len(pattern)
    if not pattern_length:
        return match_positions

    for position in range(len(text) - pattern_length + 1):
        i = 0
        while i < pattern_length:
            if pattern[i] != text[position + i]:
                break
            i += 1

        if i == pattern_length:
            match_positions.append(position)

    return match_positions


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
