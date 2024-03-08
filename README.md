 # Autoregressive Language Model Fine-tuned with Instruction-Tuning and RLHF

This code demonstrates how to fine-tune an autoregressive language model using instruction-tuning and reinforcement learning from human feedback (RLHF). The model is trained on a dataset of human-written text and then fine-tuned on a smaller dataset of instructions and human feedback. The fine-tuned model can then be used to generate text that is more accurate, factual, thoughtful, and nuanced.

## Prerequisites

To run this code, you will need the following:

* A GPU with at least 4GB of memory
* Python 3.6 or later
* PyTorch 1.0 or later
* Transformers 4.0 or later

## Installation

To install the required dependencies, run the following command:

```
pip install -r requirements.txt
```

## Data

The dataset used to train the model is the WikiText-2 dataset, which consists of over 100 million tokens of English text. The dataset is available for download from the following link:

[WikiText-2 dataset](https://www.cs.toronto.edu/~rkiros/wikitext-2/)

The dataset used to fine-tune the model is a smaller dataset of instructions and human feedback. The dataset is available for download from the following link:

[Instruction-tuning and RLHF dataset](https://github.com/huggingface/transformers/tree/master/examples/language-modeling/instruction-tuning-and-rlhf)

## Training

To train the model, run the following command:

```
python train.py --model_name_or_path [path to pre-trained model] --train_data [path to training data] --output_dir [path to output directory]
```

The training process will take several hours.

## Evaluation

To evaluate the model, run the following command:

```
python evaluate.py --model_name_or_path [path to fine-tuned model] --eval_data [path to evaluation data] --output_dir [path to output directory]
```

The evaluation process will take several minutes.

## Usage

To use the fine-tuned model, run the following command:

```
python generate.py --model_name_or_path [path to fine-tuned model] --input_text [input text] --output_file [path to
<img src="https://img.shields.io/badge/PYTHON-black?style=for-the-badge&logo=python&logoColor=gold"/>
