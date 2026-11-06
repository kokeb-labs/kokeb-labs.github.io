# Projects

Every repository is public, MIT licensed and checked by the same CI.

| Repository | What it is | Documentation |
| --- | --- | --- |
| [`ci-tools`](https://github.com/kokeb-labs/ci-tools) | Reusable GitHub Actions workflows, lint configurations and the documentation theme every repository uses | [Site](https://kokeb-labs.github.io/ci-tools/) |
| [`espidf-tools`](https://github.com/kokeb-labs/espidf-tools) | Build, flash and setup scripts for ESP-IDF projects, driven by one `app_config.yml` | [Site](https://kokeb-labs.github.io/espidf-tools/) |
| [`driver-template`](https://github.com/kokeb-labs/driver-template) | Template for a new chip driver or library: code, host tests, an ESP32 example, docs and CI | [README](https://github.com/kokeb-labs/driver-template#readme) |
| [`.github`](https://github.com/kokeb-labs/.github) | Organisation profile, community files, settings as code and the brand | [README](https://github.com/kokeb-labs/.github#readme) |

## Coming next

Chip drivers (`driver-<chip>`) and `kb-core`, the shared utilities, RTOS wrappers, interfaces and handlers, are
next. The [roadmap](roadmap.md) has the order.

## Boards

[HardFOC](https://github.com/hardfoc) is a family of motor-control boards built on these drivers and tools. It keeps
its own organisation; Kokeb Labs holds the parts that work on any board.
