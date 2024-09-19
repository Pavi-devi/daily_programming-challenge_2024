def permute(s):
    def backtrack(path, options):
        if not options:
            result.append(path)
            return
        for i in range(len(options)):
            backtrack(path + options[i], options[:i] + options[i+1:])

    result = []
    backtrack('', s)
    return sorted(result)  # Sorting is optional, for ordered output

# Example usage
input_string = "abc"
print(permute(input_string))
