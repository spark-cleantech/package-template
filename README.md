# Spark Package Template

This package is developed to ease development of Spark-Cleantech packages : it helps you create a
new package with already pre-configured tests & linting & documentation (see Features)

## Usage : create a new package

### 1. Decide whether the package will need a dedicated environment

For large projects it is recommended to use an isolated environment:

```
conda create -n MY_PACKAGE -c conda-forge python=3.11 cruft make -y
conda activate MY_PACKAGE
```

For smaller projects (analysis tools, etc), it is recommended to use
a common environment `spy` (Spark Python)

```
conda activate spy
```

If you create an isolated environment :

create a new conda environment (e.g. `MY_PACKAGE`) with Python 3.11,
cruft and make, then create the package:

```
cruft create https://github.com/spark-cleantech/package-template
```

answer the configuration questions or accept the defaults when in doubt.

Create the git repo and add the pre-commit git hooks:

```
cd MY_PACKAGE
git init
git add .
git commit -m "Initial commit of the package boilerplate"
```

Go to GitHub, click + "[make a new repository](https://github.com/organizations/spark-cleantech/repositories/new)", call it the same thing
as your cookiecutter folder (e.g. `MY_PACKAGE`). Add no licence nor README ;
keep the repo Private.

Attach an empty remote repository and push the skeleton package:

```
git branch -M main
git remote add origin git@github.com:spark-cleantech/MY_PACKAGE.git
git push --set-upstream origin main
```

To setup the package and its dependecies run:

```
make conda-env-update
conda activate MY_PACKAGE
pre-commit install
pip install -e . --no-deps
```

If using Windows, `make` is not available by default. Either install it
([for instance with Chocolatey](https://stackoverflow.com/questions/32127524/how-to-install-and-use-make-in-windows)),
or open the [Makefile](./Makefile) and execute the lines therein manually.

Finally to run pre-commit, pytest, and mypy on the newly created package run:

```
make
```

To update the boilerplate to the latest template execute:

```
make template-update
```

## Features

Alpha stage:

- pre-commit hooks
  - various linters
  - ruff
- version with setuptools-scm-git
- copyright license
- GitHub Actions
  - unit-tests (py3.11)
  - pre-commit
  - build documentation
  - static type check
- Makefile
- gitignore
- auto template update via cruft
- add documentation skeleton (with sphinx / myst)

Here is an example of package generated :

- https://github.com/spark-cleantech/test9

## License

```
Copyright (C) Spark Cleantech SAS (SIREN 909736068) - All Rights Reserved
Unauthorized copying of this file, via any medium is strictly prohibited
Proprietary and confidential
Written by Erwan Pannier <erwan.pannier@spark-cleantech.eu>, March 2024
```

## Credits

Originally based on Cookiecutter template at https://github.com/ecmwf-projects/cookiecutter-conda-package,
distributed under Apache Licence. Licence was changed after the fork.
