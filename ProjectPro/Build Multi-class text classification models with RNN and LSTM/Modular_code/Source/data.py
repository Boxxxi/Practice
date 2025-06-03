import torch
import numpy as np


class TextDataset(torch.utils.data.Dataset):

    def __init__(self, tokens, embeddings, labels):
        """
        :param tokens: List of word tokens
        :param embeddings: Word embeddings (from glove)
        :param labels: List of labels
        """
        self.tokens = tokens
        self.embeddings = embeddings
        self.labels = labels

    def __len__(self):
        return len(self.tokens)

    def __getitem__(self, idx):
        return self.labels[idx], np.array([self.embeddings.get(token, self.embeddings.get('<unk>')) for token in self.tokens[idx]], dtype=np.float32)
