# pyproject-base

following development of [uv](https://docs.astral.sh/uv/), which aims to likely replace this whole workflow

one of the most interesting aspects to me would be having the same commands multiplatform (ex. *nix `pyenv` vs Windows `py` launcher)

also following controversies (similarly to [ruff](https://docs.astral.sh/ruff/)'s)

#

rename folder `python/pyproject_base/` to `python/<new-project-name>`
#
in `pyproject.toml`
 - amend occurencies of `pyproject_base`
 - amend metadata
    - version of `requires-python`
    - `authors`
    - `classifiers`
 - verify LSPs and linters settings
#
amend 
#
verify python version in `Makefile`
#
amend `README.md` and `LICENSE`
#

# References

[pyproject dynamic optional-dependencies](https://stackoverflow.com/a/76771725/15446311)

[pip-tools constraint optional dependencies](https://github.com/jazzband/pip-tools/issues/1020)


