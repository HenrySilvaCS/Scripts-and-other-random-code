import numpy as np
from sklearn.decomposition import TruncatedSVD



def distinct_words(corpus):
    """ Determine a list of distinct words for the corpus.
        Params:
            corpus (list of list of strings): corpus of documents
        Return:
            corpus_words (list of strings): list of distinct words across the corpus, sorted 
            num_corpus_words (integer): number of distinct words across the corpus
    """
    corpus_words = set()
    num_corpus_words = -1
    
    flat_list = [y for x in corpus for y in x]
    for i in range(len(flat_list)):
        if flat_list[i] in corpus_words:
            corpus_words.discard(flat_list[i])
        corpus_words.add(flat_list[i])
    
    corpus_words = list(sorted(corpus_words))
    num_corpus_words = len(corpus_words)

    return corpus_words, num_corpus_words
    
    
    def compute_co_occurrence_matrix(corpus, window_size=4):
    """ Compute co-occurrence matrix for the given corpus and window_size (default of 4).
     
        Params:
            corpus (list of list of strings): corpus of documents
            window_size (int): size of context window
        Return:
            M (a symmetric numpy matrix of shape (number of unique words in the corpus , number of unique words in the corpus)): 
                Co-occurence matrix of word counts. 
         
            word2Ind (dict): dictionary that maps word to index (i.e. row/column number) for matrix M.
    """
    words, num_words = distinct_words(corpus)
    corpus_flat = [y for x in corpus for y in x]
    M = np.zeros((num_words,num_words))  
    count = 0
    for word in words:
        words_index = words.index(word)
        for j in range(len(corpus)):
            for corpus_word in corpus[j]:
                if corpus_word == word:
                    for i in range(window_size + 1):
                        if count < window_size:
                            if i != 0:
                                next_word = corpus[j][count + (i)]
                                M[words_index,words.index(next_word)] += 1

                        elif count >= window_size and count < (len(corpus[j]) - window_size):
                            if i != 0:
                                next_word = corpus[j][count + (i)]
                                prev_word = corpus[j][count - i]
                                M[words_index,words.index(next_word)] += 1
                                M[words_index,words.index(prev_word)] += 1
                        else:
                            if i != 0:
                                prev_word = corpus[j][count - i]
                                M[words_index,words.index(prev_word)] += 1

                count += 1
            count = 0
            
    word2Ind = {}
    for i in range(len(words)):
        word2Ind[words[i]] = words.index(words[i])

    return M, word2Ind
  def reduce_to_k_dim(M, k=2):
    """ Reduce a co-occurence count matrix of dimensionality (num_corpus_words, num_corpus_words)
        to a matrix of dimensionality (num_corpus_words, k) using the following SVD function from Scikit-Learn:
            - http://scikit-learn.org/stable/modules/generated/sklearn.decomposition.TruncatedSVD.html
    
        Params:
            M (numpy matrix of shape (number of unique words in the corpus , number of unique words in the corpus)): co-occurence matrix of word counts
            k (int): embedding size of each word after dimension reduction
        Return:
            M_reduced (numpy matrix of shape (number of corpus words, k)): matrix of k-dimensioal word embeddings.
                    In terms of the SVD from math class, this actually returns U * S
    """    
    n_iters = 10     # Use this parameter in your call to `TruncatedSVD`
    M_reduced = None
    print("Running Truncated SVD over %i words..." % (M.shape[0]))
    
    svd = TruncatedSVD(n_components=k,n_iter=n_iters)
    svd.fit(M)
    M_reduced = svd.transform(M)

    print("Done.")
    return M_reduced  
    
