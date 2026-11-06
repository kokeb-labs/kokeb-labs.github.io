"""How the Kokeb Labs pieces fit together, from your firmware down to the chip.

Reads: Top to bottom, each arrow is a call. Your firmware calls the kb-core handlers, which call chip drivers
(driver-<chip>), which reach the hardware only through an MCU port, yours or a ready one from kb-core; the port drives
the chip on your board. Dashed cards are planned. On the right, the tools that every repository uses: driver-template
starts a driver, espidf-tools builds and flashes ESP-IDF projects, ci-tools checks, documents and releases them all.
"""

from kokeb_mkdocs_theme.figkit import Fig


def build(_data):
    f = Fig(
        "ecosystem",
        "From your firmware to the chip",
        alt="Layer diagram: your firmware calls kb-core, which calls brand-free chip drivers, which reach the "
        "hardware only through an MCU port; driver-template, espidf-tools and ci-tools start, "
        "build and check every repository.",
        width=1200,
        kicker="Kokeb Labs",
        subtitle="Each arrow is a call. Everything above the port runs on any MCU and on a laptop.",
        profile="overview",
        legend=[("teal", "yours"), ("brand", "Kokeb Labs"), ("slate", "hardware"), ("~solid", "calls")],
    )
    W = f.body_w
    side, gap, row = 330, 48, 64
    M = W - side - gap
    nx = M + gap

    fw = f.card(0, 0, M, "Your firmware", ["a product, a board or a test bench"], tone="teal", accent=True)
    core = f.card(0, fw.b + row, M, "kb-core", ["handlers, interfaces, RTOS wrappers, utilities"], tone="brand",
                  dashed=True, tag="planned")
    drv = f.card(0, core.b + row, M, "Chip drivers", ["driver-<chip>: one per chip, no SDK calls"], tone="brand",
                 dashed=True, tag="planned")
    port = f.card(0, drv.b + row, M, "MCU port", ["transfer, GPIO and delay: yours, or a ready one in kb-core"], tone="teal",
                  accent=True)
    chip = f.card(0, port.b + row, M, "The chip, on your board", ["SPI, I2C or UART"], tone="slate", accent=True)
    for a, b, verb in ((fw, core, "calls"), (core, drv, "calls"), (drv, port, "through its hooks"),
                       (port, chip, "bus transfers")):
        f.edge([(M / 2, a.b + 4), (M / 2, b.y - 4)], label=verb)

    top = core.y
    inner = f.region_inner_top(top)
    ch = 92
    tools = [
        ("driver-template", ["starts a driver"]),
        ("espidf-tools", ["builds and flashes"]),
        ("ci-tools", ["checks, documents, releases"]),
    ]
    y = inner
    for name, lines in tools:
        f.card(nx + 16, y, side - 32, name, lines, tone="brand", accent=True, h=ch)
        y += ch + 16
    f.region(nx, top, side, y - top + 2, "Tools for every repo", tone="brand")
    return f
