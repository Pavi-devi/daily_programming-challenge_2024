def longestCommonPrefix(strs):
    # Edge case: if the list is empty, return an empty string
    if not strs:
        return ""

    # Take the first string as the initial prefix
    prefix = strs[0]

    # Iterate over the rest of the strings in the array
    for s in strs[1:]:
        # Shorten the prefix while it doesn't match the start of string `s`
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            # If the prefix becomes empty, return an empty string
            if not prefix:
                return ""

    return prefix
strs = ["flower", "flow", "flight"]
print(longestCommonPrefix(strs))  # Output: "fl"

