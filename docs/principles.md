---
description: The rules every Kokeb Labs driver and repository follows, and why.
---

# How we build

## A driver never touches the SDK

A driver is the chip's datasheet turned into C++: registers, timing, modes and errors. Everything that depends on
your MCU sits behind a small port class that you write, and the driver only calls its hooks.

| The driver owns | Your port owns |
| --- | --- |
| Register framing, reset and chip-ID checks, conversions, CRCs | Bringing the bus up, moving bytes, optional GPIO, delay and log hooks |
| Units, ranges and `Config` presets with datasheet defaults | Pins, clocks, DMA, locking, which SPI or I2C peripheral |

The port derives from the driver's interface with CRTP (`class MyPort : public chip::SpiInterface<MyPort>`) and a
C++20 concept checks every required hook at compile time. There are no virtual calls, so the compiler can
inline the port into the driver.

## Predictable on small MCUs

- **No exceptions, no heap, no RTTI.** Every call returns `Result<T>`: a value, or an `Error` that says what went
  wrong (`Bus`, `Timeout`, `DeviceIdMismatch`, chip-specific faults).
- **Nothing happens in a constructor.** `Initialize()` does the first I/O, so you decide when the bus is touched.
- **Bounded waits.** A driver never blocks forever on a busy flag.

## Brand-free

A driver is named after its chip, not after a product: repository `driver-<chip>`, namespace `<chip>::`. A product's
pin map or modes never go into a shared repository.

| Kind of "specific" | Example | Where it lives |
| --- | --- | --- |
| Chip-specific | the registers of one sensor | that chip's driver |
| MCU-specific | an ESP-IDF SPI port | `interfaces/mcu/<family>/` in kb-core, built only for that family |
| Product-specific | one product's pin map or modes | the product's own repository, through extension points |

## Tested without hardware

Every driver builds and runs its tests on the host with CMake and `ctest`: a simulated chip answers like the real
one, error paths are forced, and compile-fail tests check that a broken port does not compile. Hardware tests are
labelled `needs-hardware` and `hardware-verified` on pull requests.

## The same checks in every repository

| Check | What it catches |
| --- | --- |
| Strict docs build, link check, figure and generated-table drift | Broken links, stale diagrams, docs that disagree with the code |
| Host build and tests, clang-tidy, cppcheck | Bugs, undefined behaviour, the port contract |
| clang-format, markdownlint, yamllint | Style drift |
| DCO sign-off, required files, MIT licence | Provenance and licensing |
| `CI gate` | One required check that passes only when everything else did |

## Supply-chain hygiene

Every third-party GitHub Action is pinned to a commit SHA on a real release tag and reviewed before it is allowed
in the organisation; tools without a trusted action are downloaded from their own release and checked against a
pinned SHA-256. Dependabot keeps the pins current. Secret scanning with push protection, Dependabot alerts and
CodeQL are on for every repository.

## Licence and sign-off

Everything is MIT licensed, `Copyright (c) 2026 The Kokeb Labs Authors`. There is no CLA: you sign off each commit
(`git commit -s`) to certify the [Developer Certificate of Origin](https://developercertificate.org/).
