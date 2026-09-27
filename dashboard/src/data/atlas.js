/**
 * ATLAS (Nestlé India) — Pitchbook Data Layer
 * All figures INR Crore unless stated. Market Data Date: 25 September 2026.
 */

export const MARKET_DATE = "25 September 2026";

export const companies = [
  { name: "ATLAS", ticker: "NESTLEIND", isTarget: true },
  { name: "HUL", ticker: "HINDUNILVR", isTarget: false },
  { name: "Britannia", ticker: "BRITANNIA", isTarget: false },
  { name: "Marico", ticker: "MARICO", isTarget: false },
  { name: "Dabur", ticker: "DABUR", isTarget: false },
  { name: "Tata Consumer", ticker: "TATACONSUM", isTarget: false },
];

// ── Capitalisation Table ──
export const capTable = [
  { company: "ATLAS", ticker: "NESTLEIND", price: 1362.60, sharesMn: 1928.31, mktCap: 262752, debt: 753, cash: 76, ev: 263429, high52: 1553.00, low52: 1145.00, vsHigh: -0.123, dps: 14.00 },
  { company: "HUL", ticker: "HINDUNILVR", price: 1942.90, sharesMn: 2350.00, mktCap: 455000, debt: 1647, cash: 6071, ev: 450576, high52: 2667.20, low52: 1915.00, vsHigh: -0.272, dps: 41.00 },
  { company: "Britannia", ticker: "BRITANNIA", price: 4939.00, sharesMn: 240.87, mktCap: 117905, debt: 1225, cash: 38, ev: 119092, high52: 6271.00, low52: 4883.35, vsHigh: -0.213, dps: 90.50 },
  { company: "Marico", ticker: "MARICO", price: 819.00, sharesMn: 1293.90, mktCap: 106338, debt: 554, cash: 2150, ev: 104742, high52: 889.10, low52: 690.30, vsHigh: -0.079, dps: 4.00 },
  { company: "Dabur", ticker: "DABUR", price: 385.60, sharesMn: 1771.50, mktCap: 68404, debt: 730, cash: 2272, ev: 66862, high52: 534.00, low52: 368.05, vsHigh: -0.278, dps: 8.25 },
  { company: "Tata Consumer", ticker: "TATACONSUM", price: 983.00, sharesMn: 989.50, mktCap: 97307, debt: 2393, cash: 1430, ev: 98269, high52: 1282.70, low52: 979.20, vsHigh: -0.234, dps: 10.00 },
];

// ── EV Bridge Checks ──
export const evBridge = [
  { company: "ATLAS", mktCap: 262752.0, netDebt: 677.2, evDerived: 263429.2, evStored: 263429.2, pass: true },
  { company: "HUL", mktCap: 455000.0, netDebt: -4424.0, evDerived: 450576.0, evStored: 450576.0, pass: true },
  { company: "Britannia", mktCap: 117905.0, netDebt: 1186.8, evDerived: 119091.8, evStored: 119091.8, pass: true },
  { company: "Marico", mktCap: 106338.0, netDebt: -1596.0, evDerived: 104742.0, evStored: 104742.0, pass: true },
  { company: "Dabur", mktCap: 68404.0, netDebt: -1541.7, evDerived: 66862.3, evStored: 66862.3, pass: true },
  { company: "Tata Consumer", mktCap: 97307.0, netDebt: 962.3, evDerived: 98269.3, evStored: 98269.3, pass: true },
];

// ── Trading Multiples ──
export const tradingMultiples = [
  { company: "ATLAS", ltm: "FY2026", evEbitda: 49.6, pe: 74.1, evRev: 11.38, ebitdaMargin: 0.229, patMargin: 0.153 },
  { company: "HUL", ltm: "FY2025", evEbitda: 31.5, pe: 44.3, evRev: 7.44, ebitdaMargin: 0.236, patMargin: 0.170 },
  { company: "Britannia", ltm: "FY2025", evEbitda: 42.9, pe: 55.3, evRev: 6.89, ebitdaMargin: 0.161, patMargin: 0.123 },
  { company: "Marico", ltm: "FY2025", evEbitda: 49.0, pe: 64.1, evRev: 9.67, ebitdaMargin: 0.197, patMargin: 0.153 },
  { company: "Dabur", ltm: "FY2025", evEbitda: 28.9, pe: 39.3, evRev: 5.32, ebitdaMargin: 0.184, patMargin: 0.139 },
  { company: "Tata Consumer", ltm: "FY2025", evEbitda: 39.3, pe: 75.6, evRev: 5.58, ebitdaMargin: 0.142, patMargin: 0.073 },
];

// ── Financial detail for charts ──
export const financials = {
  ATLAS: { ev: 263429, ebitda: 5306, pat: 3545, revenue: 23155 },
  HUL: { ev: 450576, ebitda: 14296, pat: 10282, revenue: 60573 },
  Britannia: { ev: 119092, ebitda: 2779, pat: 2131, revenue: 17296 },
  Marico: { ev: 104742, ebitda: 2138, pat: 1658, revenue: 10831 },
  Dabur: { ev: 66862, ebitda: 2316, pat: 1740, revenue: 12563 },
  "Tata Consumer": { ev: 98269, ebitda: 2502, pat: 1287, revenue: 17618 },
};

// ── Income Statement ──
export const atlasIS = [
  { metric: "Revenue", cy22: 16897, fy25: 20260, fy26: 23155, yoy: (23155 - 20260) / 20260 },
  { metric: "EBITDA", cy22: null, fy25: 4770, fy26: 5306, yoy: (5306 - 4770) / 4770 },
  { metric: "EBITDA Margin", cy22: null, fy25: 0.235, fy26: 0.229, yoy: null, isPct: true },
  { metric: "PAT", cy22: 2391, fy25: 3315, fy26: 3545, yoy: (3545 - 3315) / 3315 },
  { metric: "PAT Margin", cy22: 0.141, fy25: 0.164, fy26: 0.153, yoy: null, isPct: true },
];

export const peerIS = [
  { company: "HUL", fy23: { rev: 59549, ebitda: 14272, pat: 9962 }, fy24: { rev: 60966, ebitda: 14476, pat: 10114 }, fy25: { rev: 60573, ebitda: 14296, pat: 10282 } },
  { company: "Britannia", fy23: { rev: 15618, ebitda: 2547, pat: 2139 }, fy24: { rev: 16186, ebitda: 2800, pat: 2082 }, fy25: { rev: 17296, ebitda: 2779, pat: 2131 } },
  { company: "Marico", fy23: { rev: 9764, ebitda: 1810, pat: 1322 }, fy24: { rev: 9653, ebitda: 1993, pat: 1502 }, fy25: { rev: 10831, ebitda: 2138, pat: 1658 } },
  { company: "Dabur", fy23: { rev: 11530, ebitda: 2164, pat: 1701 }, fy24: { rev: 12404, ebitda: 2400, pat: 1811 }, fy25: { rev: 12563, ebitda: 2316, pat: 1740 } },
  { company: "Tata Consumer", fy23: { rev: 13783, ebitda: 1874, pat: 1204 }, fy24: { rev: 15206, ebitda: 2323, pat: 1150 }, fy25: { rev: 17618, ebitda: 2502, pat: 1287 } },
];

// ── Balance Sheet FY2025 ──
export const balanceSheet = [
  { company: "ATLAS", totalAssets: 12324, totalEquity: 4117, totalDebt: 753, cash: 76, netDebt: 677, capex: 1811 },
  { company: "HUL", totalAssets: 79880, totalEquity: 49609, totalDebt: 1647, cash: 6071, netDebt: -4424, capex: 1211 },
  { company: "Britannia", totalAssets: 8020, totalEquity: 3887, totalDebt: 1225, cash: 38, netDebt: 1187, capex: 375 },
  { company: "Marico", totalAssets: 8300, totalEquity: null, totalDebt: 554, cash: 2150, netDebt: -1596, capex: null },
  { company: "Dabur", totalAssets: 11006, totalEquity: 10801, totalDebt: 730, cash: 2272, netDebt: -1542, capex: 570 },
  { company: "Tata Consumer", totalAssets: 31978, totalEquity: 23189, totalDebt: 2393, cash: 1430, netDebt: 963, capex: null },
];

// ── Growth Rates ──
export const peerGrowth = [
  { company: "HUL", revFY23: 59549, revFY25: 60573, revCAGR: 0.009, ebitdaFY23: 14272, ebitdaFY25: 14296, ebitdaCAGR: 0.001 },
  { company: "Britannia", revFY23: 15618, revFY25: 17296, revCAGR: 0.052, ebitdaFY23: 2547, ebitdaFY25: 2779, ebitdaCAGR: 0.044 },
  { company: "Marico", revFY23: 9764, revFY25: 10831, revCAGR: 0.053, ebitdaFY23: 1810, ebitdaFY25: 2138, ebitdaCAGR: 0.086 },
  { company: "Dabur", revFY23: 11530, revFY25: 12563, revCAGR: 0.044, ebitdaFY23: 2164, ebitdaFY25: 2316, ebitdaCAGR: 0.035 },
  { company: "Tata Consumer", revFY23: 13783, revFY25: 17618, revCAGR: 0.131, ebitdaFY23: 1874, ebitdaFY25: 2502, ebitdaCAGR: 0.156 },
];

export const atlasGrowth = [
  { metric: "Revenue", fy25: 20260, fy26: 23155, yoy: (23155 - 20260) / 20260 },
  { metric: "EBITDA", fy25: 4770, fy26: 5306, yoy: (5306 - 4770) / 4770 },
  { metric: "PAT", fy25: 3315, fy26: 3545, yoy: (3545 - 3315) / 3315 },
];

// ── DCF ──
export const dcfAssumptions = [
  { label: "Base Revenue (FY2026 LTM)", value: "INR 23,155 Cr (standalone)" },
  { label: "Forecast Horizon", value: "10 years (FY2027–FY2036)" },
  { label: "Revenue Growth — Phase 1 (FY2027–FY2030)", value: "13.5% p.a." },
  { label: "Revenue Growth — Phase 2 (FY2031–FY2034)", value: "10.0% p.a." },
  { label: "Revenue Growth — Phase 3 (FY2035–FY2036)", value: "7.0% p.a." },
  { label: "EBITDA Margin", value: "22.9% → 24.2% by FY2033" },
  { label: "Capex", value: "8.5% of revenue p.a." },
  { label: "D&A", value: "2.6% of revenue p.a." },
  { label: "Effective Tax Rate", value: "25.2%" },
  { label: "NWC Change", value: "(0.5%) of revenue p.a." },
  { label: "Net Debt (bridge)", value: "INR 677 Cr (March 2025 BS)" },
  { label: "Shares Outstanding", value: "1,928.31 million (post Aug 2025 bonus)" },
  { label: "Terminal Value Method", value: "Gordon Growth Model" },
  { label: "WACC Range", value: "11.0% – 13.0%" },
  { label: "Terminal Growth Rate Range", value: "5.0% – 6.0%" },
  { label: "Risk-Free Rate", value: "7.2% (10-yr GOI bond, Sep 2026)" },
  { label: "Equity Risk Premium", value: "5.5%" },
  { label: "Beta Range", value: "0.75 – 0.95" },
];

export const dcfSensitivity = {
  waccs: [0.11, 0.12, 0.13],
  tgrs: [0.050, 0.055, 0.060],
  grid: {
    "11-5.0": 350, "11-5.5": 371, "11-6.0": 397,
    "12-5.0": 296, "12-5.5": 310, "12-6.0": 327,
    "13-5.0": 255, "13-5.5": 265, "13-6.0": 277,
  },
  baseCase: { wacc: 0.12, tgr: 0.055 },
};

export const dcfBase = {
  pvFCFFs: 24254,
  pvTV: 36208,
  tvPct: 0.599,
  ev: 60462,
  equity: 59785,
  pricePerShare: 310,
  currentPrice: 1362.60,
  premium: 3.395,
};

// ── Valuation Summary ──
export const valuationRange = [
  { method: "EV/EBITDA Comps", low: 791, high: 1345, basis: "Peer range 28.9x–49.0x × ATLAS FY2026 EBITDA ₹5,306 Cr" },
  { method: "P/E Comps", low: 722, high: 1390, basis: "Peer range 39.3x–75.6x × ATLAS FY2026 PAT ₹3,545 Cr" },
  { method: "DCF (Illustrative)", low: 255, high: 397, basis: "WACC 11–13%, TGR 5–6%; analyst assumptions only" },
];

export const currentPrice = 1362.60;

export const multipleContext = [
  { label: "EV/EBITDA at current price", value: "49.6x" },
  { label: "Peer median EV/EBITDA", value: "39.3x" },
  { label: "Premium to peer median EV/EBITDA", value: "+26%", isHighlight: true },
  { label: "P/E at current price", value: "74.1x" },
  { label: "Peer median P/E", value: "55.3x" },
  { label: "Premium to peer median P/E", value: "+34%", isHighlight: true },
  { label: "Current price vs EV/EBITDA comp high", value: "+1.3%" },
  { label: "Current price vs P/E comp high", value: "(2.0%)" },
  { label: "Current price vs DCF base case", value: "+339%", isHighlight: true },
];
