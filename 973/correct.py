def left_rotate(s: str, d: int) -> str:
    """Left rotate string s by d characters."""
    d = d % len(s) if s else 0   # handle d > len(s)
    return s[d:] + s[:d]
