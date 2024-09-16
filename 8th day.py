def reverseWords(s: str) -> str:
    
    words = s.split()
    reversed_words = words[::-1]

    return ' '.join(reversed_words)


s = "the sky is blue"
result = reverseWords(s)
print(result)  
