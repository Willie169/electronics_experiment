import numpy as np
import matplotlib.pyplot as plt


def foo(vin_pp, freq, vout_pp, title, filename):
    assert freq.shape == vout_pp.shape
    gain = vout_pp / vin_pp
    gain_db = 20 * np.log10(gain)
    plt.figure(figsize=(9, 6))
    plt.semilogx(freq, gain_db, "o-", label="Measured")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title(title)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename, dpi=300)


vin_pp = 0.2

freq1 = np.concatenate(
    [
        np.arange(100, 2000, 100),
        np.arange(2000, 20000, 1000),
        np.arange(20000, 30000, 2000),
        np.arange(30000, 100000, 10000),
        np.arange(100000, 350000, 50000),
    ]
)

vout_pp1 = np.array(
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
        7.0,
        6.6,
        6.2,
        5.8,
        5.4,
        5.0,
        4.6,
        4.4,
        4.2,
        4.0,  # 2k
        3.6,  # 2.2k
        3.4,
        3.2,
        3.0,
        2.8,  # 3k
        2.2,  # 4k
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

freq2 = np.concatenate(
    [
        np.arange(2000, 4000, 100),
        np.arange(4000, 10000, 500),
        np.arange(10000, 20000, 1000),
        np.arange(20000, 50000, 5000),
        np.arange(50000, 100000, 10000),
        np.arange(100000, 1100000, 100000),
    ]
)

vout_pp2 = np.array(
    [
        24.8,  # 2k
        23.8,  # 2.1k
        22.8,
        21.8,
        22.8,
        20.0,
        19.4,
        18.6,
        18.0,
        17.4,
        16.8,  # 3k
        16.2,
        15.8,
        15.2,
        14.8,
        14.4,
        14,
        13.6,
        13.2,
        12.8,
        12.4,  # 4k
        11,  # 4.5k
        10,  # 5k
        9,
        8.2,
        7.2,
        6.8,
        6.4,
        6,
        5.6,
        5.2,
        5.0,
        4.8,  # 10k
        4.4,  # 11k
        4.0,
        3.6,
        3.2,
        3.0,
        2.8,
        2.6,
        2.4,
        2.2,
        2.0,  # 20k
        1.6,  # 25k
        1.2,
        0.8,
        0.6,
        0.4,
        0.4,  # 50k
        0.4,  # 60k
        0.4,
        0.4,
        0.4,
        0.4,  # 100k
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
    ]
)

foo(vin_pp, freq1, vout_pp1, "103 Integrator Bode Magnitude Plot", "103.png")
foo(vin_pp, freq2, vout_pp2, "102 Integrator Bode Magnitude Plot", "102.png")
