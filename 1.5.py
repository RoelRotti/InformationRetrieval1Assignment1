# TODO: Implement this! (3 points)
from nltk.stem import PorterStemmer

def stem_token(token):
    """
        Stems the given token using the PorterStemmer from the nltk library
        Input: a single token
        Output: the stem of the token
    """
    # YOUR CODE HERE
    ps = PorterStemmer()
    output = ps.stem(token)
    return output
