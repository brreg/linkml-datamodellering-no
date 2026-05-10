# 1. Skip container class blocks (Containerklasse + XContainer)
/^[A-Za-z0-9_]*Container[A-Za-z0-9_]*[[:space:]]*\{/ {
    skip = 1
    next
}

skip && /^[[:space:]]*\}/ {
    skip = 0
    next
}

skip {
    next
}

# 2. Remove ALL lines mentioning Container (simplest and safe)
/Container/ {
    next
}

# 3. Print rest unchanged
{
    print
}