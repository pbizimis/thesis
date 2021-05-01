# Code Used for Training

## StyleGAN2-ADA Training

The stylegan2ada.ipynb notebook shows a training process for one StyleGAN2-ADA model.

```
@inproceedings{Karras2020ada,
  title     = {Training Generative Adversarial Networks with Limited Data},
  author    = {Tero Karras and Miika Aittala and Janne Hellsten and Samuli Laine and Jaakko Lehtinen and Timo Aila},
  booktitle = {Proc. NeurIPS},
  year      = {2020}
}
```

## NCSN++ Training

The ncsnpp.ipynb notebook shows the training process of the NCSN++ model, which is trained for the thesis. The score_sde_pytorch repository is a fork of the offical repository that includes the configuration files that were used.

Configuration adaptations were based on recommendations from the author:
- https://github.com/yang-song/score_sde/issues/2
- https://github.com/yang-song/score_sde_pytorch/issues/1

```
@inproceedings{
  song2021scorebased,
  title={Score-Based Generative Modeling through Stochastic Differential Equations},
  author={Yang Song and Jascha Sohl-Dickstein and Diederik P Kingma and Abhishek Kumar and Stefano Ermon and Ben Poole},
  booktitle={International Conference on Learning Representations},
  year={2021},
  url={https://openreview.net/forum?id=PxTIG12RRHS}
}
```

Furthermore, the recommended sigma_max value was calculated by using the AdversarialConsistentScoreMatching repository. The fork contains the configuration for the custom dataset of the thesis. The ncsnpp_sigma_max_calculation.ipynb notebook shows the calculation process.

```
@inproceedings{
  jolicoeur-martineau2021adversarial,
  title={Adversarial score matching and improved sampling for image generation},
  author={Alexia Jolicoeur-Martineau and R{\'e}mi Pich{\'e}-Taillefer and Ioannis Mitliagkas and Remi Tachet des Combes},
  booktitle={International Conference on Learning Representations},
  year={2021},
  url={https://openreview.net/forum?id=eLfqMl3z3lq}
}
```