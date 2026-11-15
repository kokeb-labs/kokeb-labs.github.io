# kokeb-labs.github.io

The Kokeb Labs portal, published at <https://kokeb-labs.github.io/>: what the organisation is, its projects, how
it builds software, the roadmap and how to contribute. Each project keeps its own documentation site under
`https://kokeb-labs.github.io/<repo>/`.

## Editing

Pages live in `docs/`, their order in `docs/.nav.yml`. Figures are drawn with the figure kit of the theme package
(ci-tools 1.22.0 or later, which the `@v1` pin below includes): `docs/diagrams/figures/*.py` for the system map and
`docs/model/<id>.<kind>.yml` for the state, sequence, matrix and pipeline figures, with the outputs in
`docs/diagrams/`. Preview locally:

```bash
pip install "kokeb-mkdocs-theme @ git+https://github.com/kokeb-labs/ci-tools@v1#subdirectory=packages/kokeb-mkdocs-theme"
kokeb-docs figures
kokeb-docs check
mkdocs serve
```

After you change a `state` figure's model, run `kokeb-docs figkit layout <id>` once and commit the layout file (it
needs Graphviz).

A push to `main` publishes the site; pull requests build and check it without publishing. Sign off every commit
(`git commit -s`).

## Licence

MIT, see [LICENSE](LICENSE).
