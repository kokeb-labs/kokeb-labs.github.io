# kokeb-labs.github.io

The Kokeb Labs portal, published at <https://kokeb-labs.github.io/>: what the organisation is, its projects, how
it builds software, the roadmap and how to contribute. Each project keeps its own documentation site under
`https://kokeb-labs.github.io/<repo>/`.

## Editing

Pages live in `docs/`, their order in `docs/.nav.yml`, figures in `docs/diagrams/figures/`. Preview locally:

```bash
pip install "kokeb-mkdocs-theme @ git+https://github.com/kokeb-labs/ci-tools@v1#subdirectory=packages/kokeb-mkdocs-theme"
kokeb-docs figures
mkdocs serve
```

A push to `main` publishes the site; pull requests build and check it without publishing. Sign off every commit
(`git commit -s`).

## Licence

MIT, see [LICENSE](LICENSE).
