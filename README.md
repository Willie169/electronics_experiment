## Noninverting amplifier

- Target: An op amp operating under $\pm 15$ V where $v_i$ is connected to $v_+$, $v_-$ is connected ground through a 1 k Ohm resistance, and $v_o$ is connected to $v_-$ through a 2 k Ohm resistance
- Input: 500-500 k Hz 2 V amplitude sine wave
- Output $v_o$
- Measured data: [`bode_plot.py`](bode_plot.py) `freq` (frequency (Hz)) and `vout_pp` (output voltage peak-to-peak).
- Bode magnitude plot: [`bode_plot.png`](bode_plot.png)
- Phase shift: Does in high frequency, about 45 degree shift at $\ge 10^3$ Hz order of magnitude
- Photos: [`photo/Noninverting_amplifier`](photo/Noninverting_amplifier)

## Difference amplifier 1

- Target: An op amp operating under $\pm 15$ V where $v_1$ is connected to $v_-$ through a 1 k Ohm resistance, $v_2$ is connected to $v_+$ through a 1 k Ohm resistance, $v_+$ is connected to ground through a 1 k Ohm resistance, and $v_o$ is connected to $v_-$ through a 1 k Ohm resistance
- Input: 500-500 k Hz 2 V amplitude sine wave
- Output $v_o$
- Common-mode gain (expected): 0
- Common-mode gain (measured): 0
- Differential gain (expected): 1
- Differential gain (measured, low-frequency): 1
- Normalized differential frequency response: Similar to that of noninverting amplifier
- Photos: [`photo/Difference_amplifier_1`](photo/Difference_amplifier_1)


## Difference amplifier 2

- Target: An op amp operating under $\pm 15$ V where $v_1$ is connected to $v_-$ through a 1 k Ohm resistance, $v_2$ is connected to $v_+$ through a 1 k Ohm resistance, $v_+$ is connected to ground through a 1 k Ohm resistance, and $v_o$ is connected to $v_-$ through a 10 k Ohm resistance
- Input: 500-500 k Hz 2 V amplitude sine wave
- Output $v_o$
- Common-mode gain (expected): -4.5
- Common-mode gain (measured): -4.48
- Differential gain (expected): 7.75
- Differential gain (measured, floating source, low-frequency): 5.39
- Photos: [`photo/Difference_amplifier_2`](photo/Difference_amplifier_2)

## Difference amplifier 3

- Target: An op amp operating under $\pm 15$ V where $v_1$ is connected to $v_-$ through a 1 k Ohm resistance, $v_2$ is connected to $v_+$ through a 1 k Ohm resistance, $v_+$ is connected to ground through a 1 k Ohm resistance, $v_o$ is connected to $v_-$ through a 10 k Ohm resistance, and $v_1$ is connected to ground
- Input: 500-500 k Hz 2 V amplitude sine wave at $v_2$ relative to ground
- Output $v_o$
- Result: Square wave
- Photos: [`photo/Difference_amplifier_3`](photo/Difference_amplifier_3)

