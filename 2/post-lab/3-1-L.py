import numpy as np
import matplotlib.pyplot as plt

vin_pp = 0.2

freq = np.concatenate(
    [
        np.arange(100, 1000, 100),
        np.arange(1000, 20000, 1000),
        np.arange(20000, 100000, 10000),
        np.arange(100000, 350000, 50000),
    ]
)

vout_pp = np.array(
    [
        27.4,  # 100
        27.4,
        23,
        17.4,
        14,
        11.8,
        10.2,
        9.2,
        8.4,
        7.4,  # 1k
        4.0,
        2.8,
        2.2,
        1.8,
        1.4,
        1.2,
        1.0,
        1.0,
        1.0,  # 10k
        0.8,
        0.8,
        0.8,
        0.8,
        0.6,  # 15k
        0.6,
        0.6,
        0.6,
        0.6,
        0.6,  # 20k
        0.6,
        0.6,
        0.6,
        0.6,
        0.6,
        0.6,
        0.6,
        0.6,  # 100k
        0.6,
        0.6,
        0.6,
        0.6,
    ]
)

assert freq.shape == vout_pp.shape

gain = vout_pp / vin_pp
gain_db = 20 * np.log10(gain)

plt.figure(figsize=(9, 6))
plt.semilogx(freq, gain_db, "o-", label="Measured")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude (dB)")
plt.title("Integrator Bode Magnitude Plot")
plt.grid(True, which="both", linestyle="--", alpha=0.5)
plt.legend()
plt.tight_layout()
plt.savefig("bode_plot.png", dpi=300)
