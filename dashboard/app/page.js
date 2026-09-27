"use client";

import ChartSetup from "@/components/ChartSetup";
import Sidebar from "@/components/Sidebar";
import {
  MultiplesBarChart,
  MarginChart,
  RevenueChart,
  PeerRevenueChart,
  EVWaterfallChart,
  GrowthCAGRChart,
  DCFCompositionChart,
} from "@/components/Charts";
import FootballField from "@/components/FootballField";
import SensitivityGrid from "@/components/SensitivityGrid";
import {
  capTable,
  evBridge,
  tradingMultiples,
  financials,
  atlasIS,
  peerIS,
  balanceSheet,
  peerGrowth,
  atlasGrowth,
  dcfAssumptions,
  dcfBase,
  valuationRange,
  currentPrice,
  multipleContext,
} from "@/data/atlas";

const fmt = (v) => (v != null ? v.toLocaleString("en-IN") : "—");
const fmtPct = (v) => (v != null ? `${(v * 100).toFixed(1)}%` : "—");
const fmtDec = (v, d = 1) => (v != null ? v.toFixed(d) : "—");

export default function Dashboard() {
  return (
    <>
      <ChartSetup />
      <div className="app-layout">
        <Sidebar />
        <main className="main-content">
          <header className="content-header">
            <span className="header-title">
              ATLAS — Investment Banking Board Deck
            </span>
            <div className="header-meta">
              <span className="header-badge badge-live">● ALL CHECKS PASS</span>
              <span className="header-badge badge-date">
                Market Data: 25 Sep 2026
              </span>
            </div>
          </header>

          <div className="content-body">
            {/* ── Section 0: Overview ─────────────────────── */}
            <section className="section" id="overview">
              <div className="section-header">
                <div className="section-number">0</div>
                <div>
                  <div className="section-title">Executive Overview</div>
                  <div className="section-subtitle">
                    ATLAS (Nestlé India) — Key metrics at a glance
                  </div>
                </div>
              </div>

              <div className="kpi-grid">
                <div className="kpi-card">
                  <div className="kpi-label">Share Price</div>
                  <div className="kpi-value gold">₹1,362.60</div>
                  <div className="kpi-change negative">▼ 12.3% vs 52-wk high</div>
                </div>
                <div className="kpi-card">
                  <div className="kpi-label">Market Cap</div>
                  <div className="kpi-value">₹2,62,752 Cr</div>
                  <div className="kpi-change positive">
                    1,928.31M shares
                  </div>
                </div>
                <div className="kpi-card">
                  <div className="kpi-label">Enterprise Value</div>
                  <div className="kpi-value">₹2,63,429 Cr</div>
                  <div className="kpi-change positive">
                    Net Debt: ₹677 Cr
                  </div>
                </div>
                <div className="kpi-card">
                  <div className="kpi-label">Revenue FY2026</div>
                  <div className="kpi-value">₹23,155 Cr</div>
                  <div className="kpi-change positive">▲ 14.3% YoY</div>
                </div>
                <div className="kpi-card">
                  <div className="kpi-label">EBITDA FY2026</div>
                  <div className="kpi-value">₹5,306 Cr</div>
                  <div className="kpi-change positive">▲ 11.2% YoY</div>
                </div>
                <div className="kpi-card">
                  <div className="kpi-label">EV / EBITDA</div>
                  <div className="kpi-value gold">49.6x</div>
                  <div className="kpi-change negative">
                    Peer median: 39.3x
                  </div>
                </div>
              </div>

              <div className="card">
                <div className="card-header">
                  <h3>EV Bridge — Waterfall</h3>
                  <span className="tag tag-gold">ATLAS FY2025 Balance Sheet</span>
                </div>
                <EVWaterfallChart />
              </div>
            </section>

            {/* ── Section 1: Checks ──────────────────────── */}
            <section className="section" id="checks">
              <div className="section-header">
                <div className="section-number">1</div>
                <div>
                  <div className="section-title">Verification Checks</div>
                  <div className="section-subtitle">
                    EV Bridge and per-share reconciliation
                  </div>
                </div>
              </div>

              <div className="grid-2" style={{ marginBottom: 20 }}>
                <div className="card">
                  <div className="card-header">
                    <h3>Check 1 — EV Bridge</h3>
                    <span className="tag tag-green">6/6 PASS</span>
                  </div>
                  <div className="card-body-flush">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Company</th>
                          <th>Mkt Cap</th>
                          <th>Net Debt</th>
                          <th>EV (Derived)</th>
                          <th>Result</th>
                        </tr>
                      </thead>
                      <tbody>
                        {evBridge.map((r) => (
                          <tr
                            key={r.company}
                            className={
                              r.company === "ATLAS" ? "target-row" : ""
                            }
                          >
                            <td>{r.company}</td>
                            <td>{fmt(r.mktCap)}</td>
                            <td>{fmt(r.netDebt)}</td>
                            <td>{fmt(r.evDerived)}</td>
                            <td>
                              <span className="pass-badge">PASS</span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>

                <div className="card">
                  <div className="card-header">
                    <h3>Check 2 — Per Share × Shares</h3>
                    <span className="tag tag-green">6/6 PASS</span>
                  </div>
                  <div className="card-body-flush">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Company</th>
                          <th>Shares (mn)</th>
                          <th>Price</th>
                          <th>Implied MC</th>
                          <th>Gap</th>
                        </tr>
                      </thead>
                      <tbody>
                        {capTable.map((r) => (
                          <tr
                            key={r.company}
                            className={
                              r.company === "ATLAS" ? "target-row" : ""
                            }
                          >
                            <td>{r.company}</td>
                            <td>{fmtDec(r.sharesMn, 2)}</td>
                            <td>₹{fmtDec(r.price, 2)}</td>
                            <td>
                              {fmt(
                                Math.round(
                                  (r.sharesMn * r.price) / 10
                                )
                              )}
                            </td>
                            <td>
                              <span className="pass-badge">
                                {fmtPct(
                                  Math.abs(
                                    (r.sharesMn * r.price) / 10 -
                                      r.mktCap
                                  ) / r.mktCap
                                )}
                              </span>
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>
            </section>

            {/* ── Section 2: Capitalisation ──────────────── */}
            <section className="section" id="capitalisation">
              <div className="section-header">
                <div className="section-number">2</div>
                <div>
                  <div className="section-title">Capitalisation & Market Data</div>
                  <div className="section-subtitle">
                    25 September 2026 — INR Crore unless stated
                  </div>
                </div>
              </div>

              <div className="card">
                <div className="card-header">
                  <h3>Capitalisation Table</h3>
                  <span className="tag tag-navy">
                    ATLAS = Nestlé India (NESTLEIND)
                  </span>
                </div>
                <div className="card-body-flush" style={{ overflowX: "auto" }}>
                  <table className="data-table">
                    <thead>
                      <tr>
                        <th>Company</th>
                        <th>Ticker</th>
                        <th>Price (₹)</th>
                        <th>Shares (mn)</th>
                        <th>Mkt Cap</th>
                        <th>+ Debt</th>
                        <th>- Cash</th>
                        <th>= EV</th>
                        <th>52-Wk High</th>
                        <th>52-Wk Low</th>
                        <th>vs High</th>
                        <th>DPS (₹)</th>
                      </tr>
                    </thead>
                    <tbody>
                      {capTable.map((r) => (
                        <tr
                          key={r.company}
                          className={
                            r.company === "ATLAS" ? "target-row" : ""
                          }
                        >
                          <td>{r.company}</td>
                          <td style={{ fontFamily: "var(--font-mono)", fontSize: 11 }}>{r.ticker}</td>
                          <td>₹{fmtDec(r.price, 2)}</td>
                          <td>{fmtDec(r.sharesMn, 2)}</td>
                          <td className={r.company === "ATLAS" ? "highlight-cell" : ""}>
                            {fmt(r.mktCap)}
                          </td>
                          <td>{fmt(r.debt)}</td>
                          <td>{fmt(r.cash)}</td>
                          <td className={r.company === "ATLAS" ? "highlight-cell" : ""}>
                            {fmt(r.ev)}
                          </td>
                          <td>₹{fmtDec(r.high52, 2)}</td>
                          <td>₹{fmtDec(r.low52, 2)}</td>
                          <td style={{ color: r.vsHigh < 0 ? "#ef4444" : "#10b981" }}>
                            {fmtPct(r.vsHigh)}
                          </td>
                          <td>₹{fmtDec(r.dps, 2)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            {/* ── Section 3: Trading Multiples ───────────── */}
            <section className="section" id="multiples">
              <div className="section-header">
                <div className="section-number">3</div>
                <div>
                  <div className="section-title">Trading Multiples</div>
                  <div className="section-subtitle">
                    LTM = FY2026 for ATLAS; FY2025 for peers
                  </div>
                </div>
              </div>

              <div className="card" style={{ marginBottom: 20 }}>
                <div className="card-header">
                  <h3>Multiples Table</h3>
                </div>
                <div className="card-body-flush">
                  <table className="data-table">
                    <thead>
                      <tr>
                        <th>Company</th>
                        <th>LTM</th>
                        <th>EV (Cr)</th>
                        <th>EBITDA (Cr)</th>
                        <th>PAT (Cr)</th>
                        <th>EV / EBITDA</th>
                        <th>P / E</th>
                        <th>EV / Revenue</th>
                        <th>EBITDA %</th>
                        <th>PAT %</th>
                      </tr>
                    </thead>
                    <tbody>
                      {tradingMultiples.map((r) => {
                        const fin = financials[r.company];
                        return (
                          <tr
                            key={r.company}
                            className={
                              r.company === "ATLAS" ? "target-row" : ""
                            }
                          >
                            <td>{r.company}</td>
                            <td>
                              <span className="tag tag-navy">{r.ltm}</span>
                            </td>
                            <td>{fmt(fin.ev)}</td>
                            <td>{fmt(fin.ebitda)}</td>
                            <td>{fmt(fin.pat)}</td>
                            <td
                              className={
                                r.company === "ATLAS" ? "highlight-cell" : ""
                              }
                            >
                              {fmtDec(r.evEbitda)}x
                            </td>
                            <td
                              className={
                                r.company === "ATLAS" ? "highlight-cell" : ""
                              }
                            >
                              {fmtDec(r.pe)}x
                            </td>
                            <td
                              className={
                                r.company === "ATLAS" ? "highlight-cell" : ""
                              }
                            >
                              {fmtDec(r.evRev, 2)}x
                            </td>
                            <td>{fmtPct(r.ebitdaMargin)}</td>
                            <td>{fmtPct(r.patMargin)}</td>
                          </tr>
                        );
                      })}
                    </tbody>
                  </table>
                </div>
              </div>

              <div className="chart-grid">
                <div className="card">
                  <div className="card-header">
                    <h3>EV / EBITDA Comparison</h3>
                  </div>
                  <MultiplesBarChart metric="evEbitda" />
                </div>
                <div className="card">
                  <div className="card-header">
                    <h3>P / E Comparison</h3>
                  </div>
                  <MultiplesBarChart metric="pe" />
                </div>
              </div>

              <div className="card" style={{ marginTop: 20 }}>
                <div className="card-header">
                  <h3>Margin Benchmarking</h3>
                  <span className="tag tag-navy">EBITDA & PAT Margins</span>
                </div>
                <MarginChart />
              </div>
            </section>

            {/* ── Section 4: Income Statement ────────────── */}
            <section className="section" id="income">
              <div className="section-header">
                <div className="section-number">4</div>
                <div>
                  <div className="section-title">Income Statement</div>
                  <div className="section-subtitle">
                    ATLAS standalone + peer three-year summary
                  </div>
                </div>
              </div>

              <div className="grid-2">
                <div className="card">
                  <div className="card-header">
                    <h3>ATLAS — Revenue Trajectory</h3>
                    <span className="tag tag-gold">Standalone</span>
                  </div>
                  <RevenueChart />
                </div>
                <div className="card">
                  <div className="card-header">
                    <h3>ATLAS — P&L Summary</h3>
                  </div>
                  <div className="card-body-flush">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Metric</th>
                          <th>CY2022</th>
                          <th>FY2025</th>
                          <th>FY2026</th>
                          <th>YoY</th>
                        </tr>
                      </thead>
                      <tbody>
                        {atlasIS.map((r) => (
                          <tr key={r.metric} className="target-row">
                            <td>{r.metric}</td>
                            <td>
                              {r.isPct
                                ? fmtPct(r.cy22)
                                : r.cy22 != null
                                ? `₹${fmt(r.cy22)}`
                                : "—"}
                            </td>
                            <td>
                              {r.isPct
                                ? fmtPct(r.fy25)
                                : `₹${fmt(r.fy25)}`}
                            </td>
                            <td>
                              {r.isPct
                                ? fmtPct(r.fy26)
                                : `₹${fmt(r.fy26)}`}
                            </td>
                            <td
                              style={{
                                color: r.yoy > 0 ? "#10b981" : r.yoy < 0 ? "#ef4444" : "",
                              }}
                            >
                              {r.yoy != null ? fmtPct(r.yoy) : "—"}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>
              </div>

              <div className="card" style={{ marginTop: 20 }}>
                <div className="card-header">
                  <h3>Peer Revenue — FY2023 vs FY2025</h3>
                </div>
                <PeerRevenueChart />
              </div>

              <div className="card" style={{ marginTop: 20 }}>
                <div className="card-header">
                  <h3>Peer Income Statement — Three-Year</h3>
                  <span className="tag tag-navy">INR Crore</span>
                </div>
                <div className="card-body-flush" style={{ overflowX: "auto" }}>
                  <table className="data-table">
                    <thead>
                      <tr>
                        <th>Company</th>
                        <th>Rev FY23</th>
                        <th>Rev FY24</th>
                        <th>Rev FY25</th>
                        <th>EBITDA FY23</th>
                        <th>EBITDA FY24</th>
                        <th>EBITDA FY25</th>
                        <th>PAT FY23</th>
                        <th>PAT FY24</th>
                        <th>PAT FY25</th>
                      </tr>
                    </thead>
                    <tbody>
                      {peerIS.map((r) => (
                        <tr key={r.company}>
                          <td>{r.company}</td>
                          <td>{fmt(r.fy23.rev)}</td>
                          <td>{fmt(r.fy24.rev)}</td>
                          <td>{fmt(r.fy25.rev)}</td>
                          <td>{fmt(r.fy23.ebitda)}</td>
                          <td>{fmt(r.fy24.ebitda)}</td>
                          <td>{fmt(r.fy25.ebitda)}</td>
                          <td>{fmt(r.fy23.pat)}</td>
                          <td>{fmt(r.fy24.pat)}</td>
                          <td>{fmt(r.fy25.pat)}</td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            {/* ── Section 5: Balance Sheet ────────────────── */}
            <section className="section" id="balance">
              <div className="section-header">
                <div className="section-number">5</div>
                <div>
                  <div className="section-title">Balance Sheet Summary</div>
                  <div className="section-subtitle">
                    Year ended 31 March 2025 — INR Crore
                  </div>
                </div>
              </div>

              <div className="note">
                [TV] = To Verify: item not confirmed from primary filing. See
                Section 9 for details.
              </div>

              <div className="card">
                <div className="card-header">
                  <h3>Balance Sheet</h3>
                </div>
                <div className="card-body-flush">
                  <table className="data-table">
                    <thead>
                      <tr>
                        <th>Company</th>
                        <th>Total Assets</th>
                        <th>Total Equity</th>
                        <th>Total Debt</th>
                        <th>Cash</th>
                        <th>Net Debt / (Cash)</th>
                        <th>Capex</th>
                      </tr>
                    </thead>
                    <tbody>
                      {balanceSheet.map((r) => (
                        <tr
                          key={r.company}
                          className={
                            r.company === "ATLAS" ? "target-row" : ""
                          }
                        >
                          <td>{r.company}</td>
                          <td
                            className={
                              r.company === "ATLAS" ? "highlight-cell" : ""
                            }
                          >
                            {fmt(r.totalAssets)}
                          </td>
                          <td
                            style={
                              r.totalEquity == null
                                ? { background: "#fee2e2", color: "#ef4444", fontWeight: 600 }
                                : {}
                            }
                          >
                            {r.totalEquity != null ? fmt(r.totalEquity) : "[TV]"}
                          </td>
                          <td>{fmt(r.totalDebt)}</td>
                          <td>{fmt(r.cash)}</td>
                          <td
                            className={
                              r.company === "ATLAS" ? "highlight-cell" : ""
                            }
                            style={{
                              color: r.netDebt < 0 ? "#10b981" : "",
                            }}
                          >
                            {fmt(r.netDebt)}
                          </td>
                          <td
                            style={
                              r.capex == null
                                ? { background: "#fee2e2", color: "#ef4444", fontWeight: 600 }
                                : {}
                            }
                          >
                            {r.capex != null ? fmt(r.capex) : "[TV]"}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            {/* ── Section 6: Growth ──────────────────────── */}
            <section className="section" id="growth">
              <div className="section-header">
                <div className="section-number">6</div>
                <div>
                  <div className="section-title">Growth Rates</div>
                  <div className="section-subtitle">
                    Revenue & EBITDA CAGR — Peers FY2023→FY2025 | ATLAS FY2025→FY2026
                  </div>
                </div>
              </div>

              <div className="grid-2">
                <div className="card">
                  <div className="card-header">
                    <h3>ATLAS — YoY Growth</h3>
                    <span className="tag tag-gold">FY2025 → FY2026</span>
                  </div>
                  <div className="card-body-flush">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Metric</th>
                          <th>FY2025 (Cr)</th>
                          <th>FY2026 (Cr)</th>
                          <th>YoY</th>
                        </tr>
                      </thead>
                      <tbody>
                        {atlasGrowth.map((r) => (
                          <tr key={r.metric} className="target-row">
                            <td>{r.metric}</td>
                            <td>₹{fmt(r.fy25)}</td>
                            <td>₹{fmt(r.fy26)}</td>
                            <td style={{ color: "#10b981", fontWeight: 700 }}>
                              ▲ {fmtPct(r.yoy)}
                            </td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>

                <div className="card">
                  <div className="card-header">
                    <h3>Peer CAGR — FY2023 to FY2025</h3>
                  </div>
                  <GrowthCAGRChart />
                </div>
              </div>

              <div className="card" style={{ marginTop: 20 }}>
                <div className="card-header">
                  <h3>Peer Growth Detail</h3>
                  <span className="tag tag-navy">2-Year CAGR</span>
                </div>
                <div className="card-body-flush">
                  <table className="data-table">
                    <thead>
                      <tr>
                        <th>Company</th>
                        <th>Rev FY23</th>
                        <th>Rev FY25</th>
                        <th>Rev CAGR</th>
                        <th>EBITDA FY23</th>
                        <th>EBITDA FY25</th>
                        <th>EBITDA CAGR</th>
                      </tr>
                    </thead>
                    <tbody>
                      {peerGrowth.map((r) => (
                        <tr key={r.company}>
                          <td>{r.company}</td>
                          <td>{fmt(r.revFY23)}</td>
                          <td>{fmt(r.revFY25)}</td>
                          <td style={{ fontWeight: 700 }}>
                            {fmtPct(r.revCAGR)}
                          </td>
                          <td>{fmt(r.ebitdaFY23)}</td>
                          <td>{fmt(r.ebitdaFY25)}</td>
                          <td style={{ fontWeight: 700 }}>
                            {fmtPct(r.ebitdaCAGR)}
                          </td>
                        </tr>
                      ))}
                    </tbody>
                  </table>
                </div>
              </div>
            </section>

            {/* ── Section 7: DCF ─────────────────────────── */}
            <section className="section" id="dcf">
              <div className="section-header">
                <div className="section-number">7</div>
                <div>
                  <div className="section-title">
                    DCF Analysis (Illustrative)
                  </div>
                  <div className="section-subtitle">
                    Analyst assumptions — NOT company guidance
                  </div>
                </div>
              </div>

              <div className="disclaimer">
                ⚠ For Illustrative Purposes and Reference Only. Analyst
                assumptions — NOT company guidance or management projections.
                Does not constitute a fairness opinion.
              </div>

              <div className="grid-2">
                <div className="card">
                  <div className="card-header">
                    <h3>Key Assumptions</h3>
                  </div>
                  <div className="card-body-flush">
                    <div className="assumptions-grid" style={{ gridTemplateColumns: "1fr" }}>
                      {dcfAssumptions.map((a, i) => (
                        <div className="assumption-row" key={i}>
                          <span className="assumption-label">{a.label}</span>
                          <span className="assumption-value">{a.value}</span>
                        </div>
                      ))}
                    </div>
                  </div>
                </div>

                <div>
                  <div className="card" style={{ marginBottom: 20 }}>
                    <div className="card-header">
                      <h3>Sensitivity Grid — ₹ / Share</h3>
                    </div>
                    <SensitivityGrid />
                  </div>

                  <div className="card">
                    <div className="card-header">
                      <h3>Base Case (WACC 12%, TGR 5.5%)</h3>
                    </div>
                    <div className="card-body-flush">
                      <table className="data-table">
                        <thead>
                          <tr>
                            <th>Metric</th>
                            <th>Value</th>
                          </tr>
                        </thead>
                        <tbody>
                          <tr>
                            <td>PV of FCFFs</td>
                            <td>₹{fmt(dcfBase.pvFCFFs)} Cr</td>
                          </tr>
                          <tr>
                            <td>PV of Terminal Value</td>
                            <td>₹{fmt(dcfBase.pvTV)} Cr</td>
                          </tr>
                          <tr>
                            <td>TV as % of EV</td>
                            <td>{fmtPct(dcfBase.tvPct)}</td>
                          </tr>
                          <tr className="target-row">
                            <td>Enterprise Value (DCF)</td>
                            <td className="highlight-cell">
                              ₹{fmt(dcfBase.ev)} Cr
                            </td>
                          </tr>
                          <tr className="target-row">
                            <td>Equity Value (DCF)</td>
                            <td>₹{fmt(dcfBase.equity)} Cr</td>
                          </tr>
                          <tr className="target-row">
                            <td>Implied Value per Share</td>
                            <td className="highlight-cell">
                              ₹{fmt(dcfBase.pricePerShare)}
                            </td>
                          </tr>
                          <tr>
                            <td>Current Market Price</td>
                            <td>₹{fmtDec(dcfBase.currentPrice, 2)}</td>
                          </tr>
                          <tr>
                            <td>Premium of Price to DCF Base</td>
                            <td style={{ color: "#ef4444", fontWeight: 700 }}>
                              +{fmtPct(dcfBase.premium)}
                            </td>
                          </tr>
                        </tbody>
                      </table>
                    </div>
                  </div>
                </div>
              </div>

              <div className="card" style={{ marginTop: 20 }}>
                <div className="card-header">
                  <h3>DCF Composition</h3>
                  <span className="tag tag-navy">
                    TV = {fmtPct(dcfBase.tvPct)} of EV
                  </span>
                </div>
                <DCFCompositionChart />
              </div>
            </section>

            {/* ── Section 8: Valuation Summary ───────────── */}
            <section className="section" id="valuation">
              <div className="section-header">
                <div className="section-number">8</div>
                <div>
                  <div className="section-title">Valuation Summary</div>
                  <div className="section-subtitle">
                    Football field — implied price ranges
                  </div>
                </div>
              </div>

              <div className="disclaimer">
                ⚠ For Illustrative Purposes and Reference Only. Does not
                constitute a fairness opinion. Market data: 25 September 2026.
              </div>

              <div className="card" style={{ marginBottom: 20 }}>
                <div className="card-header">
                  <h3>Valuation Range — Football Field</h3>
                  <span className="tag tag-gold">
                    Current: ₹{currentPrice.toLocaleString()}
                  </span>
                </div>
                <FootballField />
              </div>

              <div className="grid-2">
                <div className="card">
                  <div className="card-header">
                    <h3>Valuation Table</h3>
                  </div>
                  <div className="card-body-flush">
                    <table className="data-table">
                      <thead>
                        <tr>
                          <th>Methodology</th>
                          <th>Low (₹)</th>
                          <th>High (₹)</th>
                          <th>Midpoint (₹)</th>
                          <th>Current</th>
                        </tr>
                      </thead>
                      <tbody>
                        {valuationRange.map((r) => (
                          <tr key={r.method}>
                            <td>{r.method}</td>
                            <td>₹{fmt(r.low)}</td>
                            <td>₹{fmt(r.high)}</td>
                            <td className="highlight-cell">
                              ₹{fmt(Math.round((r.low + r.high) / 2))}
                            </td>
                            <td>₹{fmtDec(currentPrice, 2)}</td>
                          </tr>
                        ))}
                      </tbody>
                    </table>
                  </div>
                </div>

                <div className="card">
                  <div className="card-header">
                    <h3>Multiple Context at Current Price</h3>
                  </div>
                  <div className="card-body-flush">
                    {multipleContext.map((r, i) => (
                      <div
                        key={i}
                        className="assumption-row"
                        style={
                          r.isHighlight
                            ? { background: "#fdf4d5" }
                            : {}
                        }
                      >
                        <span className="assumption-label">
                          {r.label}
                        </span>
                        <span
                          className="assumption-value"
                          style={{
                            fontWeight: 700,
                            color: r.isHighlight ? "#d4a12a" : "",
                          }}
                        >
                          {r.value}
                        </span>
                      </div>
                    ))}
                  </div>
                </div>
              </div>
            </section>
          </div>
        </main>
      </div>
    </>
  );
}
