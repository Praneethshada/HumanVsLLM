def reverse_vowels(str1: str) -> str:
    V = "aeiou"          # BUG: uppercase vowels are ignored
    vowels = [c for c in str1 if c in V]
    out = []
    j = len(vowels) - 1
    for ch in str1:
        if ch in V:
            out.append(vowels[j])
            j -= 1
        else:
            out.append(ch)
    return "".join(out)
