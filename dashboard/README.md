# ATLAS Pitchbook Dashboard (Next.js & React)

[![Next.js](https://img.shields.io/badge/Next.js-16.3-black?style=for-the-badge&logo=next.js&logoColor=white)](https://nextjs.org/)
[![React](https://img.shields.io/badge/React-19.2-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://react.dev/)
[![Chart.js](https://img.shields.io/badge/Chart.js-4.5-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white)](https://www.chartjs.org/)

An interactive, institutional-grade board deck and financial dashboard for **Nestlé India Limited** (*Project Code: ATLAS*). Built with **Next.js 16 (Turbopack)**, **React 19**, and **Chart.js**, designed to deliver real-time visual analysis of trading multiples, financial statements, DCF sensitivity, and peer benchmarking.

---

## Key Features

- **Interactive Valuation Football Field:** Real-time visual comparison of Trading Comps (EV/EBITDA, P/E) vs. 10-Year DCF vs. Current Market Price (₹1,362.60).
- **Two-Way DCF Sensitivity Matrix:** Dynamic grid computing per-share intrinsic value across WACC (11.0% – 13.0%) and Terminal Growth Rates (5.0% – 6.0%).
- **Multiples & Margins Benchmarking:** Interactive Chart.js visualizations for peer EV/EBITDA, P/E, EBITDA margins, PAT margins, and revenue growth CAGRs against HUL, Britannia, Marico, Dabur, and TCPL.
- **Audited Financial Statements:** Historical and LTM financials for CY2022, FY2025, and FY2026, including gross margin progression, EBITDA bridges, and balance sheet capital structure.
- **Enterprise Value Waterfall:** Complete bridge visualization from Market Capitalisation through Net Debt, Lease Liabilities, and Cash to Enterprise Value.
- **Dark Institutional Design:** Custom Bloomberg / investment-banking styled design system with responsive layouts and typography.

---

## Directory & Component Structure

```
dashboard/
├── app/
│   ├── layout.js          # HTML metadata, font configurations, and root layout
│   ├── page.js            # Main dashboard container with tabbed sections & views
│   ├── globals.css        # Financial design tokens, CSS variables, and dark theme
│   └── page.module.css    # Scoped styles for layout-specific elements
├── components/
│   ├── ChartSetup.js      # Global Chart.js registry, defaults, and tooltip formatting
│   ├── Charts.js          # Chart.js component wrappers (Multiples, Margins, Waterfalls)
│   ├── FootballField.js   # Custom SVG/HTML Valuation Football Field component
│   ├── SensitivityGrid.js # Interactive DCF Sensitivity matrix with base-case highlighting
│   └── Sidebar.js         # Navigation sidebar with anchor links & active status
├── data/
│   └── atlas.js           # Single Source of Truth (SSOT) data layer matching atlas_compute.py
├── package.json           # Next.js, React, and Chart.js dependencies
└── README.md              # Frontend documentation (this file)
```

---

## Getting Started

### 1. Install Dependencies
```bash
npm install
```

### 2. Run the Development Server
```bash
npm run dev
```
Open **[http://localhost:3000](http://localhost:3000)** in your browser. The app hot-reloads automatically on file changes.

### 3. Build for Production
```bash
npm run build
npm start
```

### 4. Linting
```bash
npm run lint
```

---

## Data Synchronization

The dashboard's data layer in [`data/atlas.js`](data/atlas.js) is mathematically reconciled with the quantitative engine in [`../atlas_compute.py`](../atlas_compute.py). Any revisions to base financials or peer multiples should be verified in `atlas_compute.py` first before updating `data/atlas.js`.
