# TODO: Implement this! (3 points)
def read_queries(root_folder = "./datasets/"):
    """
        Reads in the CACM queries. The dataset is assumed to be in the folder "./datasets/" by default
        Returns: A list of 2-tuples: (query_id, query)
    """
    # YOUR CODE HERE
    list_tuples = []
    unique = 0
    W = ""
    with open(root_folder+'query.text') as f:
        line = f.readline()
        while line:
            read = 0
            if line.startswith(".I"):
                if unique:
                    list_tuples.append((id_tuple, W)) # Append what is known
                    W=""
                id_tuple = int(line.strip(".I ").strip("\n")) # Extract last number string
                unique = 1
            if line.startswith(".W"):
                line = f.readline()
                while not line.startswith("."):
                    W = W+line
                    W = W.replace("\n", " ")
                    line = f.readline()
                    read = 1
            if not read: line = f.readline()
        list_tuples.append((id_tuple, W)) # Append last one
    #raise NotImplementedError()
    return list_tuples
