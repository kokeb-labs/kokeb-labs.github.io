"""How the Kokeb Labs pieces fit together, from your firmware down to the chip, and the tooling beside them.

Reads: Top to bottom, each arrow is a call. Your firmware calls the chip drivers directly today, or through kb-core
when it is released; a driver reaches the chip only through the hooks of an MCU port, which is a short class you write
or a ready one for ESP32 or STM32; the port drives the chip on your board. Dashed cards are in development or at an
early stage. At the top right, the open boards your firmware can run on, built around the drivers. On the right, the
tooling and process every repository uses: driver-template starts a driver, board-template starts a board, ci-tools
checks, documents and releases them all, the handbook holds the rules the checks enforce, espidf-tools builds and
flashes ESP-IDF projects, and driver-requests takes the requests for new drivers.
"""

from kokeb_mkdocs_theme.figkit import Fig


def build(_data):
    f = Fig(
        "system-map",
        "How Kokeb Labs fits together",
        alt="System map: your firmware calls chip drivers, directly or through kb-core when it is released; a driver "
        "reaches the chip only through an MCU port; beside this path, the templates, ci-tools, the handbook and "
        "driver-requests start, check and release every repository.",
        width=1200,
        kicker="Kokeb Labs",
        subtitle="Each arrow is a call. Everything above the port runs on any MCU and on a laptop.",
        profile="overview",
        palette=2,
        legend=[("teal", "yours"), ("brand", "Kokeb Labs"), ("slate", "hardware"), ("~solid", "calls"),
                ("~dashed", "in development or early")],
    )
    W = f.body_w
    side, gap, row = 340, 48, 64
    M = W - side - gap
    nx = M + gap

    fw = f.card(0, 0, M, "Your firmware", ["a product, a board or a test bench"], tone="teal", accent=True)
    boards = f.card(nx, 0, side, "Open boards", ["KiCad boards built around the drivers, for your firmware to run on; concept stage"],
                    tone="brand", dashed=True, tag="early")
    core_w = M - 150
    core = f.card(0, fw.b + row, core_w, "kb-core",
                  ["framework with handlers, interfaces and RTOS wrappers"], tone="brand", dashed=True,
                  tag="in development")
    drv = f.card(0, core.b + row, M, "Chip drivers",
                 ["driver-<chip>: 22 public, release candidate 0.1.0-rc.1; no SDK calls"], tone="brand", accent=True)
    port = f.card(0, drv.b + row, M, "MCU port",
                  ["transfer, GPIO and delay hooks: a class you write, or an ESP32 or STM32 port (in development)"],
                  tone="teal", accent=True)
    chip = f.card(0, port.b + row, M, "The chip, on your board", ["SPI, I2C, UART, ADC or another bus"],
                  tone="slate", accent=True)
    f.connect(fw, core, "bottom", "top", at=0.35, bt=0.35, label="calls")
    f.connect(core, drv, "bottom", "top", at=0.35, bt=0.35, label="calls")
    # Today a driver is used on its own: an arrow past kb-core.
    bx = M - 60
    f.edge([(bx, fw.b + 4), (bx, drv.y - 4)], label="directly, today", label_dy=-8)
    f.connect(drv, port, "bottom", "top", label="through its hooks")
    f.connect(port, chip, "bottom", "top", label="bus transfers")

    top = core.y
    inner = f.region_inner_top(top)
    tools = [
        ("driver-template", ["starts a driver"]),
        ("board-template", ["starts a board"]),
        ("ci-tools", ["checks, documents, releases"]),
        ("handbook", ["the rules the checks enforce"]),
        ("espidf-tools", ["builds and flashes ESP-IDF apps"]),
        ("driver-requests", ["asks for a driver or a port"]),
    ]
    y = inner
    for name, lines in tools:
        c = f.card(nx + 16, y, side - 32, name, lines, tone="brand", accent=True)
        y += c.h + 12
    f.region(nx, top, side, y - top + 4, "Tooling and process", tone="brand")
    return f
