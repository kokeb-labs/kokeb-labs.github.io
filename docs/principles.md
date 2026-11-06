# How we build

## Brand-free drivers

A driver is named after its chip, not after a product: repository `driver-<chip>`, namespace `<chip>::`. It never
calls an MCU SDK. It calls a few hooks (transfer, GPIO, delay) on a port class you write, checked at compile time
with no virtual calls, so the same driver runs on ESP-IDF, STM32, Zephyr, Linux and on the host for tests.

## Three kinds of "specific"

| Kind | Example | Where it lives |
| --- | --- | --- |
| Chip-specific | the registers of one sensor | in that chip's driver |
| MCU-specific | an ESP-IDF SPI port | under `interfaces/mcu/<family>/`, built only for that family |
| Product-specific | one product's pin map or modes | never in a shared repository; products use extension points |

## Every repository, the same checks

- A strict documentation build, figure and generated-table drift checks, link checks.
- C++ builds and host tests, clang-tidy and cppcheck over the same compile database.
- A DCO sign-off on every commit, an MIT licence and the required root files.
- One required check, `CI gate`, and every third-party action pinned to a commit SHA.

## Licence and sign-off

Everything is MIT licensed, `Copyright (c) 2026 The Kokeb Labs Authors`. There is no CLA: you sign off each commit
(`git commit -s`) to certify the [Developer Certificate of Origin](https://developercertificate.org/).
