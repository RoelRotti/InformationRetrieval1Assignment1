# TODO: Implement this! (5 points)
def compute_df(documents):
    """
        Compute the document frequency of all terms in the vocabulary
        Input: A list of documents
        Output: A dictionary with {token: document frequency)
    """
    # YOUR CODE HERE
    document_frequency = {}
    for document in documents:
        unique_tokens_in_document = []
        for token in document:
            if token not in document_frequency: # Token is never ever encountered before
                document_frequency[token] = 1 
                unique_tokens_in_document.append(token)
                #document_frequency[token].append(1)
            elif token not in unique_tokens_in_document: # Token is not previously encountered in document
                document_frequency[token] += 1 
                unique_tokens_in_document.append(token)
    return document_frequency
