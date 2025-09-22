# [ACL main 2025] PsyDial: A Large-scale Long-term Conversational Dataset for Mental Health Support

## The PsyDial Dataset

PsyDial is a semi-real, Chinese-language dataset created by reconstructing real-world, long-term counseling dialogues.

## Getting Started

`data`: the PsyDial (D4.json) dataset and the masked real-world dataset.

- `PsyDial-D0_m.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D0_m

- `PsyDial-D1.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D1
- `PsyDial-D2.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D2
- `PsyDial-D3.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D3
- `PsyDial-D4.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D4
- `PsyDial-D101.json`: https://huggingface.co/datasets/qiuhuachuan/PsyDial-D101

`model`: https://huggingface.co/qiuhuachuan/PsyDial-Pi4

`/code`: Contains the implementation of the RMRR method and evaluation scripts.

`cal_LDD.py`: the script to calculate the LDD.

## Citation

If you find this dataset valuable for your research, kindly cite it using the following BibTeX.

```BibTeX
@inproceedings{qiu-lan-2025-psydial,
    title = "{P}sy{D}ial: A Large-scale Long-term Conversational Dataset for Mental Health Support",
    author = "Qiu, Huachuan  and
      Lan, Zhenzhong",
    editor = "Che, Wanxiang  and
      Nabende, Joyce  and
      Shutova, Ekaterina  and
      Pilehvar, Mohammad Taher",
    booktitle = "Proceedings of the 63rd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers)",
    month = jul,
    year = "2025",
    address = "Vienna, Austria",
    publisher = "Association for Computational Linguistics",
    url = "https://aclanthology.org/2025.acl-long.1049/",
    doi = "10.18653/v1/2025.acl-long.1049",
    pages = "21624--21655",
    ISBN = "979-8-89176-251-0",
    abstract = "Dialogue systems for mental health counseling aim to alleviate client distress and assist individuals in navigating personal challenges. Developing effective conversational agents for psychotherapy requires access to high-quality, real-world, long-term client-counselor interaction data, which is difficult to obtain due to privacy concerns. Although removing personally identifiable information is feasible, this process is labor-intensive. To address these challenges, we propose a novel privacy-preserving data reconstruction method that reconstructs real-world client-counselor dialogues while mitigating privacy concerns. We apply the RMRR (Retrieve, Mask, Reconstruct, Refine) method, which facilitates the creation of the privacy-preserving PsyDial dataset, with an average of 37.8 turns per dialogue. Extensive analysis demonstrates that PsyDial effectively reduces privacy risks while maintaining dialogue diversity and conversational exchange. To fairly and reliably evaluate the performance of models fine-tuned on our dataset, we manually collect 101 dialogues from professional counseling books. Experimental results show that models fine-tuned on PsyDial achieve improved psychological counseling performance, outperforming various baseline models. A user study involving counseling experts further reveals that our LLM-based counselor provides higher-quality responses. Code, data, and models are available at https://github.com/qiuhuachuan/PsyDial, serving as valuable resources for future advancements in AI psychotherapy."
}
```
