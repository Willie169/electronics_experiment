import numpy as np
import matplotlib.pyplot as plt

vin_pp = 4.0

freq = np.concatenate(
    [
        np.arange(500, 1000, 100),
        np.arange(1000, 11000, 1000),
        np.arange(20000, 40000, 2000),
        np.arange(40000, 100000, 10000),
        np.arange(100000, 200000, 20000),
        np.arange(200000, 400000, 50000),
        np.arange(400000, 600000, 100000),
    ]
)

vout_pp = np.array(
    [
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.4,
        12.2,
        12.2,
        11.6,
        11.0,
        10.4,
        9.6,
        9.0,
        8.4,
        8.0,
        7.6,
        7.4,
        6.0,
        5.0,
        4.4,
        4.0,
        3.6,
        3.2,
        2.8,
        2.6,
        2.4,
        2.2,
        2.0,
        1.8,
        1.6,
        1.4,
        1.2,
        1.0,
    ]
)

gain = vout_pp / vin_pp
gain_db = 20 * np.log10(gain)

plt.figure(figsize=(9, 6))
plt.semilogx(freq, gain_db, "o-", label="Measured")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Non-inverting Amplifier Bode Magnitude Plot")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("bode_plot.png", dpi=300)
