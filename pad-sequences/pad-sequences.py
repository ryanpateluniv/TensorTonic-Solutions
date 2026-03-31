import numpy as np

def pad_sequences(seqs, pad_value=0, max_len=None):
    """
    Returns: np.ndarray of shape (N, L) where:
      N = len(seqs)
      L = max_len if provided else max(len(seq) for seq in seqs) or 0
    """
    if max_len is None:
        max_len = max((len(s) for s in seqs), default=0)

    for s in seqs:
        while len(s) > max_len:
            s.pop()
        while len(s) < max_len:
            s.append(pad_value)

    return np.array(seqs)
    pass