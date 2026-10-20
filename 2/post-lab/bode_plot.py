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


vin_pp = 0.4

freq_int_103 = np.concatenate(
    [
        np.arange(100, 2000, 100),
        np.arange(2000, 3000, 200),
        np.arange(3000, 4000, 500),
        np.arange(4000, 8000, 1000),
        np.arange(8000, 10000, 2000),
        np.arange(10000, 100000, 10000),
        np.arange(100000, 350000, 50000),
    ]
)

vout_pp_int_103 = np.array(
    [
        27.4,  # 100
        27.4,
        23,
        17.4,
        14,
        11.8,
        10.4,
        9.2,
        8.2,
        7.4,  # 1k
        6.8,
        6.4,
        6.0,
        5.6,
        5.2,
        5.0,
        4.8,
        4.6,
        4.4,
        4.2,  # 2k
        3.8,  # 2.2k
        3.6,
        3.4,
        3.2,
        3.0,  # 3k
        2.6,  # 3.5k
        2.2,  # 4k
        1.8,
        1.6,
        1.4,
        1.2,  # 8k
        1,  # 10k
        0.6,  # 20k
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,
        0.4,  # 100k
        0.4,
        0.4,
        0.4,
        0.4,
    ]
)

freq_int_102 = np.concatenate(
    [
        np.arange(2000, 4000, 100),
        np.arange(4000, 10000, 500),
        np.arange(10000, 20000, 2000),
        np.arange(20000, 50000, 5000),
        np.arange(50000, 60000, 10000),
        np.arange(60000, 100000, 20000),
        np.arange(100000, 1100000, 100000),
    ]
)

vout_pp_int_102 = np.array(
    [
        24.8,  # 2k
        23.8,  # 2.1k
        22.8,
        21.8,
        20.8,
        19.8,
        19.2,
        18.6,
        18.0,
        17.4,
        16.8,  # 3k
        16.4,
        16.0,
        15.6,
        15.2,
        14.8,
        14.4,
        14.0,
        13.6,
        13.2,
        12.8,  # 4k
        11.4,  # 4.5k
        10.2,
        9.2,
        8.2,
        7.4,
        6.8,
        6.4,
        6.0,
        5.6,
        5.2,
        5.0,
        4.8,  # 10k
        4.2,
        3.8,
        3.4,
        3.0,
        2.8,  # 20k
        2.4,  # 25k
        2.0,
        1.8,
        1.6,
        1.4,
        1.2,  # 50k
        1.0,  # 60k
        0.8,  # 80k
        0.6,  # 100k
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

freq_diff = np.array(
    [
        100,
        200,
        500,
        1000,
        2000,
        5000,
        10000,
        20000,
        25000,
        30000,
        35000,
        40000,
        45000,
        50000,
        100000,
    ]
)

vout_pp_diff = np.array(
    [0.04, 0.048, 0.056, 0.06, 0.084, 0.15, 0.26, 0.498, 0.8, 1, 1, 1.2, 1.4, 1.6, 2.6]
)

freq_int_shunt = np.array(
    [
        100,
        200,
        500,
        1000,
        1500,
        2000,
        2500,
        3700,
        4500,
        5000,
        7000,
        10000,
        20000,
        50000,
        100000,
        200000,
        500000,
        1000000,
    ]
)

vout_pp_int_shunt = np.array(
    [
        8,
        8,
        8,
        7.92,
        7.76,
        7.6,
        7.4,
        7,
        6.6,
        6.32,
        5.4,
        4.4,
        2.48,
        1.12,
        0.56,
        0.4,
        0.24,
        0.16,
    ]
)

foo(
    vin_pp,
    freq_int_103,
    vout_pp_int_103,
    "Exp. 3 (I) Integrator Bode Magnitude Plot",
    "3Iint.png",
)
foo(
    vin_pp,
    freq_diff,
    vout_pp_diff,
    "Exp. 3 (I) Differentiator Bode Magnitude Plot",
    "3Idiff.png",
)
foo(
    vin_pp,
    freq_int_102,
    vout_pp_int_102,
    "Exp. 3 (II) Integrator without feedback resistor Bode Magnitude Plot",
    "3IIwo.png",
)
foo(
    vin_pp,
    freq_int_shunt,
    vout_pp_int_shunt,
    "Exp. 3 (II) Integrator with Feedback Resistor Bode Magnitude Plot",
    "3IIw.png",
)
