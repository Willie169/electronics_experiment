import csv
import numpy as np
import matplotlib.pyplot as plt

R = 1e3  # Integrator input resistor, ohms
RF = 20e3  # Integrator feedback resistor, ohms
R_DIFF = 1e3  # Differentiator feedback resistor, ohms
GBW = 1e6  # Op-amp gain-bandwidth product, Hz
VIN_PP = 0.4  # Input peak-to-peak voltage, V


def transfer_function(freq, name, C):
    # Return ideal and finite-GBW complex transfer functions
    s = 2j * np.pi * np.asarray(freq, dtype=float)
    A = GBW / (s)
    if name == "integrator_with_rf":
        # input resistor R
        # feedback capacitor C in parallel with RF
        Zin = R
        Zf = 1 / (1 / RF + s * C)
    elif name == "integrator_without_rf":
        # input resistor R
        # feedback capacitor C
        Zin = R
        Zf = 1 / (s * C)
    elif name == "differentiator":
        # input capacitor C
        # feedback resistor R_DIFF
        Zin = 1 / (s * C)
        Zf = R_DIFF
    else:
        raise ValueError(f"Unknown name: {name}")
    H_ideal = -Zf / Zin
    H_gbw = -A * Zf / (Zf + (1 + A) * Zin)
    return H_ideal, H_gbw


def magnitude_db(H):
    return 20 * np.log10(np.abs(H))


def process(C, freq, vout_pp, name, title, fig_filename, csv_filename):
    assert freq.shape == vout_pp.shape
    freq = np.asarray(freq, dtype=float)
    measured = np.asarray(vout_pp, dtype=float)
    H_ideal, H_gbw = transfer_function(freq, name, C)
    ideal_vout = VIN_PP * np.abs(H_ideal)
    gbw_vout = VIN_PP * np.abs(H_gbw)
    measured_db = 20 * np.log10(measured / VIN_PP)
    ideal_db = magnitude_db(H_ideal)
    gbw_db = magnitude_db(H_gbw)
    ideal_error = 100 * (measured - ideal_vout) / ideal_vout
    gbw_error = 100 * (measured - gbw_vout) / gbw_vout
    columns = [
        "frequency_Hz",
        "measured_vout_pp_V",
        "measured_gain_dB",
        "ideal_vout_pp_V",
        "ideal_gain_dB",
        "ideal_error_percent",
        "gbw_vout_pp_V",
        "gbw_gain_dB",
        "gbw_error_percent",
    ]
    data = np.column_stack(
        [
            freq,
            measured,
            measured_db,
            ideal_vout,
            ideal_db,
            ideal_error,
            gbw_vout,
            gbw_db,
            gbw_error,
        ]
    )
    with open(csv_filename, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(columns)
        writer.writerows(data)
    plt.figure(figsize=(10, 6))
    plt.semilogx(freq, measured_db, "o-", label="Measured")
    plt.semilogx(freq, ideal_db, "--", label="Ideal op-amp")
    plt.semilogx(freq, gbw_db, "-.", label="GBW = 1 MHz")
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude (dB)")
    plt.title(title)
    plt.grid(True, which="both", linestyle="--", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_filename, dpi=300)
    plt.close()


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

freq_int_rf = np.array(
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

vout_pp_int_rf = np.array(
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

# Exp. 3 (I) Integrator
process(
    10e-9,
    freq_int_103,
    vout_pp_int_103,
    "integrator_without_rf",
    "Exp. 3 (I) Integrator Bode Magnitude Plot",
    "3Iint.png",
    "3Iint.csv",
)

# Exp. 3 (I) Differentiator
process(
    10e-9,
    freq_diff,
    vout_pp_diff,
    "differentiator",
    "Exp. 3 (I) Differentiator Bode Magnitude Plot",
    "3Idiff.png",
    "3Idiff.csv",
)

# Exp. 3 (II) Integrator without feedback resistor
process(
    1e-9,
    freq_int_103,
    vout_pp_int_103,
    "integrator_without_rf",
    "Exp. 3 (II) Integrator without Feedback Resistor Bode Magnitude Plot",
    "3IIwithout.png",
    "3IIwithout.csv",
)

# Exp. 3 (II) Integrator with feedback resistor
process(
    1e-9,
    freq_int_rf,
    vout_pp_int_rf,
    "integrator_with_rf",
    "Exp. 3 (II) Integrator with Feedback Resistor Bode Magnitude Plot",
    "3IIwith.png",
    "3IIwith.csv",
)
