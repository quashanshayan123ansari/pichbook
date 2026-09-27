"""
ATLAS — Excel Data Pack Generator
Writes all Stage 4 computed outputs to a formatted Excel workbook.
Run: python atlas_excel.py
Output: ATLAS_DataPack.xlsx
"""

import sys
try:
    import openpyxl
    from openpyxl.styles import (PatternFill, Font, Alignment, Border, Side,
                                  GradientFill)
    from openpyxl.utils import get_column_letter
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "openpyxl", "-q"])
    import openpyxl
    from openpyxl.styles import PatternFill, Font, Alignment, Border, Side

from openpyxl import Workbook
from openpyxl.styles import PatternFill, Font, Alignment, Border, Side
from openpyxl.utils import get_column_letter

# ── Colour palette ────────────────────────────────────────────────────────────
NAVY        = "14315E"   # header fills
CYAN        = "29ABE2"   # ATLAS highlight
YELLOW      = "FFFBCC"   # key output cells
LIGHT_BLUE  = "D6EAF8"   # alternate row
GREY_FILL   = "F2F2F2"   # light row alternation
WHITE       = "FFFFFF"
PASS_GREEN  = "D5F5E3"
HEADER_FNT  = Font(name="Arial", bold=True, color=WHITE, size=9)
NAVY_FNT    = Font(name="Arial", bold=True, color=NAVY, size=9)
CYAN_FNT    = Font(name="Arial", bold=True, color=CYAN, size=9)
BODY_FNT    = Font(name="Arial", size=9)
BOLD_FNT    = Font(name="Arial", bold=True, size=9)
TITLE_FNT   = Font(name="Arial", bold=True, color=NAVY, size=12)

def fill(hex_colour):
    return PatternFill("solid", fgColor=hex_colour)

def thin_border():
    s = Side(style="thin", color="BFBFBF")
    return Border(left=s, right=s, top=s, bottom=s)

def center():
    return Alignment(horizontal="center", vertical="center", wrap_text=True)

def right():
    return Alignment(horizontal="right", vertical="center")

def left():
    return Alignment(horizontal="left", vertical="center", wrap_text=True)

def header_row(ws, row, cols, values, bg=NAVY, fg=WHITE, height=20):
    ws.row_dimensions[row].height = height
    for c, v in zip(cols, values):
        cell = ws.cell(row=row, column=c, value=v)
        cell.fill = fill(bg)
        cell.font = Font(name="Arial", bold=True, color=fg, size=9)
        cell.alignment = center()
        cell.border = thin_border()

def data_cell(ws, row, col, value, fmt=None, bg=None, bold=False, align="center"):
    cell = ws.cell(row=row, column=col, value=value)
    cell.font = Font(name="Arial", bold=bold, size=9)
    if fmt:
        cell.number_format = fmt
    if bg:
        cell.fill = fill(bg)
    cell.alignment = center() if align == "center" else (right() if align == "right" else left())
    cell.border = thin_border()
    return cell

def title_cell(ws, row, col, text):
    cell = ws.cell(row=row, column=col, value=text)
    cell.font = TITLE_FNT
    cell.alignment = left()
    return cell

def set_col_widths(ws, widths):
    for i, w in enumerate(widths, 1):
        ws.column_dimensions[get_column_letter(i)].width = w


# ─────────────────────────────────────────────────────────────────────────────
# DATA (from atlas_compute.py outputs)
# ─────────────────────────────────────────────────────────────────────────────

companies = ["ATLAS", "HUL", "Britannia", "Marico", "Dabur", "Tata Consumer"]
tickers   = ["NESTLEIND", "HINDUNILVR", "BRITANNIA", "MARICO", "DABUR", "TATACONSUM"]

# 1. EV Bridge
ev_data = [
    # Company, Mkt Cap, Net Debt, EV (derived), EV (stored), Pass
    ("ATLAS",         262752.0,   677.2,  263429.2, 263429.2, "PASS"),
    ("HUL",           455000.0, -4424.0,  450576.0, 450576.0, "PASS"),
    ("Britannia",     117905.0,  1186.8,  119091.8, 119091.8, "PASS"),
    ("Marico",        106338.0, -1596.0,  104742.0, 104742.0, "PASS"),
    ("Dabur",          68404.0, -1541.7,   66862.3,  66862.3, "PASS"),
    ("Tata Consumer",  97307.0,   962.3,   98269.3,  98269.3, "PASS"),
]

# 2. Per Share check
ps_data = [
    # Company, Shares (mn), Price, Implied MC, Reported MC, Gap%
    ("ATLAS",         1928.31, 1362.60, 262752, 262752, 0.000),
    ("HUL",           2350.00, 1942.90, 456582, 455000, 0.003),
    ("Britannia",      240.87, 4939.00, 118966, 117905, 0.009),
    ("Marico",        1293.90,  819.00, 105970, 106338, 0.003),
    ("Dabur",         1771.50,  385.60,  68309,  68404, 0.001),
    ("Tata Consumer",  989.50,  983.00,  97268,  97307, 0.000),
]

# 3. Trading Multiples
# LTM = FY2026 for ATLAS; FY2025 for peers
mult_data = [
    # Company, LTM, EV/EBITDA, P/E, EV/Rev, EBITDA%, PAT%
    ("ATLAS",         "FY2026", 49.6, 74.1, 11.38, 0.229, 0.153),
    ("HUL",           "FY2025", 31.5, 44.3,  7.44, 0.236, 0.170),
    ("Britannia",     "FY2025", 42.9, 55.3,  6.89, 0.161, 0.123),
    ("Marico",        "FY2025", 49.0, 64.1,  9.67, 0.197, 0.153),
    ("Dabur",         "FY2025", 28.9, 39.3,  5.32, 0.184, 0.139),
    ("Tata Consumer", "FY2025", 39.3, 75.6,  5.58, 0.142, 0.073),
]

# 4. Capitalisation table (full)
cap_data = [
    # Company, Ticker, Price, Shares (mn), Mkt Cap, Debt, Cash, EV, 52wkH, 52wkL, vs High%, DPS
    ("ATLAS",         "NESTLEIND",    1362.60, 1928.31, 262752, 753,  76,  263429, 1553.00, 1145.00, -0.123, 14.00),
    ("HUL",           "HINDUNILVR",   1942.90, 2350.00, 455000, 1647, 6071, 450576, 2667.20, 1915.00, -0.272, 41.00),
    ("Britannia",     "BRITANNIA",    4939.00,  240.87, 117905, 1225,   38, 119092, 6271.00, 4883.35, -0.213, 90.50),
    ("Marico",        "MARICO",        819.00, 1293.90, 106338,  554, 2150, 104742,  889.10,  690.30, -0.079,  4.00),
    ("Dabur",         "DABUR",         385.60, 1771.50,  68404,  730, 2272,  66862,  534.00,  368.05, -0.278,  8.25),
    ("Tata Consumer", "TATACONSUM",    983.00,  989.50,  97307, 2393, 1430,  98269, 1282.70,  979.20, -0.234, 10.00),
]

# 5. Revenue history
rev_hist = {
    "ATLAS": {
        "periods": ["CY2022", "FY2025", "FY2026"],
        "revenue": [16897, 20260, 23155],
        "EBITDA":  [None, 4770, 5306],
        "PAT":     [2391, 3315, 3545],
        "note":    ["Jan–Dec 2022", "Apr 2024–Mar 2025", "Apr 2025–Mar 2026"],
    }
}

# 6. Peer income statement 3-year
peer_is = [
    # Company, FY2023 Rev, FY2024 Rev, FY2025 Rev, FY2023 EBITDA, FY2024 EBITDA, FY2025 EBITDA, FY2023 PAT, FY2024 PAT, FY2025 PAT
    ("HUL",           59549, 60966, 60573, 14272, 14476, 14296, 9962, 10114, 10282),
    ("Britannia",     15618, 16186, 17296,  2547,  2800,  2779, 2139,  2082,  2131),
    ("Marico",         9764,  9653, 10831,  1810,  1993,  2138, 1322,  1502,  1658),
    ("Dabur",         11530, 12404, 12563,  2164,  2400,  2316, 1701,  1811,  1740),
    ("Tata Consumer", 13783, 15206, 17618,  1874,  2323,  2502, 1204,  1150,  1287),
]

# 7. Balance sheet FY2025
bs_data = [
    # Company, Total Assets, Total Equity, Total Debt, Cash, Net Debt, Capex
    ("ATLAS",         12324, 4117,  753,   76,   677, 1811),
    ("HUL",           79880, 49609, 1647, 6071, -4424, 1211),
    ("Britannia",      8020, 3887,  1225,   38,  1187,  375),
    ("Marico",         8300, None,   554, 2150, -1596, None),
    ("Dabur",         11006, 10801,  730, 2272, -1542,  570),
    ("Tata Consumer", 31978, 23189, 2393, 1430,   963, None),
]

# 8. Revenue and EBITDA CAGR
cagr_data = [
    # Company, Rev FY23, Rev FY25, Rev CAGR, EBITDA FY23, EBITDA FY25, EBITDA CAGR
    ("HUL",           59549, 60573, 0.009, 14272, 14296, 0.001),
    ("Britannia",     15618, 17296, 0.052,  2547,  2779, 0.044),
    ("Marico",         9764, 10831, 0.053,  1810,  2138, 0.086),
    ("Dabur",         11530, 12563, 0.044,  2164,  2316, 0.035),
    ("Tata Consumer", 13783, 17618, 0.131,  1874,  2502, 0.156),
]

# 9. DCF Sensitivity
dcf_grid = {
    # (wacc, tgr): implied_price
    (0.11, 0.050): 350,
    (0.11, 0.055): 371,
    (0.11, 0.060): 397,
    (0.12, 0.050): 296,
    (0.12, 0.055): 310,
    (0.12, 0.060): 327,
    (0.13, 0.050): 255,
    (0.13, 0.055): 265,
    (0.13, 0.060): 277,
}
dcf_base = {
    "PV_FCFFs": 24254,
    "PV_TV": 36208,
    "TV_pct": 0.599,
    "EV": 60462,
    "Equity": 59785,
    "Price_per_share": 310,
    "Current_price": 1362.60,
    "Premium": 3.395,
}

# 10. Summary Valuation
val_data = [
    # Methodology, Low, High, Basis
    ("EV/EBITDA Comps",  791,  1345, "Peer range 28.9x–49.0x × ATLAS FY2026 EBITDA INR 5,306 Cr"),
    ("P/E Comps",        722,  1390, "Peer range 39.3x–75.6x × ATLAS FY2026 PAT INR 3,545 Cr"),
    ("DCF (Illustrative)", 255, 397, "WACC 11–13%, TGR 5–6%; analyst assumptions only"),
]

# ─────────────────────────────────────────────────────────────────────────────
# BUILD WORKBOOK
# ─────────────────────────────────────────────────────────────────────────────

wb = Workbook()

# ── Sheet 1: Checks ─────────────────────────────────────────────────────────
ws = wb.active
ws.title = "1. Checks"
ws.sheet_view.showGridLines = False

title_cell(ws, 1, 1, "ATLAS — Stage 4 Verification Checks")
ws.cell(1, 1).font = TITLE_FNT
ws.merge_cells("A1:G1")
ws.cell(2, 1, "Market Data Date: 25 September 2026  |  All figures INR Crore unless stated").font = Font(name="Arial", italic=True, size=9, color="808080")
ws.merge_cells("A2:G2")
ws.row_dimensions[2].height = 14

# EV Bridge
ws.cell(4, 1, "CHECK 1 — EV Bridge: Mkt Cap + Net Debt = Enterprise Value").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws.merge_cells("A4:G4")
header_row(ws, 5, range(1,8), ["Company", "Mkt Cap (Cr)", "Net Debt (Cr)", "EV (Derived)", "EV (Stored)", "Difference", "Result"])
for i, (co, mc, nd, evd, evs, res) in enumerate(ev_data, 6):
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = (co == "ATLAS")
    data_cell(ws, i, 1, co,   bg=bg, bold=bold, align="left")
    data_cell(ws, i, 2, mc,   bg=bg, bold=bold, fmt='#,##0')
    data_cell(ws, i, 3, nd,   bg=bg, bold=bold, fmt='#,##0.0')
    data_cell(ws, i, 4, evd,  bg=bg, bold=bold, fmt='#,##0.0')
    data_cell(ws, i, 5, evs,  bg=bg, bold=bold, fmt='#,##0.0')
    diff = round(evd - evs, 1)
    data_cell(ws, i, 6, diff, bg=bg, bold=bold, fmt='#,##0.0')
    c = ws.cell(row=i, column=7, value=res)
    c.fill = fill(PASS_GREEN)
    c.font = Font(name="Arial", bold=True, size=9, color="1E8449")
    c.alignment = center()
    c.border = thin_border()

# Per Share
ws.cell(14, 1, "CHECK 2 — Per Share × Shares = Market Capitalisation").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws.merge_cells("A14:G14")
header_row(ws, 15, range(1,8), ["Company", "Shares (mn)", "Price (INR)", "Implied Mkt Cap (Cr)", "Reported Mkt Cap (Cr)", "Gap (%)", "Result"])
for i, (co, sh, px, imc, rmc, gap) in enumerate(ps_data, 16):
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = (co == "ATLAS")
    data_cell(ws, i, 1, co,   bg=bg, bold=bold, align="left")
    data_cell(ws, i, 2, sh,   bg=bg, bold=bold, fmt='#,##0.00')
    data_cell(ws, i, 3, px,   bg=bg, bold=bold, fmt='#,##0.00')
    data_cell(ws, i, 4, imc,  bg=bg, bold=bold, fmt='#,##0')
    data_cell(ws, i, 5, rmc,  bg=bg, bold=bold, fmt='#,##0')
    data_cell(ws, i, 6, gap,  bg=bg, bold=bold, fmt='0.0%')
    ok = "PASS" if gap < 0.01 else "REVIEW"
    c = ws.cell(row=i, column=7, value=ok)
    c.fill = fill(PASS_GREEN)
    c.font = Font(name="Arial", bold=True, size=9, color="1E8449")
    c.alignment = center(); c.border = thin_border()

set_col_widths(ws, [18, 14, 14, 18, 18, 10, 8])


# ── Sheet 2: Capitalisation ──────────────────────────────────────────────────
ws2 = wb.create_sheet("2. Capitalisation")
ws2.sheet_view.showGridLines = False

title_cell(ws2, 1, 1, "Capitalisation and Market Data — 25 September 2026")
ws2.cell(1,1).font = TITLE_FNT
ws2.merge_cells("A1:L1")
ws2.cell(2, 1, "INR Crore unless stated. ATLAS = Nestlé India Limited (NESTLEIND). LTM = FY2026 for ATLAS; FY2025 for peers.").font = Font(name="Arial", italic=True, size=9, color="808080")
ws2.merge_cells("A2:L2")

cols = ["Company", "Ticker", "Price (INR)", "Shares (mn)", "Mkt Cap (Cr)", "+ Debt (Cr)", "- Cash (Cr)", "= EV (Cr)", "52-Wk High", "52-Wk Low", "vs 52-Wk High", "DPS FY2026 (INR)"]
header_row(ws2, 4, range(1, 13), cols)

for i, row in enumerate(cap_data, 5):
    co, tk, px, sh, mc, debt, cash, ev, h52, l52, vsh, dps = row
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = (co == "ATLAS")
    vals = [co, tk, px, sh, mc, debt, cash, ev, h52, l52, vsh, dps]
    fmts = ["","","#,##0.00","#,##0.00","#,##0","#,##0","#,##0","#,##0","#,##0.00","#,##0.00","0.0%","#,##0.00"]
    for c, (v, f) in enumerate(zip(vals, fmts), 1):
        cell = data_cell(ws2, i, c, v, bg=bg, bold=bold, fmt=f if f else None, align="left" if c <= 2 else "center")
    # Yellow on Mkt Cap and EV for ATLAS
    if co == "ATLAS":
        ws2.cell(i, 5).fill = fill(YELLOW)
        ws2.cell(i, 8).fill = fill(YELLOW)

set_col_widths(ws2, [16, 13, 10, 10, 12, 10, 10, 12, 10, 10, 12, 12])


# ── Sheet 3: Trading Multiples ───────────────────────────────────────────────
ws3 = wb.create_sheet("3. Trading Multiples")
ws3.sheet_view.showGridLines = False

title_cell(ws3, 1, 1, "Trading Multiples — 25 September 2026")
ws3.cell(1,1).font = TITLE_FNT
ws3.merge_cells("A1:H1")
ws3.cell(2, 1, "LTM = FY2026 for ATLAS (Apr 2025–Mar 2026); FY2025 for all peers (Apr 2024–Mar 2025). All figures INR Crore.").font = Font(name="Arial", italic=True, size=9, color="808080")
ws3.merge_cells("A2:H2")

hcols = ["Company", "LTM Period", "EV (Cr)", "LTM EBITDA (Cr)", "LTM PAT (Cr)", "EV / EBITDA", "P / E", "EV / Revenue"]
header_row(ws3, 4, range(1, 9), hcols)

# Retrieve EV and financials for display
ev_lookup = {r[0]: r for r in ev_data}
fin_map = {
    "ATLAS":         (263429, 5306, 3545, 23155),
    "HUL":           (450576, 14296, 10282, 60573),
    "Britannia":     (119092, 2779, 2131, 17296),
    "Marico":        (104742, 2138, 1658, 10831),
    "Dabur":         (66862, 2316, 1740, 12563),
    "Tata Consumer": (98269, 2502, 1287, 17618),
}

for i, (co, ltm, ev_eb, pe, ev_rev, ebitda_mg, pat_mg) in enumerate(mult_data, 5):
    ev_c, ebitda_c, pat_c, rev_c = fin_map[co]
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = (co == "ATLAS")
    row_vals = [co, ltm, ev_c, ebitda_c, pat_c, ev_eb, pe, ev_rev]
    fmts =     ["", "", "#,##0", "#,##0", "#,##0", "0.0", "0.0", "0.00"]
    for c, (v, f) in enumerate(zip(row_vals, fmts), 1):
        data_cell(ws3, i, c, v, bg=bg, bold=bold, fmt=f, align="left" if c == 1 else "center")
    if co == "ATLAS":
        for c in [6, 7, 8]:
            ws3.cell(i, c).fill = fill(YELLOW)

# Separator row
ws3.cell(11, 1, "EBITDA and PAT Margins").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws3.merge_cells("A11:H11")

hcols2 = ["Company", "LTM Period", "LTM Revenue (Cr)", "LTM EBITDA (Cr)", "LTM PAT (Cr)", "EBITDA Margin", "PAT Margin", "Peer Median EV/EBITDA"]
header_row(ws3, 12, range(1, 9), hcols2)
peer_medians = {"EV_EBITDA": 39.3, "PE": 55.3}

for i, (co, ltm, ev_eb, pe, ev_rev, ebitda_mg, pat_mg) in enumerate(mult_data, 13):
    ev_c, ebitda_c, pat_c, rev_c = fin_map[co]
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = (co == "ATLAS")
    row_vals = [co, ltm, rev_c, ebitda_c, pat_c, ebitda_mg, pat_mg, peer_medians["EV_EBITDA"] if co != "ATLAS" else "—"]
    fmts =     ["", "", "#,##0", "#,##0", "#,##0", "0.0%", "0.0%", "0.0"]
    for c, (v, f) in enumerate(zip(row_vals, fmts), 1):
        data_cell(ws3, i, c, v, bg=bg, bold=bold, fmt=f if isinstance(v, (int, float)) else None, align="left" if c == 1 else "center")

set_col_widths(ws3, [16, 10, 14, 14, 12, 10, 8, 16])


# ── Sheet 4: Income Statement ────────────────────────────────────────────────
ws4 = wb.create_sheet("4. Income Statement")
ws4.sheet_view.showGridLines = False

title_cell(ws4, 1, 1, "Income Statement Summary — ATLAS and Peers")
ws4.cell(1,1).font = TITLE_FNT
ws4.merge_cells("A1:P1")
ws4.cell(2, 1, "INR Crore. ATLAS: standalone, Ind AS. Peers: standalone except Marico and Tata Consumer (consolidated). Periods: Apr–Mar FY.").font = Font(name="Arial", italic=True, size=9, color="808080")
ws4.merge_cells("A2:P2")

# ATLAS section
ws4.cell(4, 1, "ATLAS (Nestlé India) — Standalone").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws4.merge_cells("A4:E4")
header_row(ws4, 5, range(1, 6), ["Metric", "CY2022 (Jan–Dec)", "FY2025 (Apr–Mar)", "FY2026 (Apr–Mar)", "FY25→FY26 YoY"])
atlas_is = [
    ("Revenue (Cr)",    16897, 20260, 23155, (23155-20260)/20260),
    ("EBITDA (Cr)",     None,  4770,  5306,  (5306-4770)/4770),
    ("EBITDA Margin",   None,  0.235, 0.229, None),
    ("PAT (Cr)",        2391,  3315,  3545,  (3545-3315)/3315),
    ("PAT Margin",      0.141, 0.164, 0.153, None),
]
for i, (metric, cy22, fy25, fy26, yoy) in enumerate(atlas_is, 6):
    is_pct = "Margin" in metric
    fmt_val = "0.0%" if is_pct else "#,##0"
    bg = LIGHT_BLUE if i % 2 == 0 else WHITE
    data_cell(ws4, i, 1, metric, bg=bg, bold=True, align="left")
    for c, v in enumerate([cy22, fy25, fy26], 2):
        data_cell(ws4, i, c, v if v is not None else "n/a", bg=bg, fmt=fmt_val if v is not None else None)
    data_cell(ws4, i, 5, yoy if yoy is not None else "—", bg=bg, fmt="0.0%" if yoy is not None else None)

# Peer section
ws4.cell(13, 1, "Peers — Three-Year Income Statement").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws4.merge_cells("A13:P13")
peer_cols = ["Company", "Rev FY23", "Rev FY24", "Rev FY25", "EBITDA FY23", "EBITDA FY24", "EBITDA FY25",
             "EM FY23", "EM FY24", "EM FY25", "PAT FY23", "PAT FY24", "PAT FY25",
             "PM FY23", "PM FY24", "PM FY25"]
header_row(ws4, 14, range(1, 17), peer_cols)

for i, row in enumerate(peer_is, 15):
    co, r23, r24, r25, e23, e24, e25, p23, p24, p25 = row
    bg = GREY_FILL if i % 2 == 0 else WHITE
    vals = [co, r23, r24, r25, e23, e24, e25,
            e23/r23, e24/r24, e25/r25,
            p23, p24, p25,
            p23/r23, p24/r24, p25/r25]
    fmts = ["","#,##0","#,##0","#,##0","#,##0","#,##0","#,##0",
            "0.0%","0.0%","0.0%","#,##0","#,##0","#,##0","0.0%","0.0%","0.0%"]
    for c, (v, f) in enumerate(zip(vals, fmts), 1):
        data_cell(ws4, i, c, v, bg=bg, fmt=f, align="left" if c == 1 else "center")

set_col_widths(ws4, [16] + [9]*15)


# ── Sheet 5: Balance Sheet ───────────────────────────────────────────────────
ws5 = wb.create_sheet("5. Balance Sheet FY2025")
ws5.sheet_view.showGridLines = False

title_cell(ws5, 1, 1, "Balance Sheet Summary — Year Ended 31 March 2025")
ws5.cell(1,1).font = TITLE_FNT
ws5.merge_cells("A1:G1")
ws5.cell(2, 1, "INR Crore. [TV] = To Verify: item not confirmed from primary filing.").font = Font(name="Arial", italic=True, size=9, color="808080")
ws5.merge_cells("A2:G2")

header_row(ws5, 4, range(1, 8), ["Company", "Total Assets", "Total Equity", "Total Debt", "Cash", "Net Debt / (Cash)", "Capex"])
for i, (co, ta, eq, td, cash, nd, cx) in enumerate(bs_data, 5):
    bg = CYAN if co == "ATLAS" else (GREY_FILL if i % 2 == 0 else WHITE)
    bold = co == "ATLAS"
    vals = [co, ta, eq if eq else "[TV]", td, cash, nd, cx if cx else "[TV]"]
    fmts = ["","#,##0","#,##0","#,##0","#,##0","#,##0","#,##0"]
    for c, (v, f) in enumerate(zip(vals, fmts), 1):
        is_tv = v == "[TV]"
        data_cell(ws5, i, c, v, bg=bg, bold=bold,
                  fmt=f if not is_tv else None,
                  align="left" if c == 1 else "center")
        if is_tv:
            ws5.cell(i, c).fill = fill("FFE0E0")
    if co == "ATLAS":
        for c in [2, 6]:
            ws5.cell(i, c).fill = fill(YELLOW)

set_col_widths(ws5, [16, 12, 12, 10, 10, 14, 10])


# ── Sheet 6: Growth ──────────────────────────────────────────────────────────
ws6 = wb.create_sheet("6. Growth Rates")
ws6.sheet_view.showGridLines = False

title_cell(ws6, 1, 1, "Revenue and EBITDA Growth — FY2023 to FY2025 (Peers)")
ws6.cell(1,1).font = TITLE_FNT
ws6.merge_cells("A1:H1")
ws6.cell(2, 1, "INR Crore. 2-year CAGR. ATLAS excluded (different fiscal year convention); see Sheet 4 for ATLAS growth.").font = Font(name="Arial", italic=True, size=9, color="808080")
ws6.merge_cells("A2:H2")

header_row(ws6, 4, range(1, 9), ["Company", "Rev FY23 (Cr)", "Rev FY25 (Cr)", "Rev CAGR", "EBITDA FY23 (Cr)", "EBITDA FY25 (Cr)", "EBITDA CAGR", "EBITDA Margin Improvement"])
for i, (co, r23, r25, rc, e23, e25, ec) in enumerate(cagr_data, 5):
    bg = GREY_FILL if i % 2 == 0 else WHITE
    em_chg = (e25/r25) - (e23/r23)
    vals = [co, r23, r25, rc, e23, e25, ec, em_chg]
    fmts = ["","#,##0","#,##0","0.0%","#,##0","#,##0","0.0%","0.0pp"]
    for c, (v, f) in enumerate(zip(vals, fmts), 1):
        data_cell(ws6, i, c, v, bg=bg, fmt=f if "pp" not in f else "0.0%", align="left" if c == 1 else "center")

# ATLAS YoY
ws6.cell(11, 1, "ATLAS — Year-on-Year Growth (FY2025 to FY2026)").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws6.merge_cells("A11:H11")
header_row(ws6, 12, range(1, 5), ["Metric", "FY2025 (Cr)", "FY2026 (Cr)", "YoY Growth"])
atlas_growth = [
    ("Revenue",  20260, 23155, (23155-20260)/20260),
    ("EBITDA",    4770,  5306, (5306-4770)/4770),
    ("PAT",       3315,  3545, (3545-3315)/3315),
]
for i, (m, v25, v26, g) in enumerate(atlas_growth, 13):
    bg = CYAN
    data_cell(ws6, i, 1, m, bg=bg, bold=True, align="left")
    data_cell(ws6, i, 2, v25, bg=bg, bold=True, fmt="#,##0")
    data_cell(ws6, i, 3, v26, bg=bg, bold=True, fmt="#,##0")
    data_cell(ws6, i, 4, g, bg=bg, bold=True, fmt="0.0%")

set_col_widths(ws6, [18, 12, 12, 10, 14, 14, 12, 16])


# ── Sheet 7: DCF ─────────────────────────────────────────────────────────────
ws7 = wb.create_sheet("7. DCF (Illustrative)")
ws7.sheet_view.showGridLines = False

ws7.cell(1, 1, "Illustrative DCF Analysis — ATLAS").font = TITLE_FNT
ws7.merge_cells("A1:F1")
ws7.cell(2, 1, "For Illustrative Purposes and Reference Only. Analyst assumptions — NOT company guidance or management projections.").font = Font(name="Arial", italic=True, size=9, color="B01F5F")
ws7.merge_cells("A2:F2")

# Assumptions
ws7.cell(4, 1, "Key Assumptions").font = Font(name="Arial", bold=True, size=10, color=NAVY)
assumptions = [
    ("Base Revenue (FY2026 LTM)", "INR 23,155 Cr (standalone)"),
    ("Forecast Horizon", "10 years (FY2027–FY2036)"),
    ("Revenue Growth — Phase 1 (FY2027–FY2030)", "13.5% p.a."),
    ("Revenue Growth — Phase 2 (FY2031–FY2034)", "10.0% p.a."),
    ("Revenue Growth — Phase 3 (FY2035–FY2036)", "7.0% p.a."),
    ("EBITDA Margin", "22.9% (FY2027), expanding to 24.2% by FY2033"),
    ("Capex", "8.5% of revenue p.a. (FY2025 observed ratio)"),
    ("Depreciation and Amortisation", "2.6% of revenue p.a."),
    ("Effective Tax Rate", "25.2%"),
    ("NWC Change", "(0.5%) of revenue p.a. (net cash inflow)"),
    ("Net Debt (bridge)", "INR 677 Cr (March 2025 balance sheet)"),
    ("Shares Outstanding", "1,928.31 million (post August 2025 bonus)"),
    ("Terminal Value Method", "Gordon Growth Model"),
    ("WACC Range", "11.0% – 13.0%"),
    ("Terminal Growth Rate Range", "5.0% – 6.0%"),
    ("Risk-Free Rate", "7.2% (10-yr GOI bond, September 2026)"),
    ("Equity Risk Premium", "5.5%"),
    ("Beta Range", "0.75 – 0.95"),
]
for i, (k, v) in enumerate(assumptions, 5):
    ws7.cell(i, 1, k).font = Font(name="Arial", bold=True, size=9)
    ws7.cell(i, 1).alignment = left()
    ws7.cell(i, 2, v).font = BODY_FNT
    ws7.cell(i, 2).alignment = left()
    bg = LIGHT_BLUE if i % 2 == 0 else WHITE
    ws7.cell(i, 1).fill = fill(bg)
    ws7.cell(i, 2).fill = fill(bg)

# Sensitivity Grid
r0 = len(assumptions) + 7
ws7.cell(r0, 1, "Sensitivity — Implied Value per Share (INR)").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws7.merge_cells(f"A{r0}:E{r0}")

header_row(ws7, r0+1, range(1, 6), ["WACC \\ TGR", "TGR = 5.0%", "TGR = 5.5%", "TGR = 6.0%", "Note"])
waccs = [0.11, 0.12, 0.13]
tgrs  = [0.050, 0.055, 0.060]
for i, w in enumerate(waccs, r0+2):
    ws7.cell(i, 1, f"WACC = {w:.0%}").font = Font(name="Arial", bold=True, size=9)
    ws7.cell(i, 1).fill = fill(NAVY); ws7.cell(i, 1).font = Font(name="Arial", bold=True, color=WHITE, size=9)
    ws7.cell(i, 1).alignment = center()
    for j, t in enumerate(tgrs, 2):
        val = dcf_grid[(w, t)]
        is_base = (w == 0.12 and t == 0.055)
        c = ws7.cell(i, j, val)
        c.fill = fill(YELLOW) if is_base else fill(LIGHT_BLUE if i % 2 == 0 else WHITE)
        c.font = Font(name="Arial", bold=is_base, size=9)
        c.alignment = center()
        c.number_format = "#,##0"
        c.border = thin_border()
    note = "← BASE CASE" if w == 0.12 else ""
    ws7.cell(i, 5, note).font = Font(name="Arial", italic=True, size=9, color="808080")

# Base case summary
r1 = r0 + 6
ws7.cell(r1, 1, "Base Case Detail (WACC 12%, TGR 5.5%)").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws7.merge_cells(f"A{r1}:E{r1}")
base_rows = [
    ("PV of FCFFs",               dcf_base["PV_FCFFs"], "#,##0"),
    ("PV of Terminal Value",      dcf_base["PV_TV"],    "#,##0"),
    ("TV as % of Enterprise Value", dcf_base["TV_pct"], "0.0%"),
    ("Enterprise Value (DCF)",    dcf_base["EV"],       "#,##0"),
    ("Equity Value (DCF)",        dcf_base["Equity"],   "#,##0"),
    ("Implied Value per Share",   dcf_base["Price_per_share"], "#,##0"),
    ("Current Market Price",      dcf_base["Current_price"],   "#,##0.00"),
    ("Premium of Current Price to DCF Base", dcf_base["Premium"], "0.0%"),
]
for i, (k, v, f) in enumerate(base_rows, r1+1):
    bg = YELLOW if "Value per Share" in k or "Enterprise Value" in k else (LIGHT_BLUE if i%2==0 else WHITE)
    data_cell(ws7, i, 1, k, bg=bg, bold=("Value" in k or "Enterprise" in k), align="left")
    data_cell(ws7, i, 2, v, bg=bg, bold=True, fmt=f)

set_col_widths(ws7, [38, 12, 12, 12, 14])


# ── Sheet 8: Valuation Summary ───────────────────────────────────────────────
ws8 = wb.create_sheet("8. Valuation Summary")
ws8.sheet_view.showGridLines = False

ws8.cell(1, 1, "Preliminary Valuation Perspective — ATLAS").font = TITLE_FNT
ws8.merge_cells("A1:F1")
ws8.cell(2, 1, "For Illustrative Purposes and Reference Only. Does not constitute a fairness opinion. Market data: 25 September 2026.").font = Font(name="Arial", italic=True, size=9, color="B01F5F")
ws8.merge_cells("A2:F2")

header_row(ws8, 4, range(1, 7), ["Methodology", "Low (INR/share)", "High (INR/share)", "Midpoint (INR/share)", "Current Price (INR)", "Basis"])
for i, (meth, lo, hi, basis) in enumerate(val_data, 5):
    mid = round((lo + hi) / 2)
    bg = LIGHT_BLUE if i % 2 == 0 else WHITE
    data_cell(ws8, i, 1, meth, bg=bg, bold=True, align="left")
    data_cell(ws8, i, 2, lo,   bg=bg, fmt="#,##0")
    data_cell(ws8, i, 3, hi,   bg=bg, fmt="#,##0")
    data_cell(ws8, i, 4, mid,  bg=bg, fmt="#,##0", bold=True)
    data_cell(ws8, i, 5, 1362.60, bg=bg, fmt="#,##0.00", bold=True)
    data_cell(ws8, i, 6, basis, bg=bg, align="left")
    ws8.cell(i, 4).fill = fill(YELLOW)

# Supporting checks
ws8.cell(9, 1, "Multiple Context at Current Price").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws8.merge_cells("A9:F9")
checks = [
    ("EV/EBITDA at current price",       "49.6x"),
    ("Peer median EV/EBITDA",            "39.3x"),
    ("Premium to peer median EV/EBITDA", "+26%"),
    ("P/E at current price",             "74.1x"),
    ("Peer median P/E",                  "55.3x"),
    ("Premium to peer median P/E",       "+34%"),
    ("Current price vs EV/EBITDA comp high", "+1.3%"),
    ("Current price vs P/E comp high",   "(2.0%)"),
    ("Current price vs DCF base case",   "+339%"),
]
for i, (k, v) in enumerate(checks, 10):
    bg = YELLOW if "Premium" in k else (LIGHT_BLUE if i % 2 == 0 else WHITE)
    data_cell(ws8, i, 1, k, bg=bg, bold=False, align="left")
    data_cell(ws8, i, 2, v, bg=bg, bold=True)

set_col_widths(ws8, [28, 14, 14, 14, 14, 50])


# ── Sheet 9: To Verify ───────────────────────────────────────────────────────
ws9 = wb.create_sheet("9. To Verify")
ws9.sheet_view.showGridLines = False

ws9.cell(1, 1, "[TO VERIFY] Items — Must Resolve Before Design Build").font = Font(name="Arial", bold=True, size=12, color="B01F5F")
ws9.merge_cells("A1:D1")

header_row(ws9, 3, range(1, 5), ["Item", "Entity", "Period", "Issue / Source Needed"], bg="B01F5F")
to_verify = [
    ("EBITDA",                      "ATLAS",           "CY2022",   "Not sourced from primary filing. Check Nestlé India Annual Report CY2022 cash flow statement."),
    ("Gross profit",                "All peers",       "FY2025",   "Cost of materials not sourced for HUL, Britannia, Marico, Dabur, TCPL. Check each company's P&L."),
    ("Total equity",                "Marico",          "FY2025",   "Approximate only (~INR 8,300 Cr). Confirm from Marico FY2025 consolidated balance sheet."),
    ("Capex",                       "Marico",          "FY2025",   "Not confirmed from filing. Check Marico FY2025 consolidated cash flow statement."),
    ("Capex",                       "Tata Consumer",   "FY2025",   "Not confirmed from filing. Check TCPL FY2025 consolidated cash flow statement."),
    ("EBITDA (exact audited)",      "HUL",             "FY2025",   "Derived from 23.6% margin estimate. Confirm from HUL FY2025 standalone P&L or annual report."),
    ("Total debt (classification)", "HUL",             "FY2025",   "Lease liability classification assumed. Confirm non-lease financial borrowings from HUL balance sheet notes."),
]
for i, row in enumerate(to_verify, 4):
    item, ent, per, issue = row
    ws9.cell(i, 1, item).fill = fill("FFE0E0"); ws9.cell(i, 1).font = Font(name="Arial", bold=True, size=9)
    ws9.cell(i, 2, ent).fill  = fill("FFE0E0"); ws9.cell(i, 2).font = BODY_FNT
    ws9.cell(i, 3, per).fill  = fill("FFE0E0"); ws9.cell(i, 3).font = BODY_FNT
    ws9.cell(i, 4, issue).fill = fill("FFF9F9"); ws9.cell(i, 4).font = BODY_FNT
    for c in range(1, 5):
        ws9.cell(i, c).alignment = left()
        ws9.cell(i, c).border = thin_border()

ws9.cell(12, 1, "Slides Dropped (Completeness Rule — 5 slides excluded)").font = Font(name="Arial", bold=True, size=10, color=NAVY)
ws9.merge_cells("A12:D12")
header_row(ws9, 13, range(1, 4), ["Slide Considered", "Reason Dropped", "Data to Reinstate"], bg=NAVY)
dropped = [
    ("VWAP / price bucket", "Exchange VWAP tape not public without terminal", "NSE VWAP data by price bucket, 52-week, all six entities"),
    ("Broker target price table", "Named dated broker reports not confirmed for all six", "Bloomberg BVAL or named broker targets for all six"),
    ("Precedent transaction premia", "No verified India F&B control transactions in public domain", "5+ comparable India FMCG deals with values and unaffected prices"),
    ("Gross margin benchmarking", "COGS not sourced for five peers", "Cost of goods sold from full P&L for each peer"),
    ("RoE / ROCE panel", "Marico equity unverified; need all five peers confirmed", "Audited equity and capital employed for all six entities"),
]
for i, (sl, re, da) in enumerate(dropped, 14):
    bg = GREY_FILL if i % 2 == 0 else WHITE
    for c, v in enumerate([sl, re, da], 1):
        ws9.cell(i, c, v).fill = fill(bg)
        ws9.cell(i, c).font = BODY_FNT
        ws9.cell(i, c).alignment = left()
        ws9.cell(i, c).border = thin_border()

set_col_widths(ws9, [30, 18, 12, 60])

# Final save
output_path = r"d:\BOOKS\Research Papers\CODES\pichbook\ATLAS_DataPack.xlsx"
wb.save(output_path)
print(f"Saved: {output_path}")
print("Sheets: 1.Checks | 2.Capitalisation | 3.Trading Multiples | 4.Income Statement | 5.Balance Sheet FY2025 | 6.Growth Rates | 7.DCF (Illustrative) | 8.Valuation Summary | 9.To Verify")
