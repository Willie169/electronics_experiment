## Noninverting amplifier

- Target: An op amp operating under $\pm 15$ V where $v_i$ is connected to $v_+$, $v_-$ is connected ground through a 1 k Ohm resistance, and $v_o$ is connected to $v_-$ through a 2 k Ohm resistance
- Input: 500-500 k Hz 2 V amplitude sine wave
- Output $v_o$
- Measured data: [`bode_plot.py`](bode_plot.py) `freq` (frequency (Hz)) and `vout_pp` (output voltage peak-to-peak).
- Bode magnitude plot: [`bode_plot.png`](bode_plot.png)
- Photos: [`photo/Noninverting_amplifier`](photo/Noninverting_amplifier)


## Difference amplifier 1

- Target: An op amp operating under $\pm 15$ V where $v_1$ is connected to $v_-$ through a 1 k Ohm resistance, $v_2$ is connected to $v_+$ through a 1 k Ohm resistance, $v_+$ is connected to ground through a 1 k Ohm resistance, and $v_o$ is connected to $v_-$ through a 1 k Ohm resistance
- Common-mode gain (expected): 0
- Common-mode gain (measured): 0
- Differential gain (expected): 1
- Differential gain (measured, low-frequency): 1

