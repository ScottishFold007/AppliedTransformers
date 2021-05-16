# Named Entity Classification

The Named Entity Classification task aims to classify a given number of entities in a given text.

## Models

We currently provide the following models for this task:

- `BertForEntityClassification`

    - Basically a BERT encoder folowed by a linear classification layer. We apply a custom tokenizer which defines the special tokens `[e]` and `[/e]` to mark entities in a corpus. For classification, we pass the corpus through the BERT encoder and gather the outputs for all entity beginning markers (`[e]`). These will then be passed into the classification layer to compute the output logits.

- `BertForSentencePairClassification`

    - [Utilizing BERT for Aspect-Based Sentiment Analysis via Constructing Auxiliary Sentence](https://arxiv.org/abs/1903.09588)


## Datasets

We currently provide the following datasets for this task:

- `SemEval2015Task12_AspectPolarity`
    - [SemEval-2015 Task 12: Aspect Based Sentiment Analysis](https://www.aclweb.org/anthology/S15-2082/)
    - Language: English
    - Domain: Restaurant Reviews
    - Entity Type: Aspects
    - Entity Labels:
        - positive
        - neutral
        - negative
    - [Download](http://alt.qcri.org/semeval2015/task12/index.php?id=data-and-tools)

- `SemEval2015Task12_OpinionPolarity`
    - [SemEval-2015 Task 12: Aspect Based Sentiment Analysis](https://www.aclweb.org/anthology/S15-2082/)
    - Opinion Annotations by: [Coupled Multi-Layer Attentions
for Co-Extraction of Aspect and Opinion Terms](https://www.aaai.org/Conferences/AAAI/2017/PreliminaryPapers/15-Wang-W-14441.pdf)
    - Language: English
    - Domain: Restaurant Reviews
    - Entity Type: Opinions
    - Entity Labels:
        - positive
        - negative
    - [Download](https://github.com/happywwy/Coupled-Multi-layer-Attentions/tree/master/util/data_semEval)

- `SemEval2014Task4`
    - [SemEval-2014 Task 4: Aspect Based Sentiment Analysis](https://www.aclweb.org/anthology/S14-2004/)
    - Language: English
    - Domain: Restaurant + Laptop Reviews
    - Entity Type: Aspects
    - Entity Labels:
        - positive
        - neutral
        - negative
        - conflict
    - [Download](http://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools)

- `SemEval2014Task4_Restaurants`
    - [SemEval-2014 Task 4: Aspect Based Sentiment Analysis](https://www.aclweb.org/anthology/S14-2004/)
    - Language: English
    - Domain: Restaurant Reviews
    - Entity Type: Aspects
    - Polarity Labels: see `SemEval2014Task4`
    - [Download](http://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools)

- `SemEval2014Task4_Laptops`
    - [SemEval-2014 Task 4: Aspect Based Sentiment Analysis](https://www.aclweb.org/anthology/S14-2004/)
    - Language: English
    - Domain: Laptop Reviews
    - Entity Type: Aspects
    - Polarity Labels: see `SemEval2014Task4`
    - [Download](http://alt.qcri.org/semeval2014/task4/index.php?id=data-and-tools)

- `GermanYelp_OpinionPolarity`
    - Language: German
    - Domain: Restaurant Reviews
    - Entity Type: Opinions
    - Entity Labels:
        - positive
        - negative

- `GermanYelp_AspectPolarity`
    - Language: German
    - Domain: Restaurant Reviews
    - Entity Type: Aspects
    - Entity Labels: see `GermanYelp_OpinionPolarity`

## Evaluation

- Hyperparameters
    - Sequence Length: 128
    - Batchsize: 8
    - Learning Rate: 1e-5
    - Weight Decay: 0.01

- `SemEval2015Task12_AspectPolarity`
    
    |                 Model                |  Micro-F1  |  Macro-F1  | Epochs |   Pretrained Model Name      |
    | :----------------------------------- | :--------: | :--------: | :----: | :--------------------------- |
    | `BertForEntityClassification`        |    82.7    |    63.8    |   14   | bert-base-uncased            |
    | `BertForEntityClassification`        |    83.9    |    67.2    |   12   | bert-base-uncased-yelp       |
    | `BertForSentencePairClassification`  |    82.5    |    66.7    |   17   | bert-base-uncased            |
    | `BertForSentencePairClassification`  |  **86.4**  |    70.4    |   16   | bert-base-uncased-yelp       |
    | `BertCapsuleNetwork`                 |    83.4    |    65.1    |   6    | bert-base-uncased            |
    | `BertCapsuleNetwork`                 |    86.0    |  **75.3**  |   13   | bert-base-uncased-yelp       |

- `SemEval2015Task12_OpinionPolarity`
    
    |                 Model                |  Micro-F1  |  Macro-F1  | Epochs |   Pretrained Model Name      |
    | :----------------------------------- | :--------: | :--------: | :----: | :--------------------------- |
    | `BertForEntityClassification`        |    96.3    |    95.1    |   19   | bert-base-uncased            |
    | `BertForEntityClassification`        |    96.5    |    95.4    |   16   | bert-base-uncased-yelp       |
    | `BertForSentencePairClassification`  |    96.5    |    95.4    |   19   | bert-base-uncased            |
    | `BertForSentencePairClassification`  |    96.9    |    95.9    |   16   | bert-base-uncased-yelp       |
    | `BertCapsuleNetwork`                 |    96.9    |    95.9    |   2    | bert-base-uncased            |
    | `BertCapsuleNetwork`                 |  **97.3**  |  **96.4**  |   13   | bert-base-uncased-yelp       |

- `SemEval2014Task4`

    |                 Model                |  Micro-F1  |  Macro-F1  | Epochs |   Pretrained Model Name      |
    | :----------------------------------- | :--------: | :--------: | :----: | :--------------------------- |
    | `BertForEntityClassification`        |    100.0   |    100.0   |   3    | bert-base-uncased            |
    | `BertForSentencePairClassification`  |    100.0   |    100.0   |   2    | bert-base-uncased            |
    | `BertCapsuleNetwork`                 |    100.0   |    100.0   |   5    | bert-base-uncased            |

- `GermanYelp_OpinionPolarity`

    |                 Model                |  Micro-F1  |  Macro-F1  | Epochs |   Pretrained Model Name      |
    | :----------------------------------- | :--------: | :--------: | :----: | :--------------------------- |
    | `BertForEntityClassification`        |    91.3    |    90.3    |   14   |  bert-base-german-cased      |
    | `BertForEntityClassification`        |  **94.7**  |  **94.1**  |   8    |  bert-base-german-cased-yelp |
    | `BertForSentencePairClassification`  |    92.4    |    91.5    |   7    |  bert-base-german-cased      |
    | `BertForSentencePairClassification`  |    93.7    |    93.0    |   19   |  bert-base-german-cased-yelp |
    | `BertCapsuleNetwork`                 |    91.4    |    90.3    |   4    |  bert-base-german-cased      |
    | `BertCapsuleNetwork`                 |    92.7    |    92.0    |   12   |  bert-base-german-cased-yelp |

- `GermanYelp_AspectPolarity`

    |                 Model                |  Micro-F1  |  Macro-F1  | Epochs |   Pretrained Model Name      |
    | :----------------------------------- | :--------: | :--------: | :----: | :--------------------------- |
    | `BertForEntityClassification`        |    88.7    |    87.4    |   7    |  bert-base-german-cased      |
    | `BertForEntityClassification`        |  **92.5**  |  **91.4**  |   18   |  bert-base-german-cased-yelp |
    | `BertForSentencePairClassification`  |    90.0    |    88.6    |   6    |  bert-base-german-cased      |
    | `BertForSentencePairClassification`  |    91.2    |    90.3    |   15   |  bert-base-german-cased-yelp |
    | `BertCapsuleNetwork`                 |    89.2    |    88.0    |   20   |  bert-base-german-cased      |
    | `BertCapsuleNetwork`                 |    92.1    |    91.1    |   15   |  bert-base-german-cased-yelp |
