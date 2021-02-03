import math
def tfidf_search(query, index_set):
    """
        Perform a search over all documents with the given query using tf-idf. 
        Note #1: You have to use the `get_index` (and the `get_df`) function created in the previous cells
        Input: 
            query - a (unprocessed) query
            index_set - the index to use
        Output: a list of (document_id, score), sorted in descending relevance to the given query 
    """
    index = get_index(index_set) # [token] -> [(doc_id, token_count)]
    df = get_df(index_set) # {token: doc_freq}
    processed_query = preprocess_query(query, index_set)
    # YOUR CODE HERE

    # Normalize index?
    relevant_documents = []
    total_documents = 3204 # Dynamicly?
    
    for word in processed_query:
      for term_frequencies in index[word]:
        doc_id = term_frequencies[1]
        tf = term_frequencies[1]
        idf = math.log(total_documents/df[word]) # IDF = log(total_documents/df)
        tf_idf = tf*idf
        if not any([e[0] == doc_id for e in relevant_documents]) : # Document not encountered before
          relevant_documents.append([doc_id, tf_idf])
        else: # Document encountered. Add tf-idf score to previous score
          for document in relevant_documents:
            if document[0] == doc_id:
              document[1] += tf_idf
              break
    # Sort in descending order according to score
    relevant_documents = sorted(relevant_documents,key=lambda x: (x[1]))
    return relevant_documents
