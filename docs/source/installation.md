# Installation

## Requirements

PyKale requires a Python version 3.6 or above. Before installing pykale, you should
- manually [install PyTorch](https://pytorch.org/get-started/locally/) matching your hardware first,
- if you will use APIs related to graphs, you need to manually install [PyTorch Geometric](https://github.com/rusty1s/pytorch_geometric) first following its [official instructions](https://github.com/rusty1s/pytorch_geometric#installation) and matching your PyTorch installation, and
- If [RDKit](https://www.rdkit.org/) will be used, you need to install it via `conda install -c conda-forge rdkit`.

## Pip install

Install PyKale using `pip` for the stable version:

```bash
pip install pykale  # for the core API and examples
```

## Install from source

Install from source for the latest version and/or development:

```sh
git clone https://github.com/pykale/pykale
cd pykale
pip install .  # for the core API and examples
pip install -e .[dev]  # editable install for developers including all dependencies
```

## Tests

For local unit tests on all `kale` API, you need to have PyTorch, PyTorch Geometric, and RDKit installed (see the top) and then run [pytest](https://pytest.org/) at the root directory:

```bash
pytest
```

You can also run pytest on individual module (see [pytest documentation](https://docs.pytest.org/en/6.2.x/)).
