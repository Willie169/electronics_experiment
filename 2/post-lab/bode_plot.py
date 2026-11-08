import csv
import numpy as np
import matplotlib.pyplot as plt

R = 1e3  # Integrator input resistor, ohms
RF = 20e3  # Integrator feedback resistor, ohms
R_DIFF = 1e3  # Differentiator feedback resistor, ohms
VIN_PP = 0.4  # Input peak-to-peak voltage, V


def transfer_function(freq, name, C):
    s = 2j * np.pi * np.asarray(freq, dtype=float)
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
    return -Zf / Zin


def magnitude_db(H):
    return 20 * np.log10(np.abs(H))


def find_crossings(freq, gain_db, level):
    x = np.log10(freq)
    y = np.asarray(gain_db) - level
    crossings = []
    for i in range(len(x) - 1):
        if y[i] * y[i + 1] < 0:
            xc = x[i] - y[i] * (x[i + 1] - x[i]) / (y[i + 1] - y[i])
            crossings.append(10**xc)
        elif y[i] == 0:
            crossings.append(freq[i])
    if len(y) > 0 and y[-1] == 0:
        crossings.append(freq[-1])
    return sorted(set(crossings))


def format_frequency(freq):
    if freq >= 1e6:
        return f"{freq / 1e6:.2f} MHz"
    elif freq >= 1e3:
        return f"{freq / 1e3:.2f} kHz"
    else:
        return f"{freq:.1f} Hz"


def process(C, freq, vout_pp, name, title, plotname, tablename):
    assert freq.shape == vout_pp.shape
    freq = np.asarray(freq, dtype=float)
    measured = np.asarray(vout_pp, dtype=float)
    H = transfer_function(freq, name, C)
    ideal_vout = VIN_PP * np.abs(H)
    dbs = [20 * np.log10(measured / VIN_PP), magnitude_db(H)]
    ideal_error = 100 * (measured - ideal_vout) / ideal_vout
    columns = [
        "frequency (Hz)",
        "measured output voltage\npeak-to-peak (V)",
        "measured gain\n(dB)",
        "ideal output voltage\npeak-to-peak (V)",
        "ideal gain\n(dB)",
        "error w.r.t.\nideal (%)",
    ]
    data = [
        [
            f"{f:.0f}",
            f"{m:.2f}",
            f"{md:.2f}",
            f"{i:.2f}",
            f"{id:.2f}",
            f"{ie:.2f}",
        ]
        for f, m, md, i, id, ie in zip(
            freq,
            measured,
            dbs[0],
            ideal_vout,
            dbs[1],
            ideal_error,
        )
    ]
    fig, ax = plt.subplots(figsize=(10, 1))
    ax.axis("off")
    table = ax.table(
        cellText=data,
        colLabels=columns,
        loc="center",
        cellLoc="center",
    )
    table.auto_set_font_size(True)
    table.scale(1, 1.5)
    fig.savefig(tablename, dpi=300, bbox_inches="tight")
    plt.close(fig)
    fig, ax = plt.subplots(figsize=(12, 7))
    line_styles = ["o-", "--"]
    amp_names = ["Measured", "Ideal op-amp"]
    amp_colors = ["tab:blue", "tab:orange"]
    for db, line_style, amp_name, color in zip(dbs, line_styles, amp_names, amp_colors):
        ax.semilogx(freq, db, line_style, label=amp_name, color=color)
    freq_dense = np.logspace(
        np.log10(freq.min()),
        np.log10(freq.max()),
        10000,
    )
    ideal_dense_db = magnitude_db(transfer_function(freq_dense, name, C))
    reference_levels = [0, -3]
    reference_colors = ["pink", "violet"]
    for level, reference_color in zip(reference_levels, reference_colors):
        crossings = [
            find_crossings(freq, dbs[0], level),
            find_crossings(freq_dense, ideal_dense_db, level),
        ]
        label = f"{level} dB reference"
        for crossing, amp_name, amp_color in zip(crossings, amp_names, amp_colors):
            for i, fc in enumerate(crossing):
                ax.plot(
                    fc,
                    level,
                    marker="D",
                    markersize=6,
                    color=amp_color,
                    zorder=5,
                )
                ax.axvline(
                    fc,
                    color=amp_color,
                    linestyle="-.",
                )
                label += f"\n    {amp_name}: {format_frequency(fc)}"
        ax.axhline(
            level,
            color=reference_color,
            linestyle="-.",
            label=label,
        )
    ax.set_xlabel("Frequency (Hz)")
    ax.set_ylabel("Magnitude (dB)")
    ax.set_title(title)
    ax.grid(True, which="both", linestyle="--", alpha=0.5)
    ax.legend()
    fig.tight_layout()
    fig.savefig(plotname, dpi=300)
    plt.close(fig)


freq_int_103 = np.concatenate(
    [
        np.arange(100, 2000, 100),
        np.arange(2000, 4000, 200),
        np.arange(4000, 10000, 1000),
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
        7.2,  # 1k
        6.4,
        5.8,
        5.2,
        4.8,
        4.4,
        4.0,
        3.8,
        3.6,
        3.4,
        3.2,  # 2k
        2.8,  # 2.2k
        2.6,
        2.4,
        2.2,
        2.0,
        1.8,
        1.8,
        1.6,
        1.6,
        1.4,  # 4k
        1.2,  # 5k
        1,
        0.8,
        0.8,
        0.6,
        0.6,
        0.4,  # 20k
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,  # 100k
        0.2,
        0.2,
        0.2,
        0.2,
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
        np.arange(50000, 100000, 10000),
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
        0.8,
        0.8,
        0.6,
        0.6,  # 100k
        0.4,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
        0.2,
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
    "3Iint_plot.png",
    "3Iint_table.png",
)

# Exp. 3 (I) Differentiator
process(
    10e-9,
    freq_diff,
    vout_pp_diff,
    "differentiator",
    "Exp. 3 (I) Differentiator Bode Magnitude Plot",
    "3Idiff_plot.png",
    "3Idiff_table.png",
)

# Exp. 3 (II) Integrator without feedback resistor
process(
    1e-9,
    freq_int_102,
    vout_pp_int_102,
    "integrator_without_rf",
    "Exp. 3 (II) Integrator without Feedback Resistor Bode Magnitude Plot",
    "3IIwithout_plot.png",
    "3IIwithout_table.png",
)

# Exp. 3 (II) Integrator with feedback resistor
process(
    1e-9,
    freq_int_rf,
    vout_pp_int_rf,
    "integrator_with_rf",
    "Exp. 3 (II) Integrator with Feedback Resistor Bode Magnitude Plot",
    "3IIwith_plot.png",
    "3IIwith_table.png",
)
