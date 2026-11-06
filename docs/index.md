---
hide:
  - navigation
  - toc
---

<div class="kb-hero" markdown>
<span class="kb-kicker">Open-source embedded software</span>

# Kokeb Labs

<p>Open, brand-free drivers, firmware building blocks and tools for embedded systems. Every chip driver works on
any MCU through a small port you write, builds and tests on a laptop, and ships with documentation and CI.
Everything is MIT licensed.</p>

[Browse the projects](projects.md){ .md-button .md-button--primary }
[How we build](principles.md){ .md-button }
[GitHub](https://github.com/kokeb-labs){ .md-button }
</div>

<!-- figure: ecosystem -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="diagrams/ecosystem.dark.svg">
  <img src="diagrams/ecosystem.svg"
    alt="Layer diagram: your firmware calls kb-core, which calls brand-free chip drivers, which reach the
    hardware only through an MCU port; driver-template, espidf-tools and ci-tools start, build and check
    every repository.">
</picture>
<!-- /figure -->

## Start here

<div class="grid cards" markdown>

- **Write a driver**

    ---

    One command gives a new chip driver with code, host tests, an ESP32 example, documentation and CI.

    [driver-template](https://github.com/kokeb-labs/driver-template)

- **Build ESP-IDF projects**

    ---

    Build, flash and monitor every app of a multi-app project from one `app_config.yml`, on your machine and
    in CI.

    [espidf-tools docs](https://kokeb-labs.github.io/espidf-tools/)

- **Reuse our CI**

    ---

    Reusable workflows for C++ checks, firmware builds, documentation sites and releases, pinned with `@v1`.

    [ci-tools docs](https://kokeb-labs.github.io/ci-tools/)

- **Contribute**

    ---

    Sign off your commits, open a pull request, and CI tells you what is missing.

    [Contributing](contributing.md)

</div>
