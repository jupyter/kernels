# Jupyter Kernels

**To see the current status of known Jupyter kernels, visit the
[jupyter.org kernels page][kernels].**

> Kernels are processes that run interactive code in a particular programming
> language and return output to the user. Kernels also respond to tab
> completion and introspection requests - [jupyter.org](https://jupyter.org)

This repository is the home of the official integration state of the Jupyter
kernels ecosystem.

## How does it work?
Every night, we run an automated test suite of all the Jupyter kernels in the
Docker container that powers all the official Jupyter deployments, namely
[jupyter/base-notebook][jupyter/base-notebook].

The results of this are recorded, and displayed on the
[jupyter.org kernels page][kernels].

## Kernel _x_ isn't listed!
Kernel maintainers, or helpful users, can opt in to this by [creating a Pull
Request][contributing] on this repository.

[jupyter/base-notebook]: https://hub.docker.com/r/jupyter/base-notebook
[kernels]: https://jupyter.org/kernels
[contributing]: ./CONTRIBUTING.md
