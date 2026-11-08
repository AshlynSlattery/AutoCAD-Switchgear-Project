"""Generate the D-201 one-line diagram (DXF, Revision A).

This script is the worked example for the project. It builds a real,
valid DXF drawing with ezdxf: a medium-voltage switchgear one-line
diagram with a utility source, a main breaker, a main bus, two feeder
breakers, a step-down transformer, and loads, plus a title block.

Run it with:
    python scripts/generate_one_line.py

It writes drawings/D-201_one-line_revA.dxf and a PNG preview next to it.
Your own drawings (the lineup elevation, Revision B) are yours to make
in LibreCAD or AutoCAD. This script just shows one way a drawing can be
produced and checked.
"""

from pathlib import Path

import ezdxf
from ezdxf.enums import TextEntityAlignment
from ezdxf.addons.drawing import Frontend, RenderContext
from ezdxf.addons.drawing.config import Configuration
from ezdxf.addons.drawing.matplotlib import MatplotlibBackend
import matplotlib.pyplot as plt

OUT_DIR = Path(__file__).resolve().parent.parent / "drawings"
DXF_PATH = OUT_DIR / "D-201_one-line_revA.dxf"
PNG_PATH = OUT_DIR / "D-201_one-line_preview.png"

# Sheet is 110 x 80 drawing units. The diagram occupies the left and
# center. The title block sits in the lower right corner.
BUS_Y = 40.0
TRUNK_X = 20.0
FDR1_X = 45.0
FDR2_X = 80.0


def breaker(msp, cx, cy, size=3.0):
    """Draw a circuit breaker symbol: a square centered on the line."""
    h = size / 2.0
    msp.add_lwpolyline(
        [(cx - h, cy - h), (cx + h, cy - h), (cx + h, cy + h),
         (cx - h, cy + h), (cx - h, cy - h)],
        dxfattribs={"layer": "EQUIPMENT"},
    )


def label(msp, x, y, text, height=1.7, align="LEFT"):
    placement = (TextEntityAlignment.CENTER if align == "CENTER"
                 else TextEntityAlignment.LEFT)
    msp.add_text(
        text,
        dxfattribs={"layer": "TEXT", "height": height,
                    "style": "Standard"},
    ).set_placement((x, y), align=placement)


def build():
    doc = ezdxf.new("R2010", setup=True)
    doc.units = ezdxf.units.MM
    for layer in ("BORDER", "BUS", "EQUIPMENT", "TEXT"):
        if layer not in doc.layers:
            doc.layers.add(layer)
    doc.layers.get("BUS").lineweight = 50  # the bus draws heavy
    msp = doc.modelspace()

    # --- sheet border ---
    msp.add_lwpolyline(
        [(0, 0), (110, 0), (110, 80), (0, 80), (0, 0)],
        dxfattribs={"layer": "BORDER"},
    )

    # --- utility source ---
    msp.add_circle((TRUNK_X, 63), radius=3.2,
                   dxfattribs={"layer": "EQUIPMENT"})
    label(msp, TRUNK_X, 68.2, "UTILITY SOURCE", align="CENTER")
    label(msp, TRUNK_X, 57.4, "12.47 kV, 3 PHASE", align="CENTER")
    msp.add_line((TRUNK_X, 59.8), (TRUNK_X, 51),
                 dxfattribs={"layer": "BUS"})

    # --- main breaker ---
    breaker(msp, TRUNK_X, 49)
    label(msp, TRUNK_X + 3.2, 49.8, "MAIN BREAKER 52-M")
    label(msp, TRUNK_X + 3.2, 47.2, "2000 A FRAME")
    msp.add_line((TRUNK_X, 47.5), (TRUNK_X, BUS_Y),
                 dxfattribs={"layer": "BUS"})

    # --- main bus ---
    msp.add_line((8, BUS_Y), (96, BUS_Y), dxfattribs={"layer": "BUS"})
    label(msp, 52, BUS_Y + 1.6, "MAIN BUS, 15 kV CLASS, 2000 A",
          align="CENTER")

    # --- feeder 1: breaker, transformer, 480 V load ---
    msp.add_line((FDR1_X, BUS_Y), (FDR1_X, 35.5),
                 dxfattribs={"layer": "BUS"})
    breaker(msp, FDR1_X, 33.5)
    label(msp, FDR1_X + 3.2, 34.3, "FDR-01 BREAKER")
    label(msp, FDR1_X + 3.2, 31.7, "1200 A FRAME")
    msp.add_line((FDR1_X, 32), (FDR1_X, 28.4),
                 dxfattribs={"layer": "BUS"})
    # transformer: two overlapping circles
    msp.add_circle((FDR1_X, 26.2), radius=2.6,
                   dxfattribs={"layer": "EQUIPMENT"})
    msp.add_circle((FDR1_X, 22.6), radius=2.6,
                   dxfattribs={"layer": "EQUIPMENT"})
    label(msp, FDR1_X + 4.2, 24.6, "XFMR T1")
    label(msp, FDR1_X + 4.2, 22.0, "1500 kVA")
    label(msp, FDR1_X + 4.2, 19.4, "12.47 kV-480 V")
    msp.add_line((FDR1_X, 20), (FDR1_X, 15),
                 dxfattribs={"layer": "BUS"})
    msp.add_lwpolyline(
        [(FDR1_X - 8.5, 8), (FDR1_X + 8.5, 8), (FDR1_X + 8.5, 15),
         (FDR1_X - 8.5, 15), (FDR1_X - 8.5, 8)],
        dxfattribs={"layer": "EQUIPMENT"},
    )
    label(msp, FDR1_X, 10.8, "480 V MCC-1", height=1.5, align="CENTER")

    # --- feeder 2: breaker, direct load ---
    msp.add_line((FDR2_X, BUS_Y), (FDR2_X, 35.5),
                 dxfattribs={"layer": "BUS"})
    breaker(msp, FDR2_X, 33.5)
    label(msp, FDR2_X + 3.2, 34.3, "FDR-02 BREAKER")
    label(msp, FDR2_X + 3.2, 31.7, "1200 A FRAME")
    msp.add_line((FDR2_X, 32), (FDR2_X, 27),
                 dxfattribs={"layer": "BUS"})
    msp.add_lwpolyline(
        [(FDR2_X - 8, 20), (FDR2_X + 8, 20), (FDR2_X + 8, 27),
         (FDR2_X - 8, 27), (FDR2_X - 8, 20)],
        dxfattribs={"layer": "EQUIPMENT"},
    )
    label(msp, FDR2_X, 22.8, "MOTOR LOAD", height=1.5, align="CENTER")

    # --- title block, lower right ---
    tb_x0, tb_y0, tb_x1, tb_y1 = 66, 2, 108, 18
    msp.add_lwpolyline(
        [(tb_x0, tb_y0), (tb_x1, tb_y0), (tb_x1, tb_y1),
         (tb_x0, tb_y1), (tb_x0, tb_y0)],
        dxfattribs={"layer": "BORDER"},
    )
    for y in (11, 7.5, 4.75):
        msp.add_line((tb_x0, y), (tb_x1, y),
                     dxfattribs={"layer": "BORDER"})
    for y_lo, y_hi in ((7.5, 11), (4.75, 7.5), (2, 4.75)):
        msp.add_line((88, y_lo), (88, y_hi),
                     dxfattribs={"layer": "BORDER"})
    label(msp, tb_x0 + 1.5, 15.0,
          "MEDIUM-VOLTAGE SWITCHGEAR", height=1.6)
    label(msp, tb_x0 + 1.5, 12.5, "LINEUP, ONE-LINE DIAGRAM", height=1.6)
    label(msp, tb_x0 + 1.5, 8.6, "DRAWING NO: D-201", height=1.4)
    label(msp, 89.5, 8.6, "REV: A", height=1.4)
    label(msp, tb_x0 + 1.5, 5.6, "SCALE: NTS", height=1.3)
    label(msp, 89.5, 5.6, "DATE: 2026-10-17", height=1.3)
    label(msp, tb_x0 + 1.5, 2.9, "DRAWN BY:", height=1.3)
    label(msp, 89.5, 2.9, "SHEET: 1 OF 1", height=1.3)

    doc.saveas(DXF_PATH)
    return doc


def render_preview(doc):
    fig = plt.figure(figsize=(11, 8))
    ax = fig.add_axes([0, 0, 1, 1])
    ax.set_facecolor("white")
    ctx = RenderContext(doc)
    backend = MatplotlibBackend(ax)
    Frontend(ctx, backend,
             config=Configuration(
                 background_policy=ezdxf.addons.drawing.config
                 .BackgroundPolicy.WHITE)).draw_layout(
                     doc.modelspace(), finalize=True)
    fig.savefig(PNG_PATH, dpi=150, facecolor="white")
    plt.close(fig)


if __name__ == "__main__":
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    document = build()
    render_preview(document)
    print(f"wrote {DXF_PATH}")
    print(f"wrote {PNG_PATH}")
