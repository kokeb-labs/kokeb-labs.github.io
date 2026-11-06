# Figures

<!-- Written by kokeb-docs figures from docs/diagrams/figures/*.py. Do not edit by hand. -->

Every figure on this site is drawn by a Python module from facts extracted from the code, so it is rebuilt,
not redrawn, when the code changes. CI runs `kokeb-docs figures --check` and fails when a
committed figure no longer matches the code. Each figure below lists the files it is drawn from.

## From your firmware to the chip

<!-- figure: ecosystem -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="ecosystem.dark.svg">
  <img src="ecosystem.svg"
    alt="Layer diagram: your firmware calls kb-core, which calls brand-free chip drivers, which reach the
    hardware only through an MCU port; driver-template, espidf-tools and ci-tools start, build and check
    every repository.">
</picture>
<!-- /figure -->

Figure module: [`docs/diagrams/figures/ecosystem.py`](../../docs/diagrams/figures/ecosystem.py)
