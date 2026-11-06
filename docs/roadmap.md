# Roadmap

<div class="kb-steps" markdown>

1. **Foundations** (done). The organisation, `ci-tools` v1, `espidf-tools` v1, `driver-template`, this site.
2. **Drivers.** Chip drivers move in from HardFOC, renamed `driver-<chip>`, each with host tests and an ESP32
   example.
3. **kb-core.** One repository with `kb::utils`, `kb::rtos`, `kb::interfaces` and `kb::handlers`.
4. **Hardware abstraction.** MCU ports under `interfaces/mcu/<family>/`, starting with ESP32.
5. **HardFOC on Kokeb.** The HardFOC boards build on these drivers and kb-core.
6. **Tools for users.** A command-line tool, a board configurator and a documentation hub.

</div>
