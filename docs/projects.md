---
description: Every Kokeb Labs repository, what it is for, who uses it and where its documentation lives.
---

# Projects

Every repository is public, MIT licensed and checked by the same CI: a strict docs build, lint, the DCO sign-off
and one required check, `CI gate`.

## driver-template <span class="kb-badge kb-badge--teal">Ready</span>

**Start a new chip driver or library in one command.** Create a repository from the template, run
`python3 tools/setup.py`, answer a few questions (chip name, bus, description), and you get:

- A C++20 driver skeleton for an SPI, I2C or UART chip, or a header-only library, with the port contract checked
  by a concept at compile time.
- Host tests against a simulated chip, compile-fail tests for the port contract, and an optimised-build check.
- A host example that runs on your PC, and an ESP32 example built by `espidf-tools`.
- A documentation site with the layer figure drawn from your headers, and the full CI.

[Repository](https://github.com/kokeb-labs/driver-template){ .md-button .md-button--primary }
[Using the template](https://github.com/kokeb-labs/driver-template/blob/main/docs/template.md){ .md-button }

## espidf-tools <span class="kb-badge kb-badge--teal">v1</span>

**Build, flash and monitor every app of a multi-app ESP-IDF project.** List the apps, ESP-IDF versions, build types
and target once in `app_config.yml`; the same scripts run on your machine and in CI.

- `build_app.sh` and `flash_app.sh` for any app, build type and ESP-IDF version, each built into its own folder.
- `manage_idf.sh` installs and switches ESP-IDF versions; serial-port detection, logs and tab completion included.
- `generate_matrix.py` turns `app_config.yml` into a CI matrix, so CI builds exactly what you build locally.

[Documentation](https://kokeb-labs.github.io/espidf-tools/){ .md-button .md-button--primary }
[Repository](https://github.com/kokeb-labs/espidf-tools){ .md-button }

## ci-tools <span class="kb-badge kb-badge--teal">v1</span>

**The CI and documentation platform every repository uses.** Short caller workflows pin `@v1` and get fixes
without breaking changes.

- C++ build and host tests, clang-format, clang-tidy and cppcheck over one compile database.
- ESP-IDF firmware builds across versions and build types with a size report, and releases that ship the exact
  firmware CI built.
- The documentation theme and figure kit used on this site: light and dark from one layout, contrast-checked, and
  redrawn from the code so a figure can't go stale.
- Every third-party action pinned to a commit SHA and reviewed before it is allowed.

[Documentation](https://kokeb-labs.github.io/ci-tools/){ .md-button .md-button--primary }
[Repository](https://github.com/kokeb-labs/ci-tools){ .md-button }

## .github

The organisation's profile, community files (contributing, code of conduct, security policy), the brand, and the
settings of every repository kept as code.

[Repository](https://github.com/kokeb-labs/.github){ .md-button }

## Coming next <span class="kb-badge kb-badge--amber">Next</span>

- **Chip drivers**, one repository per chip, named `driver-<chip>`, moving in from HardFOC. They live in their own
  organisation, [kokeb-labs-drivers](https://github.com/kokeb-labs-drivers); each has its docs site at
  `https://kokeb-labs-drivers.github.io/driver-<chip>/`.
- **kb-core**: MCU interfaces with ESP32, STM32 and host ports, a small RTOS layer, utilities, and the handlers that
  join drivers to the interfaces.

See the [roadmap](roadmap.md) for the order, or [request a driver](https://github.com/kokeb-labs/.github/issues/new?template=driver-request.yml).

## Boards

[HardFOC](https://github.com/hardfoc) is a family of motor-control boards built on these drivers and tools. It keeps
its own organisation; Kokeb Labs holds the parts that work on any board.
