---
description: How to contribute to Kokeb Labs, what makes a good first contribution, and how to report a vulnerability.
---

# Contributing

## Good first contributions

| You can | Where |
| --- | --- |
| Fix a doc, a typo or a broken example | Any repository; the docs live in `docs/` |
| Ask for a driver, or say which chip you need most | [Driver request](https://github.com/kokeb-labs/.github/issues/new?template=driver-request.yml) |
| Write a driver for a chip you know | Start from [`driver-template`](https://github.com/kokeb-labs/driver-template) and open a [discussion](https://github.com/kokeb-labs/.github/discussions) first |
| Write a port for an MCU we don't cover yet | Open a [discussion](https://github.com/kokeb-labs/.github/discussions); ports go in `kb-core` |
| Report a bug | The repository's issues, with the bug form |

Issues labelled **good first issue** are a good start.

## How a change gets in

<div class="kb-steps" markdown>

1. Fork the repository and create a branch.
2. Make the change, with its docs and tests in the same pull request.
3. Sign off every commit: `git commit -s`. CI fails a pull request with a commit that has no matching
   `Signed-off-by:` line.
4. Open the pull request. `CI gate` runs every check and tells you what is missing; a maintainer reviews.

</div>

Workflows from a first-time contributor's fork wait for a maintainer's approval before they run.

## Security

Report a vulnerability privately through the repository's **Security** tab ("Report a vulnerability"), never in a
public issue. The [security policy](https://github.com/kokeb-labs/.github/blob/main/SECURITY.md) says what happens
next.

## Community

Be kind and specific: the [code of conduct](https://github.com/kokeb-labs/.github/blob/main/CODE_OF_CONDUCT.md)
applies everywhere. Full details are in the
[contributing guide](https://github.com/kokeb-labs/.github/blob/main/CONTRIBUTING.md).
