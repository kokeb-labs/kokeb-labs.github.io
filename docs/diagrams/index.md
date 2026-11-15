# Figures

<!-- Written by kokeb-docs figures from docs/diagrams/figures/*.py. Do not edit by hand. -->

Every figure on this site is drawn by a Python module from facts extracted from the code, so it is rebuilt,
not redrawn, when the code changes. CI runs `kokeb-docs figures --check` and fails when a
committed figure no longer matches the code. Each figure below lists the files it is drawn from.

## What each assurance level asks for

<!-- figure: assurance-levels -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assurance-levels.dark.svg">
  <img src="assurance-levels.svg"
    alt="Matrix of the checks and evidence asked for at the standard, high and safety assurance levels, from
    lint and host tests for every repository to a signed evidence package at safety.">
</picture>
<!-- /figure -->

Hardware description: [`docs/model/assurance-levels.matrix.yml`](../model/assurance-levels.matrix.yml)

Drawn from:

- [`docs/model/assurance-levels.matrix.yml`](../model/assurance-levels.matrix.yml)

## What stands between a datasheet and a release candidate

<!-- figure: driver-gates -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="driver-gates.dark.svg">
  <img src="driver-gates.svg"
    alt="Pipeline in four columns in which a public datasheet and an independent chip model feed the CI
    checks, an independent review round follows, and a release candidate with a stated hardware level
    comes out.">
</picture>
<!-- /figure -->

Hardware description: [`docs/model/driver-gates.pipeline.yml`](../model/driver-gates.pipeline.yml)

Drawn from:

- [`docs/model/driver-gates.pipeline.yml`](../model/driver-gates.pipeline.yml)

## Hardware validation levels

<!-- figure: hardware-levels -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="hardware-levels.dark.svg">
  <img src="hardware-levels.svg"
    alt="State machine of the three hardware validation levels H0, H1 and H2, from a host model only, to a
    bench rig run with logs kept, to a hardware engineer's sign-off.">
</picture>
<!-- /figure -->

Hardware description: [`docs/model/hardware-levels.state.yml`](../model/hardware-levels.state.yml)

Drawn from:

- [`docs/model/hardware-levels.state.yml`](../model/hardware-levels.state.yml)

## One measurement through a driver

<!-- figure: one-measurement -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="one-measurement.dark.svg">
  <img src="one-measurement.svg"
    alt="Sequence of a driver start and one measurement, in which the firmware starts the driver, the driver
    checks the chip through the port and returns a result, and a later call returns a value or an error
    code.">
</picture>
<!-- /figure -->

Hardware description: [`docs/model/one-measurement.seq.yml`](../model/one-measurement.seq.yml)

Drawn from:

- [`docs/model/one-measurement.seq.yml`](../model/one-measurement.seq.yml)

## From a request to a release candidate

<!-- figure: request-pipeline -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="request-pipeline.dark.svg">
  <img src="request-pipeline.svg"
    alt="State machine of a driver request with the stages Requested, Triaged, Datasheet acquired, In design,
    Building, In review and Released, and a Declined end state.">
</picture>
<!-- /figure -->

Hardware description: [`docs/model/request-pipeline.state.yml`](../model/request-pipeline.state.yml)

Drawn from:

- [`docs/model/request-pipeline.state.yml`](../model/request-pipeline.state.yml)

## How Kokeb Labs fits together

<!-- figure: system-map -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="system-map.dark.svg">
  <img src="system-map.svg"
    alt="System map: your firmware calls chip drivers, directly or through kb-core when it is released; a
    driver reaches the chip only through an MCU port; beside this path, the templates, ci-tools, the
    handbook and driver-requests start, check and release every repository.">
</picture>
<!-- /figure -->

Figure module: [`docs/diagrams/figures/system-map.py`](../../docs/diagrams/figures/system-map.py)
