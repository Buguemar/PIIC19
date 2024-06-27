# PIIC19 - Detección de Exoplanetas

### Caracterización y comprensión de los procesos en la detección de exoplanetas a través de la validación de modelos de aprendizaje automáticos. 

**Objetivo general:**  
Utilizando series de tiempo, en específico curvas de luz, proponemos automatizar la detección exoplanetas así como su caracterización y modelado a través de herramientas de aprendizaje automático.

**Objetivos específicos:**
* Diseñar e implementar un modelo supervisado que aprenda directamente de curvas de luz extensas en el dominio temporal.  
* Diseñar e implementar un modelo no supervisado que aprenda a imitar los proceso de la pipeline de Kepler directamente de curvas de luz.  
* Encontrar un modelo base, derivado de los propuestos, para realizar transfer learning sobre otros surveys de cuerpos transientes.  
* Generar datos sintéticos a través de un modelo probabilista no supervisado, validado con datos reales, de objetos transientes que no hayan podido ser estudiados en profundidad debido a limitaciones tecnológicas.


# :scroll: Source

* Regarding our work in imaging the light curves via Markov transition field ([obj1](./code/obj1))
  * :lock: [Final published version](https://doi.org/10.1016/j.ascom.2021.100461)
  * :unlock: [Preprint](https://www.researchgate.net/publication/350163853_Harnessing_the_power_of_CNNs_for_unevenly-sampled_light-curves_using_Markov_Transition_Field)
  * [Poster](https://github.com/fmenat/fmenat/blob/main/posters/2020_MTF.pdf)
* Regarding our work in unsupervised learning of a representation of light curves via variational auto-encoders ([obj4](./code/obj4))
  * :unlock: [Final published version](https://www.mdpi.com/2624-6120/2/4/42)
  * [Poster](https://github.com/fmenat/fmenat/blob/main/posters/2020_VAE.pdf)
  

# 🖊️ Citation

Bugueno, M., et al. "*Harnessing the power of CNNs for unevenly-sampled light-curves using Markov transition field.*" Astronomy and Computing 35 (2021): 100461.
```bibtex
@article{bugueno2021harnessing,
  title={Harnessing the power of CNNs for unevenly-sampled light-curves using Markov transition field},
  author={Bugueno, M and Molina, Gabriel and Mena, F and Olivares, P and Araya, Mauricio},
  journal={Astronomy and Computing},
  volume={35},
  pages={100461},
  year={2021},
  publisher={Elsevier}
}
```
> this is a reference to our work in imaging light curves via MTF.


Mena, Francisco, et al. "*On the Quality of Deep Representations for Kepler Light Curves Using Variational Auto-Encoders.*" Signals 2.4 (2021): 706-728.
```bibtex
@article{mena2021quality,
  title={On the quality of deep representations for Kepler light curves using variational auto-encoders},
  author={Mena, Francisco and Olivares, Patricio and Bugue{\~n}o, Margarita and Molina, Gabriel and Araya, Mauricio},
  journal={Signals},
  volume={2},
  number={4},
  pages={706--728},
  year={2021},
  publisher={MDPI}
}
```
> This is a reference to our work with variational auto-encoders
