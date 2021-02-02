# TODO: Implement this! (4 points)
from nltk.tokenize import WordPunctTokenizer
def tokenize(text):
    """
        Tokenizes the input text. Use the WordPunctTokenizer
        Input: text - a string
        Output: a list of tokens
    """
    # YOUR CODE HERE
    tk = WordPunctTokenizer() 
    output = tk.tokenize(text)
    return output
