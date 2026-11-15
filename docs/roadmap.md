---
description: What Kokeb Labs has done, what is in progress and what comes next, with no dates.
---

# Roadmap

This is where things stand, in order. We don't publish dates: a step moves to done when its evidence exists.

<div class="kb-steps" markdown>

1. **Foundations** <span class="kb-badge kb-badge--teal">Done</span>
   The organisation and its settings as code, `ci-tools` v1, `espidf-tools` v1, `driver-template`, the handbook and
   the documentation platform, and this portal.
2. **Chip drivers** <span class="kb-badge kb-badge--teal">22 release candidates</span>
   22 public drivers, each tagged `v0.1.0-rc.1` with host tests, a fuzzer, MISRA C++:2023 checks, an ESP32 example and
   a documentation site, in the [kokeb-labs-drivers](https://github.com/kokeb-labs-drivers) organisation. The
   [driver request pipeline](contributing.md#request-a-driver) decides which chip comes next.
3. **Hardware validation** <span class="kb-badge kb-badge--amber">Next</span>
   Every driver is at level H0 today. A driver moves to H1 when a defined bench rig has run its example with the logs
   kept, and to H2 when a hardware engineer signs off. A release candidate that passes the bench is tagged again, on
   the same commit, as its release. Help with a bench is welcome: see [contributing](contributing.md).
4. **kb-core and MCU ports** <span class="kb-badge kb-badge--amber">In development</span>
   The framework that joins drivers to interfaces, handlers and an RTOS layer, and ports for ESP32 and STM32. These
   repositories are not public yet. Drivers stay usable without them.
5. **Open boards** <span class="kb-badge kb-badge--amber">Started</span>
   Open KiCad boards built around the drivers, in the
   [kokeb-labs-open-boards](https://github.com/kokeb-labs-open-boards) organisation, each traced from its needs to its
   test results. `board-template`, the parts library and the circuit-block library exist; the first board, a BMP581
   breakout, is at concept stage and nothing has been built or verified yet.
6. **Tools for users**
   A command-line tool, a board configurator and a documentation hub. Planned: nothing to try yet.

</div>

## Language standard

Drivers target C++20 today. The standard will move up under the [stated policy](principles.md#language-standard)
when every compiler we ship for supports it and the checks are ready for it, not on a date.

## Follow along

- **Releases:** watch a repository on GitHub (Watch, Custom, Releases).
- **Discussions:** questions and ideas in the [kokeb-labs discussions](https://github.com/kokeb-labs/.github/discussions)
  and the [drivers discussions](https://github.com/kokeb-labs-drivers/.github/discussions).
- **Driver requests** shape step 2: [ask for a chip](contributing.md#request-a-driver).
