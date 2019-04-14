Position-aware Attention RNN Model for Relation Extraction
=========================

## Requirements

- Python 3
- PyTorch 0.3.1
- ./dataset/semeval or ./dataset/tacred
- ./dataset/glove/glove.840B.300d.txt

## Preparation

```
python prepare_vocab.py dataset/semeval dataset/vocab --glove_dir dataset/glove
```

## Training

```
python train.py --train_dir dataset/semeval/train-0.3.json --dev_dir dataset/semeval/dev.json --vocab_dir dataset/vocab --id 00 --info "Position-aware attention model"
```

## Evaluation

```
python eval.py saved_models/00 --eval_dir dataset/semeval/dev.json
```
