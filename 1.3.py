# TODO: Implement this! (1 point)
def load_stopwords(root_folder = "./datasets/"):
    """
        Loads the stopwords. The dataset is assumed to be in the folder "./datasets/" by default
        Output: A set of stopwords
    """
    # YOUR CODE HERE
    #raise NotImplementedError()
    list_stopwords = set()
    
    with open(root_folder+'common_words') as f:
        #line = f.readline()
        for line in f:
            list_stopwords.add(line.strip("\n")) # Append last one
    #raise NotImplementedError()
    return list_stopwords
