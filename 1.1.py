# TODO: Implement this! (4 points)
def read_cacm_docs(root_folder = "./datasets/"):
    """
        Reads in the CACM documents. The dataset is assumed to be in the folder "./datasets/" by default
        Returns: A list of 2-tuples: (doc_id, document), where 'document' is a single string created by 
            appending the title and abstract (separated by a "\n"). 
            In case the record doesn't have an abstract, the document is composed only by the title
    """
    # YOUR CODE HERE
    list_tuples = []
    unique = 0
    T = ""
    W = ""
    with open(root_folder+'cacm.all') as f:
        line = f.readline()
        while line:
            read = 0
            if line.startswith(".I"):
                # If a T has been found before
                if unique:
                    list_tuples.append((id_tuple, T+W)) # Append what is known
                    T=""
                    W=""
                id_tuple = int(line.strip(".I ").strip("\n")) # Extract last number string
                unique = 1
            if line.startswith(".T"):
                # Extract the next couple of lines
                line = f.readline()
                while not line.startswith("."):
                    T = T+line
                    T = T.replace("\n", " ")
                    line = f.readline()
                    read = 1
            if line.startswith(".W"):
                # Extract next couple of lines
                line = f.readline()
                while not line.startswith("."):
                    W = W+line
                    W = W.replace("\n", " ")
                    line = f.readline()
                    read = 1
            if not read: line = f.readline()
        list_tuples.append((id_tuple, T+W)) # Append last one
    #raise NotImplementedError()
    return list_tuples

print(read_cacm_docs())
