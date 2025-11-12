def left_rotate(s: str, d: int) -> str:
    """BUGGY: performs right rotation instead of left rotation."""
    if not s:
        return s
    d = d % len(s)
    return s[-d:] + s[:-d]   # ❌ wrong direction
