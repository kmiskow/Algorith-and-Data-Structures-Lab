from typing import List


def find(pattern: str, text: str) -> List[int]:
    result = []
    N = len(text)
    M = len(pattern)
    BASE = 256
    PRIME = 101
    HASH = pow(BASE, M - 1, PRIME)

    if N < M or not pattern or not text:
        return result

    # Calculate hash for pattern and first window of text
    pattern_hash = 0
    text_hash = 0
    for i in range(M):
        pattern_hash = (BASE * pattern_hash + ord(pattern[i])) % PRIME
        text_hash = (BASE * text_hash + ord(text[i])) % PRIME

    # Slide pattern over text one by one
    for i in range(N - M + 1):
        if pattern_hash == text_hash:
            # Check if all characters match
            for j in range(M):
                if text[i + j] != pattern[j]:
                    break
            else:
                result.append(i)

        # Calculate hash for next window of text
        if i < N - M:
            text_hash = (BASE * (text_hash - ord(text[i]) * HASH) + ord(text[i + M])) % PRIME

            # convert to positive in case of negative value
            if text_hash < 0:
                text_hash += PRIME

    return result


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
