pyri
====

Pyri is a tool that can be used to import refractive indexes and extinction
coefficients for different materials at different wavelengths. This data can then
be used for different applications like simulating light interaction's with
particules. All the data comes from RefractiveIndex.INFO.

Throughout the library, a few key acronyms are used:

* wl: wavelength
* ri: refractive index
* ec: extinction coefficient

Pyri includes functions that let you import experimental data or Sellmeier's
formula for different materials and store it locally. This data can then easily
be called and used.

Below is an example of how to import new experimental data and then how to
use it. For more examples, please visit the Examples section of the documentation.
