# 04 — Text cleaning, tokenization, counts, TF–IDF and embeddings

[Course map](README.md) · [Practicals](../02-practicals/README.md) · [Questions](../03-questions-and-answers/worked-questions.md#lesson-04)

```mermaid
flowchart LR
 N0["Document"] --> N1["Tokenization"] --> N2["Count or embedding"] --> N3["Task model"] --> N4["Held out evaluation"]
```

## On this page

- [The idea](#the-idea)
- [Work through it](#work-through-it)
- [Common mistakes and practical limits](#common-mistakes-and-practical-limits)

## The idea

**Analogy:** A representation is the alphabet the model sees; removing a word can remove the meaning.

Define document units and tasks before text cleaning. Tokenization maps text into units, which may be words, subwords or bytes. Lowercasing, punctuation removal, stop-word removal and stemming are choices, not universal improvements. Removing “not” can reverse sentiment. Keep train/test document duplicates and author/source effects under control.

Bag-of-words counts tokens; TF–IDF downweights common terms using a corpus-derived statistic. Fit vocabulary and IDF on training data. Sparse linear classifiers and Naive Bayes are strong baselines. Static embeddings assign one vector per token; contextual models change a token's representation with surrounding text.

Evaluate at the task unit: classification metrics for document categories, span metrics for entities, ranking metrics for retrieval. Similarity between embeddings is not factual correctness. New vocabulary, languages and domain-specific phrasing need explicit evaluation rather than assuming English benchmark behaviour transfers.

## Work through it

Documents["not good","good"]need a representation that preserves negation. A count vector with vocabulary[not,good]gives[1,1]and[0,1]. If “not”is deleted, they become identical and no downstream classifier can recover the distinction from those features.

Cosine similarity is $x^Ty/(\|x\|\|y\|)$ for nonzero vectors. Identical directions have similarity 1 even when magnitudes differ.

## Common mistakes and practical limits

Do not compute the vocabulary/IDF across final test documents in an ordinary inductive benchmark. Padding tokens should not be treated as real content. A token ID's numerical size has no semantic distance meaning.

---

[← Convolution, pooling, residual networks and transfer learning](lesson-03-convolution-and-vision.md) · [RNNs, LSTMs, GRUs and sequence learning →](lesson-05-recurrent-sequences.md)
