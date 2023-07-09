def palindrome(sentence: str) -> bool:
    """verify phrases are polindrome

    Args:
        sentence (str): phrase for verify 

    Returns:
        bool: sentence True or False.

    >>> palindrome("ana")
    True
    """
    sentence = sentence.lower().replace(" ", "")
    return sentence == sentence[::-1]


if __name__ == "__main__":
    print(palindrome("ana"))
