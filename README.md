# Consumer Health Question Answering Using Off-the-shelf Components

Source code and files for *Consumer Health Question Answering Using Off-the-shelf Components* paper accepted on [ECIR 2023 Conference](https://ecir2023.org/home.html)

- `data`: 
  - raw xml data (`search_topics` folder)
  - 113 test questions (`data_to_process.csv`)
  - results from retrieval stage

- `retrieval`: scripts for pipeline's retrieval stage (Evidence Search)

- `experiments`: notebooks for QA models inference, scores aggregation and metrics calculation (Question Answering)
- `finetune`: notebook for fine-tuning Roberta Large pre-trained model on BoolQ dataset
- `statistics`: notebooks for statistics calculation (see Table 2, columns "Hits" and "#0")



The pre-trained BioLinkBERT models used for expreiments can be found [here](https://worksheets.codalab.org/worksheets/0x7a6ab9c8d06a41d191335b270da2902e).



