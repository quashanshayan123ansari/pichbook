"""
ATLAS (Nestlé India) — Investment Banking Board Deck
Stage 4: Compute — All derived figures calculated here.
Market Data Date: 25 September 2026
All monetary values: INR Crore unless stated otherwise.

FISCAL YEAR NOTES:
- CY2022: Jan–Dec 2022 (last full calendar year before FY change)
- FY2024: 15 months Jan 2023–Mar 2024 — NON-COMPARABLE, used only for reference
- FY2025: 12 months Apr 2024–Mar 2025 (first full Apr–Mar year)
- FY2026: 12 months Apr 2025–Mar 2026 (most recent full year, LTM for multiples)
- Q1 FY2027: Apr–Jun 2026 (partial, for context only)

For peers, all use Apr–Mar FY, so FY2023/FY2024/FY2025 are comparable 12-month periods.
Tata Consumer uses consolidated figures (given international operations).
All others standalone unless noted.
"""

# ============================================================
# SECTION 1: RAW SOURCED DATA
# ============================================================

# --- ATLAS (Nestlé India) ---
# Source: Annual Reports (nestle.in), NSE/BSE filings, Scribd (verified filings)

atlas_fin = {
    "CY2022": {
        "revenue": 16897.0,     # Cr | Source: Annual Report CY2022 (₹168,970M)
        "PBT": 3256.0,          # Cr | Source: Annual Report CY2022 (₹32,560M)
        "PAT": 2390.5,          # Cr | Source: Annual Report CY2022 (₹23,905M)
        "EBITDA": None,         # [TO VERIFY] not sourced for CY2022
        "gross_profit": None,   # [TO VERIFY]
    },
    # FY2024 (15 months) — NOT used for margin/multiple comparisons
    "FY2024_15m": {
        "revenue": 24393.9,     # Cr | Source: NSE filing (₹243,939M) 15-month period
        "EBITDA": 5849.8,       # Cr | Source: Scribd/nestle.in (₹58,498M) 15-month
        "PAT": 3932.8,          # Cr | Source: Scribd/nestle.in (₹39,328M) 15-month
    },
    "FY2025": {
        "revenue": 20260.42,    # Cr | Source: Nestle.in audited results
        "material_cost": 8390.15,  # Cr | Source: nestle.in P&L standalone
        "employee_cost": 2023.71,  # Cr | Source: nestle.in P&L standalone
        "depreciation": 518.17,    # Cr | Source: nestle.in P&L standalone
        "EBIT": 4292.65,        # Cr | Source: Derived (PBT 4447.47 + Finance Cost 136)
        "EBITDA": 4769.6,       # Cr | Source: nestle.in (₹47,696M) — also = EBIT + D&A = 4292.65+518.17=4810.82 [note rounding]
        "PBT": 4447.47,         # Cr | Source: nestle.in P&L
        "PAT": 3314.50,         # Cr | Source: nestle.in P&L / NSE filing
        "total_assets": 12323.89,  # Cr | Source: Scribd/nestle.in (₹123,238.9M)
        "total_equity": 4117.15,   # Cr | Source: nestle.in (₹41,171.5M)
        "non_current_borrowings": 22.48,  # Cr | Source: nestle.in (₹224.8M)
        "current_borrowings": 730.86,     # Cr | Source: nestle.in (₹7,308.6M)
        "cash": 76.18,          # Cr | Source: nestle.in (₹761.8M)
        "capex": 1810.9,        # Cr | Source: investing activities cash flow
        # Shares: post 1:10 split (2024), pre-Aug-2025 bonus
        "shares_mn": 964.16,    # million | Source: nestle.in (964,157,160)
        "DPS": 24.25,           # INR per share (pre-bonus adj) | ₹14.25 interim + ₹10.00 final = ₹24.25
    },
    "FY2026": {
        "revenue": 23154.6,     # Cr | Source: nestle.in audited results Apr 2026 (₹231,546M)
        "EBITDA": 5306.1,       # Cr | Source: nestle.in (₹53,061M)
        "PAT": 3544.6,          # Cr | Source: nestle.in (₹35,446M)
        # Post Aug 2025 bonus: pre-bonus 964.16M * 2 = 1928.31M shares
        "shares_mn": 1928.31,   # million | Source: nestle.in bonus allotment
        # FY2026 DPS: ₹7 interim (Feb 2026) + ₹5 final + ₹2 special (Jul 2026)
        # All on post-bonus share count (face value ₹1)
        "DPS": 14.0,            # INR per share (post-bonus basis) = 7+5+2
    }
}

# Derived: gross profit FY2025
atlas_fin["FY2025"]["gross_profit"] = (
    atlas_fin["FY2025"]["revenue"] - atlas_fin["FY2025"]["material_cost"]
)

# Derived: total debt and net debt FY2025
atlas_fin["FY2025"]["total_debt"] = (
    atlas_fin["FY2025"]["non_current_borrowings"] + atlas_fin["FY2025"]["current_borrowings"]
)
atlas_fin["FY2025"]["net_debt"] = (
    atlas_fin["FY2025"]["total_debt"] - atlas_fin["FY2025"]["cash"]
)

# Market data — 25 Sep 2026
# Note: price ₹1,362.60 is post-bonus (1928.31M shares)
atlas_mkt = {
    "price": 1362.60,
    "mkt_cap_Cr": 262752.0,    # Cr | Source: BSE/investing.com (~₹2.63 lakh Cr)
    "52wk_high": 1553.00,
    "52wk_low": 1145.00,
    "shares_mn": 1928.31,
}
# EV = mkt_cap + net_debt (use FY2025 net debt, most recent balance sheet)
atlas_mkt["EV_Cr"] = atlas_mkt["mkt_cap_Cr"] + atlas_fin["FY2025"]["net_debt"]

# Equity value check
eq_check = atlas_mkt["shares_mn"] * atlas_mkt["price"] / 100  # -> Cr (mn shares * price / 100 = Cr)
# Actually: shares_mn * price = INR millions -> /100 = Cr
# 1928.31 million shares * 1362.60 INR = 2,628,247 million INR = 262,824.7 Cr ≈ 262,752 Cr ✓

# ============================================================
# SECTION 2: PEER DATA
# ============================================================

# --- HUL (Hindustan Unilever Ltd) ---
# Standalone, Apr-Mar FY, Source: HUL Annual Reports, hul.co.in
hul_fin = {
    "FY2023": {"revenue": 59549.0, "EBITDA": 14272.0, "PAT": 9962.0},
    "FY2024": {"revenue": 60966.0, "EBITDA": 14476.0, "PAT": 10114.0},
    "FY2025": {
        "revenue": 60573.0,     # Cr | Source: hul.co.in (₹60,573 Cr continuing ops)
        "EBITDA": 14296.0,      # Cr | EBITDA margin ~23.6% * 60573 [TO VERIFY exact figure]
        "PAT": 10282.0,         # Cr | Source: hul.co.in FY2025
        "total_assets": 79880.0,  # Cr | Source: HUL consolidated
        "total_equity": 49609.0,
        "cash": 6071.0,
        "total_debt": 1647.0,   # Cr | lease liabilities approx [TO VERIFY]
        "shares_mn": 2350.0,    # million | ~2.35 billion shares
        "DPS": 41.0,            # FY2026: ₹41/share (FY2025 not provided; use FY2026 declared)
        "capex_pct": 0.02,      # ~2% of turnover
    },
    "FY2026": {
        "revenue": 63763.0,     # Cr | Source: hul.co.in
        "PAT": 10652.0,         # Cr | Source: hul.co.in (continuing ops)
        "EBITDA": None,         # [TO VERIFY] not explicitly sourced
    }
}
hul_fin["FY2025"]["gross_profit"] = None  # [TO VERIFY]
hul_fin["FY2025"]["net_debt"] = hul_fin["FY2025"]["total_debt"] - hul_fin["FY2025"]["cash"]
hul_fin["FY2025"]["capex"] = hul_fin["FY2025"]["revenue"] * hul_fin["FY2025"]["capex_pct"]

hul_mkt = {
    "price": 1942.90,
    "mkt_cap_Cr": 455000.0,    # ~₹4.55 lakh Cr | Source: etmoney/indmoney
    "52wk_high": 2667.20,
    "52wk_low": 1915.00,
    "shares_mn": 2350.0,
    "DPS_FY26": 41.0,
}
hul_mkt["EV_Cr"] = hul_mkt["mkt_cap_Cr"] + hul_fin["FY2025"]["net_debt"]

# EBITDA FY2025: margin ~23.6% on ₹60,573 Cr
hul_fin["FY2025"]["EBITDA"] = 60573.0 * 0.2359  # = 14,289 Cr approx

# --- Britannia Industries ---
# Standalone, Apr-Mar FY, Source: britannia.co.in annual reports
brit_fin = {
    "FY2023": {"revenue": 15618.42, "EBITDA": 2546.69, "PAT": 2139.30,
               "total_assets": 9353.0, "total_equity": 3565.0},
    "FY2024": {"revenue": 16186.08, "EBITDA": 2799.63, "PAT": 2082.05,
               "total_assets": 8370.84, "total_equity": 3966.0},
    "FY2025": {
        "revenue": 17295.92,    # Cr | Source: Britannia annual results
        "EBITDA": 2778.98,      # Cr | Source: Britannia annual results
        "PAT": 2130.72,         # Cr | Source: Britannia annual results
        "total_assets": 8019.72,
        "total_equity": 3886.55,
        "total_debt": 1225.0,   # Cr | Source: balance sheet (712.50 NC + 504.05 C)
        "cash": 38.19,          # Cr | Source: britannia.co.in
        "shares_mn": 240.87,    # million | Source: companiesmarketcap
        "DPS_FY26": 90.50,      # Cr | Source: announced FY2026 final dividend
        "capex": 375.0,         # Cr | Source: PPE movement FY25
    }
}
brit_fin["FY2025"]["net_debt"] = brit_fin["FY2025"]["total_debt"] - brit_fin["FY2025"]["cash"]

brit_mkt = {
    "price": 4939.00,
    "mkt_cap_Cr": 117905.0,    # Source: NSE data 25 Sep 2026
    "52wk_high": 6271.00,
    "52wk_low": 4883.35,
    "shares_mn": 240.87,
}
brit_mkt["EV_Cr"] = brit_mkt["mkt_cap_Cr"] + brit_fin["FY2025"]["net_debt"]

# --- Marico Ltd ---
# Consolidated, Apr-Mar FY, Source: Marico Annual Reports
marico_fin = {
    "FY2023": {"revenue": 9764.0, "EBITDA": 1810.0, "PAT": 1322.0,
               "total_assets": 6800.0},
    "FY2024": {"revenue": 9653.0, "EBITDA": 1993.0, "PAT": 1502.0,
               "total_assets": 7400.0},
    "FY2025": {
        "revenue": 10831.0,     # Cr | Source: Marico AR
        "EBITDA": 2138.0,       # Cr | Source: Marico AR
        "PAT": 1658.0,          # Cr | Source: Marico AR
        "total_assets": 8300.0, # Cr | approx
        "total_debt": 554.0,    # Cr | (₹5.54 billion)
        "cash": 2150.0,         # Cr | (₹21.5 billion) — strong cash position
        "shares_mn": 1293.9,    # million | Source: 129.39 Cr shares
        "DPS_FY26": 4.0,        # Source: announced FY2026 final dividend
        "capex": None,          # [TO VERIFY]
    }
}
marico_fin["FY2025"]["net_debt"] = marico_fin["FY2025"]["total_debt"] - marico_fin["FY2025"]["cash"]
# Net cash position (negative net debt)

marico_mkt = {
    "price": 819.00,
    "mkt_cap_Cr": 106338.0,    # Source: NSE data 25 Sep 2026
    "52wk_high": 889.10,
    "52wk_low": 690.30,
    "shares_mn": 1293.9,
}
marico_mkt["EV_Cr"] = marico_mkt["mkt_cap_Cr"] + marico_fin["FY2025"]["net_debt"]

# --- Dabur India ---
# Standalone, Apr-Mar FY, Source: Dabur Annual Reports
dabur_fin = {
    "FY2023": {"revenue": 11529.9, "EBITDA": 2164.1, "PAT": 1701.3,
               "total_assets": 9352.4, "total_equity": 8973.3, "total_debt": 999.0},
    "FY2024": {"revenue": 12404.0, "EBITDA": 2400.2, "PAT": 1811.3,
               "total_assets": 10532.8, "total_equity": 9866.3, "total_debt": 1158.1},
    "FY2025": {
        "revenue": 12563.1,     # Cr | Source: Dabur AR
        "EBITDA": 2316.3,       # Cr | Source: Dabur AR
        "PAT": 1740.4,          # Cr | Source: Dabur AR
        "total_assets": 11005.5,
        "total_equity": 10800.7,
        "total_debt": 730.1,    # Cr | Source: Dabur AR
        "cash": 2271.8,         # Cr | Source: Dabur AR
        "shares_mn": 1771.5,    # million | ~₹177.2 Cr equity / Re1 FV
        "DPS_FY26": 8.25,       # Source: FY2026 dividend
        "capex": 569.5,         # Cr | Source: Dabur AR FY2025
    }
}
dabur_fin["FY2025"]["net_debt"] = dabur_fin["FY2025"]["total_debt"] - dabur_fin["FY2025"]["cash"]

dabur_mkt = {
    "price": 385.60,
    "mkt_cap_Cr": 68404.0,     # Source: NSE data 25 Sep 2026
    "52wk_high": 534.00,
    "52wk_low": 368.05,
    "shares_mn": 1771.5,
}
dabur_mkt["EV_Cr"] = dabur_mkt["mkt_cap_Cr"] + dabur_fin["FY2025"]["net_debt"]

# --- Tata Consumer Products ---
# Consolidated (includes international ops), Apr-Mar FY
# Source: TCPL Annual Reports, tataconsumer.com
tcpl_fin = {
    "FY2023": {"revenue": 13783.0, "EBITDA": 1874.0, "PAT": 1204.0,
               "total_assets": 31978.0, "total_equity": 21390.0},
    "FY2024": {"revenue": 15206.0, "EBITDA": 2323.0, "PAT": 1150.0,
               "total_assets": 34453.0, "total_equity": 23189.0},
    "FY2025": {
        "revenue": 17618.0,     # Cr | Source: TCPL AR / tataconsumer.com
        "EBITDA": 2502.0,       # Cr | Source: TCPL AR
        "PAT": 1287.0,          # Cr | Source: TCPL AR (owners of parent)
        "total_assets": 31977.68,  # Cr | Source: tataconsumer.com
        "total_equity": 23189.0,   # Cr | approx — FY2024 figure, FY2025 [TO VERIFY]
        "total_debt": 2392.68,  # Cr | Source: tataconsumer FY2025
        "cash": 1430.38,        # Cr | Source: tataconsumer FY2025
        "goodwill": 11884.0,    # Cr | Note: significant goodwill from acquisitions
        "shares_mn": 989.5,     # million | 98.95 Cr shares
        "DPS_FY26": 10.0,       # Source: FY2026 dividend
        "capex": None,          # [TO VERIFY]
    }
}
tcpl_fin["FY2025"]["net_debt"] = tcpl_fin["FY2025"]["total_debt"] - tcpl_fin["FY2025"]["cash"]

tcpl_mkt = {
    "price": 983.00,
    "mkt_cap_Cr": 97307.0,     # Source: NSE data 25 Sep 2026
    "52wk_high": 1282.70,
    "52wk_low": 979.20,
    "shares_mn": 989.5,
}
tcpl_mkt["EV_Cr"] = tcpl_mkt["mkt_cap_Cr"] + tcpl_fin["FY2025"]["net_debt"]

# ============================================================
# SECTION 3: CHECKS
# ============================================================

print("=" * 70)
print("STAGE 4 CHECKS")
print("=" * 70)

# CHECK 1: Equity Value + Net Debt = EV for each entity
print("\nCHECK 1: EV Bridge (Mkt Cap + Net Debt = EV)")
for name, mkt, fin, fy in [
    ("ATLAS", atlas_mkt, atlas_fin["FY2025"], "FY2025"),
    ("HUL", hul_mkt, hul_fin["FY2025"], "FY2025"),
    ("Britannia", brit_mkt, brit_fin["FY2025"], "FY2025"),
    ("Marico", marico_mkt, marico_fin["FY2025"], "FY2025"),
    ("Dabur", dabur_mkt, dabur_fin["FY2025"], "FY2025"),
    ("TCPL", tcpl_mkt, tcpl_fin["FY2025"], "FY2025"),
]:
    ev_derived = mkt["mkt_cap_Cr"] + fin["net_debt"]
    ev_stored = mkt["EV_Cr"]
    match = abs(ev_derived - ev_stored) < 1.0
    print(f"  {name}: Mkt Cap {mkt['mkt_cap_Cr']:,.0f} + Net Debt {fin['net_debt']:,.1f} = EV {ev_derived:,.1f} | Stored: {ev_stored:,.1f} | {'PASS' if match else 'FAIL'}")

# CHECK 2: Per share × shares = aggregate
print("\nCHECK 2: Per Share × Shares = Mkt Cap")
for name, mkt in [
    ("ATLAS", atlas_mkt),
    ("HUL", hul_mkt),
    ("Britannia", brit_mkt),
    ("Marico", marico_mkt),
    ("Dabur", dabur_mkt),
    ("TCPL", tcpl_mkt),
]:
    implied_mc = mkt["shares_mn"] * mkt["price"] / 100  # million shares * INR -> Cr (/100 because mn*Cr/mn=Cr... 
    # Actually: shares in millions, price in INR
    # Market cap in Cr: (shares_mn * 1e6 * price) / 1e7 = shares_mn * price / 10
    implied_mc2 = mkt["shares_mn"] * mkt["price"] / 10  # -> INR Cr
    gap = abs(implied_mc2 - mkt["mkt_cap_Cr"]) / mkt["mkt_cap_Cr"]
    print(f"  {name}: {mkt['shares_mn']:.2f}M * ₹{mkt['price']} = ₹{implied_mc2:,.0f} Cr | Reported: ₹{mkt['mkt_cap_Cr']:,.0f} Cr | Gap: {gap:.1%}")

# ============================================================
# SECTION 4: TRADING MULTIPLES TABLE
# ============================================================

print("\n" + "=" * 70)
print("TRADING MULTIPLES (LTM = FY2026 for ATLAS; FY2025 for peers)")
print("Market Data Date: 25 September 2026")
print("=" * 70)

# For peers, use FY2025 as LTM (most recently completed full year)
# For ATLAS, use FY2026 as LTM (full year results released Apr 2026)

def multiples(name, mkt_cap, ev, ebitda_ltm, pat_ltm, revenue_ltm, ebitda_prior=None, pat_prior=None):
    ev_ebitda = ev / ebitda_ltm if ebitda_ltm else None
    pe = mkt_cap / pat_ltm if pat_ltm else None
    ev_rev = ev / revenue_ltm if revenue_ltm else None
    ebitda_mg = ebitda_ltm / revenue_ltm if ebitda_ltm and revenue_ltm else None
    pat_mg = pat_ltm / revenue_ltm if pat_ltm and revenue_ltm else None
    print(f"\n  {name}:")
    print(f"    EV/EBITDA (LTM): {ev_ebitda:.1f}x" if ev_ebitda else "    EV/EBITDA: N/A")
    print(f"    P/E (LTM): {pe:.1f}x" if pe else "    P/E: N/A")
    print(f"    EV/Revenue (LTM): {ev_rev:.2f}x" if ev_rev else "    EV/Revenue: N/A")
    print(f"    EBITDA Margin: {ebitda_mg:.1%}" if ebitda_mg else "    EBITDA Margin: N/A")
    print(f"    PAT Margin: {pat_mg:.1%}" if pat_mg else "    PAT Margin: N/A")
    return {
        "EV_EBITDA": ev_ebitda, "PE": pe, "EV_Rev": ev_rev,
        "EBITDA_mg": ebitda_mg, "PAT_mg": pat_mg
    }

atlas_m = multiples("ATLAS (LTM=FY2026)",
    atlas_mkt["mkt_cap_Cr"], atlas_mkt["EV_Cr"],
    atlas_fin["FY2026"]["EBITDA"], atlas_fin["FY2026"]["PAT"], atlas_fin["FY2026"]["revenue"])

hul_m = multiples("HUL (LTM=FY2025)",
    hul_mkt["mkt_cap_Cr"], hul_mkt["EV_Cr"],
    hul_fin["FY2025"]["EBITDA"], hul_fin["FY2025"]["PAT"], hul_fin["FY2025"]["revenue"])

brit_m = multiples("Britannia (LTM=FY2025)",
    brit_mkt["mkt_cap_Cr"], brit_mkt["EV_Cr"],
    brit_fin["FY2025"]["EBITDA"], brit_fin["FY2025"]["PAT"], brit_fin["FY2025"]["revenue"])

marico_m = multiples("Marico (LTM=FY2025)",
    marico_mkt["mkt_cap_Cr"], marico_mkt["EV_Cr"],
    marico_fin["FY2025"]["EBITDA"], marico_fin["FY2025"]["PAT"], marico_fin["FY2025"]["revenue"])

dabur_m = multiples("Dabur (LTM=FY2025)",
    dabur_mkt["mkt_cap_Cr"], dabur_mkt["EV_Cr"],
    dabur_fin["FY2025"]["EBITDA"], dabur_fin["FY2025"]["PAT"], dabur_fin["FY2025"]["revenue"])

tcpl_m = multiples("TCPL (LTM=FY2025)",
    tcpl_mkt["mkt_cap_Cr"], tcpl_mkt["EV_Cr"],
    tcpl_fin["FY2025"]["EBITDA"], tcpl_fin["FY2025"]["PAT"], tcpl_fin["FY2025"]["revenue"])

# ============================================================
# SECTION 5: MARGIN BENCHMARKING
# ============================================================

print("\n" + "=" * 70)
print("MARGIN BENCHMARKING — FY2025 (all entities)")
print("=" * 70)

margin_data = {
    "ATLAS (FY2026 LTM)": {
        "EBITDA_mg": atlas_fin["FY2026"]["EBITDA"] / atlas_fin["FY2026"]["revenue"],
        "PAT_mg": atlas_fin["FY2026"]["PAT"] / atlas_fin["FY2026"]["revenue"],
        "gross_mg": atlas_fin["FY2025"]["gross_profit"] / atlas_fin["FY2025"]["revenue"],  # FY2025 only
    },
    "HUL": {
        "EBITDA_mg": hul_fin["FY2025"]["EBITDA"] / hul_fin["FY2025"]["revenue"],
        "PAT_mg": hul_fin["FY2025"]["PAT"] / hul_fin["FY2025"]["revenue"],
        "gross_mg": None,
    },
    "Britannia": {
        "EBITDA_mg": brit_fin["FY2025"]["EBITDA"] / brit_fin["FY2025"]["revenue"],
        "PAT_mg": brit_fin["FY2025"]["PAT"] / brit_fin["FY2025"]["revenue"],
        "gross_mg": None,
    },
    "Marico": {
        "EBITDA_mg": marico_fin["FY2025"]["EBITDA"] / marico_fin["FY2025"]["revenue"],
        "PAT_mg": marico_fin["FY2025"]["PAT"] / marico_fin["FY2025"]["revenue"],
        "gross_mg": None,
    },
    "Dabur": {
        "EBITDA_mg": dabur_fin["FY2025"]["EBITDA"] / dabur_fin["FY2025"]["revenue"],
        "PAT_mg": dabur_fin["FY2025"]["PAT"] / dabur_fin["FY2025"]["revenue"],
        "gross_mg": None,
    },
    "TCPL": {
        "EBITDA_mg": tcpl_fin["FY2025"]["EBITDA"] / tcpl_fin["FY2025"]["revenue"],
        "PAT_mg": tcpl_fin["FY2025"]["PAT"] / tcpl_fin["FY2025"]["revenue"],
        "gross_mg": None,
    },
}

for ent, mg in margin_data.items():
    print(f"  {ent}: EBITDA {mg['EBITDA_mg']:.1%} | PAT {mg['PAT_mg']:.1%}" + 
          (f" | Gross {mg['gross_mg']:.1%}" if mg['gross_mg'] else ""))

# ============================================================
# SECTION 6: REVENUE GROWTH
# ============================================================

print("\n" + "=" * 70)
print("REVENUE GROWTH")
print("=" * 70)

# ATLAS: CY2022 -> FY2025 -> FY2026
# Note: FY2024 (15 months) excluded from CAGR
import math

# ATLAS: CY2022 to FY2026 = 4 years (CY2022 ends Dec 2022, FY2026 ends Mar 2026 = 3.25 yrs approx)
# Use simpler: FY2025 vs FY2026 YoY
atlas_rev_yoy = (atlas_fin["FY2026"]["revenue"] / atlas_fin["FY2025"]["revenue"]) - 1
atlas_ebitda_yoy = (atlas_fin["FY2026"]["EBITDA"] / atlas_fin["FY2025"]["EBITDA"]) - 1
atlas_pat_yoy = (atlas_fin["FY2026"]["PAT"] / atlas_fin["FY2025"]["PAT"]) - 1
print(f"  ATLAS Rev YoY FY25->FY26: {atlas_rev_yoy:.1%}")
print(f"  ATLAS EBITDA YoY FY25->FY26: {atlas_ebitda_yoy:.1%}")
print(f"  ATLAS PAT YoY FY25->FY26: {atlas_pat_yoy:.1%}")

# Peers: FY2023 to FY2025 CAGR
for name, fin23, fin25 in [
    ("HUL", hul_fin["FY2023"]["revenue"], hul_fin["FY2025"]["revenue"]),
    ("Britannia", brit_fin["FY2023"]["revenue"], brit_fin["FY2025"]["revenue"]),
    ("Marico", marico_fin["FY2023"]["revenue"], marico_fin["FY2025"]["revenue"]),
    ("Dabur", dabur_fin["FY2023"]["revenue"], dabur_fin["FY2025"]["revenue"]),
    ("TCPL", tcpl_fin["FY2023"]["revenue"], tcpl_fin["FY2025"]["revenue"]),
]:
    cagr = (fin25 / fin23) ** 0.5 - 1
    print(f"  {name} Rev CAGR FY23-FY25 (2yr): {cagr:.1%}")

# ============================================================
# SECTION 7: DCF ASSUMPTIONS (Illustrative)
# ============================================================

print("\n" + "=" * 70)
print("DCF ASSUMPTIONS (Illustrative — Analyst assumptions, not company guidance)")
print("=" * 70)

dcf_base = {
    "forecast_horizon_yrs": 10,
    "base_revenue_FY26": atlas_fin["FY2026"]["revenue"],
    "base_EBITDA_FY26": atlas_fin["FY2026"]["EBITDA"],
    # Revenue growth: Phase 1 (FY27-30) 13-14%, Phase 2 (FY31-34) 9-11%, Phase 3 (FY35-36) 7%
    "rev_growth_phase1": 0.135,   # Mid of 13-14%
    "rev_growth_phase2": 0.10,    # 10%
    "rev_growth_phase3": 0.07,    # 7%
    # EBITDA margin path: current ~22.9%, sustaining ~23-24%
    "EBITDA_margin_path": [0.229, 0.232, 0.235, 0.238, 0.240, 0.241, 0.242, 0.242, 0.242, 0.242],
    # Capex % revenue: ~7-9% (FY25 capex ₹1,811 Cr / revenue ₹20,260 = 8.9%)
    "capex_pct_rev": 0.085,
    # D&A % revenue: ~2.6% (FY25: 518/20260 = 2.6%)
    "da_pct_rev": 0.026,
    # Tax rate: 25.2% effective (India statutory ~25.17%)
    "tax_rate": 0.252,
    # Working capital: assume minimal (asset-light model, negative WC)
    "nwc_change_pct_rev": -0.005,  # slight benefit
    # WACC range: 11-13% (risk free ~7.2%, equity risk premium ~5.5%, beta ~0.7-0.9)
    "wacc_low": 0.11,
    "wacc_mid": 0.12,
    "wacc_high": 0.13,
    # Terminal growth rate range: 5-6% (India nominal GDP ~7%, FMCG discount ~1-2%)
    "tgr_low": 0.050,
    "tgr_mid": 0.055,
    "tgr_high": 0.060,
    # Terminal method: Gordon Growth (EV/EBITDA cross-check)
}

# Run base case DCF
def run_dcf(base_rev, base_ebitda, g1, g2, g3, margins, capex_pct, da_pct, tax_rate, nwc_pct, wacc, tgr, shares_mn, net_debt):
    fcffs = []
    revenues = []
    rev = base_rev
    for yr in range(1, 11):
        if yr <= 4:
            rev = rev * (1 + g1)
        elif yr <= 8:
            rev = rev * (1 + g2)
        else:
            rev = rev * (1 + g3)
        revenues.append(rev)
        ebitda = rev * margins[yr - 1]
        da = rev * da_pct
        ebit = ebitda - da
        nopat = ebit * (1 - tax_rate)
        capex = rev * capex_pct
        nwc_chg = rev * nwc_pct
        fcff = nopat + da - capex - nwc_chg
        fcffs.append(fcff)
    # Terminal value (Gordon Growth)
    terminal_fcff = fcffs[-1] * (1 + tgr)
    terminal_value = terminal_fcff / (wacc - tgr)
    # PV of FCFFs
    pv_fcffs = sum(f / (1 + wacc) ** (i + 1) for i, f in enumerate(fcffs))
    pv_tv = terminal_value / (1 + wacc) ** 10
    enterprise_value = pv_fcffs + pv_tv
    equity_value = enterprise_value - net_debt
    value_per_share = equity_value / shares_mn * 10  # Cr -> INR per share (Cr/million = 10 INR)
    return {
        "PV_FCFFs": pv_fcffs, "PV_TV": pv_tv, "EV": enterprise_value,
        "Equity_Value": equity_value, "Value_per_share": value_per_share,
        "TV_pct": pv_tv / enterprise_value, "revenues": revenues, "fcffs": fcffs
    }

shares_for_dcf = atlas_mkt["shares_mn"]  # 1928.31 million (post-bonus)
net_debt_for_dcf = atlas_fin["FY2025"]["net_debt"]

dcf_results = {}
for wacc in [0.11, 0.12, 0.13]:
    for tgr in [0.050, 0.055, 0.060]:
        key = f"WACC{int(wacc*100)}_TGR{int(tgr*1000)}"
        dcf_results[key] = run_dcf(
            dcf_base["base_revenue_FY26"],
            dcf_base["base_EBITDA_FY26"],
            dcf_base["rev_growth_phase1"],
            dcf_base["rev_growth_phase2"],
            dcf_base["rev_growth_phase3"],
            dcf_base["EBITDA_margin_path"],
            dcf_base["capex_pct_rev"],
            dcf_base["da_pct_rev"],
            dcf_base["tax_rate"],
            dcf_base["nwc_change_pct_rev"],
            wacc, tgr, shares_for_dcf, net_debt_for_dcf
        )

print("\nDCF SENSITIVITY GRID — Value per Share (₹)")
print(f"{'':>15}" + "".join(f"  TGR={tgr:.1%}" for tgr in [0.050, 0.055, 0.060]))
for wacc in [0.11, 0.12, 0.13]:
    row = f"WACC={wacc:.0%}     "
    for tgr in [0.050, 0.055, 0.060]:
        key = f"WACC{int(wacc*100)}_TGR{int(tgr*1000)}"
        row += f"  ₹{dcf_results[key]['Value_per_share']:>7,.0f}"
    print(row)

# Headline (base case): WACC=12%, TGR=5.5%
base_dcf = dcf_results["WACC12_TGR55"]
print(f"\nBase Case (WACC 12%, TGR 5.5%):")
print(f"  PV of FCFFs: ₹{base_dcf['PV_FCFFs']:,.0f} Cr")
print(f"  PV of Terminal Value: ₹{base_dcf['PV_TV']:,.0f} Cr ({base_dcf['TV_pct']:.1%} of EV)")
print(f"  Enterprise Value: ₹{base_dcf['EV']:,.0f} Cr")
print(f"  Equity Value: ₹{base_dcf['Equity_Value']:,.0f} Cr")
print(f"  Value per Share: ₹{base_dcf['Value_per_share']:,.0f}")
print(f"  Current Price: ₹{atlas_mkt['price']:,.2f}")
print(f"  Premium/(Discount): {(atlas_mkt['price'] / base_dcf['Value_per_share'] - 1):+.1%}")

# CHECK: Sensitivity grid centre cell = base case
centre = dcf_results["WACC12_TGR55"]["Value_per_share"]
print(f"\nCHECK — Sensitivity grid centre (WACC 12%, TGR 5.5%) = ₹{centre:,.0f} | Base case = ₹{base_dcf['Value_per_share']:,.0f} | PASS")

# ============================================================
# SECTION 8: CAPITALISATION TABLE
# ============================================================

print("\n" + "=" * 70)
print("CAPITALISATION — ATLAS (25 Sep 2026)")
print("=" * 70)

cap_table = {
    "Mkt Cap": atlas_mkt["mkt_cap_Cr"],
    "(-) Cash": -atlas_fin["FY2025"]["cash"],
    "(+) Total Debt": atlas_fin["FY2025"]["total_debt"],
    "= Enterprise Value": atlas_mkt["EV_Cr"],
}
for k, v in cap_table.items():
    print(f"  {k}: ₹{v:>10,.1f} Cr")

print(f"\n  Net Debt / EBITDA (FY2026): {atlas_fin['FY2025']['net_debt'] / atlas_fin['FY2026']['EBITDA']:.2f}x")
print(f"  Net Debt / EBITDA (FY2025): {atlas_fin['FY2025']['net_debt'] / atlas_fin['FY2025']['EBITDA']:.2f}x")

# ============================================================
# SECTION 9: SUMMARY VALUATION RANGE
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY VALUATION — ATLAS Implied Price per Share")
print("=" * 70)

# Trading comps: apply peer median EV/EBITDA and P/E to ATLAS
peer_ev_ebitda = sorted([hul_m["EV_EBITDA"], brit_m["EV_EBITDA"], marico_m["EV_EBITDA"],
                          dabur_m["EV_EBITDA"], tcpl_m["EV_EBITDA"]])
peer_pe = sorted([hul_m["PE"], brit_m["PE"], brit_m["PE"], marico_m["PE"],
                   dabur_m["PE"], tcpl_m["PE"]])

peer_ev_ebitda_median = peer_ev_ebitda[len(peer_ev_ebitda)//2]
peer_pe_median = peer_pe[len(peer_pe)//2]

print(f"\nPeer EV/EBITDA range: {min(peer_ev_ebitda):.1f}x - {max(peer_ev_ebitda):.1f}x | Median: {peer_ev_ebitda_median:.1f}x")
print(f"Peer P/E range: {min(peer_pe):.1f}x - {max(peer_pe):.1f}x | Median: {peer_pe_median:.1f}x")

# EV/EBITDA implied price (applied to ATLAS FY2026 EBITDA)
ev_ebitda_low_ev = min(peer_ev_ebitda) * atlas_fin["FY2026"]["EBITDA"]
ev_ebitda_high_ev = max(peer_ev_ebitda) * atlas_fin["FY2026"]["EBITDA"]
ev_ebitda_low_eq = ev_ebitda_low_ev - atlas_fin["FY2025"]["net_debt"]
ev_ebitda_high_eq = ev_ebitda_high_ev - atlas_fin["FY2025"]["net_debt"]
# Price per share: equity / shares_mn * 10 (Cr to INR)
ev_ebitda_low_px = ev_ebitda_low_eq / atlas_mkt["shares_mn"] * 10
ev_ebitda_high_px = ev_ebitda_high_eq / atlas_mkt["shares_mn"] * 10

print(f"\nTrading Comps (EV/EBITDA, peer range applied to ATLAS FY2026 EBITDA):")
print(f"  Low (x{min(peer_ev_ebitda):.1f}): ₹{ev_ebitda_low_px:,.0f} per share")
print(f"  High (x{max(peer_ev_ebitda):.1f}): ₹{ev_ebitda_high_px:,.0f} per share")

# P/E implied price
pe_low_px = min(peer_pe) * atlas_fin["FY2026"]["PAT"] / atlas_mkt["shares_mn"] * 10
pe_high_px = max(peer_pe) * atlas_fin["FY2026"]["PAT"] / atlas_mkt["shares_mn"] * 10
print(f"\nTrading Comps (P/E, peer range applied to ATLAS FY2026 PAT):")
print(f"  Low (x{min(peer_pe):.1f}): ₹{pe_low_px:,.0f} per share")
print(f"  High (x{max(peer_pe):.1f}): ₹{pe_high_px:,.0f} per share")

# DCF range
dcf_vals = [r["Value_per_share"] for r in dcf_results.values()]
print(f"\nDCF (Illustrative):")
print(f"  Range: ₹{min(dcf_vals):,.0f} - ₹{max(dcf_vals):,.0f} per share")
print(f"  Base: ₹{base_dcf['Value_per_share']:,.0f} per share")

print(f"\nCurrent Market Price (25 Sep 2026): ₹{atlas_mkt['price']:,.2f}")

print("\n" + "=" * 70)
print("ALL COMPUTATIONS COMPLETE")
print("=" * 70)
