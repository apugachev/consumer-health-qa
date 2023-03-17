# Consumer Health Question Answering Using Off-the-shelf Components

Source code and files for *Consumer Health Question Answering Using Off-the-shelf Components* [[Paper](https://webis.de/publications.html?q=pugachev_2023)] accepted on [ECIR 2023 Conference](https://ecir2023.org/home.html)

- `data`: 
  - raw xml data (`search_topics` folder)
  - 113 test questions (`data_to_process.csv`)
  - results from retrieval stage

- `retrieval`: scripts for pipeline's retrieval stage (Evidence Search)

- `experiments`: notebooks for QA models inference, scores aggregation and metrics calculation (Question Answering)
- `finetune`: notebook for fine-tuning Roberta Large pre-trained model on BoolQ dataset
- `statistics`: notebooks for statistics calculation (see Table 2, columns "Hits" and "#0")



The pre-trained BioLinkBERT models used for expreiments can be found [here](https://worksheets.codalab.org/worksheets/0x7a6ab9c8d06a41d191335b270da2902e).

Citation:

```
@InProceedings{pugachev:2023,
  address =                  {Berlin Heidelberg New York},
  author =                   {Alexander Pugachev and Ekaterina Artemova and Alexander Bondarenko and Pavel Braslavski},
  booktitle =                {Advances in Information Retrieval. 45th European Conference on IR Research (ECIR 2023)},
  month =                    apr,
  publisher =                {Springer},
  series =                   {Lecture Notes in Computer Science},
  site =                     {Dublin, Ireland},
  title =                    {{Consumer Health Question Answering Using Off-the-shelf Components}},
  year =                     2023
}
```

