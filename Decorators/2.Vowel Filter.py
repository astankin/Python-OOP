def vowel_filter(function):

    def wrapper():
        letters = function()
        return [vowel for vowel in letters if vowel in "aoeiuyAOEIUY"]
    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]

print(get_letters())
