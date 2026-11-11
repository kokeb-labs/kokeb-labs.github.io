---
description: What Kokeb Labs is building, in order, and how to follow along.
---

# Roadmap

<div class="kb-steps" markdown>

1. **Foundations** <span class="kb-badge kb-badge--teal">Done</span>
   The organisation and its settings as code, `ci-tools` v1, `espidf-tools` v1, `driver-template`, the documentation
   platform and this site.
2. **Chip drivers** <span class="kb-badge kb-badge--amber">Next</span>
   Drivers move in from HardFOC one chip at a time, renamed `driver-<chip>`, each with host tests, an ESP32 example
   and a docs site, in the [kokeb-labs-drivers](https://github.com/kokeb-labs-drivers) organisation.
3. **kb-core**
   One repository with `kb::utils`, `kb::rtos`, `kb::interfaces` and `kb::handlers`. Pick your MCU, RTOS and drivers
   in one CMake file; only what you pick is built.
4. **MCU ports**
   Ready-made ports under `interfaces/mcu/<family>/`, starting with ESP32, then STM32 and the host.
5. **HardFOC on Kokeb**
   The HardFOC motor-control boards build on these drivers and kb-core.
6. **Tools for users**
   A command-line tool, a board configurator and a documentation hub.

</div>

## Follow along

- **Releases:** watch a repository on GitHub (Watch, Custom, Releases).
- **Discussions:** questions and ideas in the [discussions](https://github.com/kokeb-labs/.github/discussions).
- **Driver requests** shape step 2: [ask for a chip](https://github.com/kokeb-labs/.github/issues/new?template=driver-request.yml).
