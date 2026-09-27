"use client";

import { Bar } from "react-chartjs-2";
import { tradingMultiples, financials } from "@/data/atlas";

const COLORS = {
  ATLAS: { bg: "rgba(212, 161, 42, 0.85)", border: "#d4a12a" },
  HUL: { bg: "rgba(30, 77, 142, 0.75)", border: "#1e4d8e" },
  Britannia: { bg: "rgba(45, 108, 192, 0.7)", border: "#2d6cc0" },
  Marico: { bg: "rgba(90, 154, 223, 0.65)", border: "#5a9adf" },
  Dabur: { bg: "rgba(16, 185, 129, 0.65)", border: "#10b981" },
  "Tata Consumer": { bg: "rgba(124, 58, 237, 0.65)", border: "#7c3aed" },
};

export function MultiplesBarChart({ metric = "evEbitda" }) {
  const labels = tradingMultiples.map((d) => d.company);
  const values = tradingMultiples.map((d) => d[metric]);
  const colors = labels.map((l) => COLORS[l]?.bg || "rgba(148, 163, 184, 0.5)");
  const borders = labels.map((l) => COLORS[l]?.border || "#94a3b8");

  const title =
    metric === "evEbitda" ? "EV / EBITDA" : metric === "pe" ? "P / E" : "EV / Revenue";

  const data = {
    labels,
    datasets: [
      {
        label: title,
        data: values,
        backgroundColor: colors,
        borderColor: borders,
        borderWidth: 1.5,
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 800, easing: "easeOutQuart" },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#0f2240",
        titleFont: { family: "Inter", weight: 600, size: 12 },
        bodyFont: { family: "Inter", size: 12 },
        padding: 12,
        cornerRadius: 8,
        callbacks: {
          label: (ctx) => `${title}: ${ctx.parsed.y.toFixed(1)}x`,
        },
      },
      datalabels: {
        anchor: "end",
        align: "top",
        formatter: (v) => `${v.toFixed(1)}x`,
        font: { family: "Inter", weight: 700, size: 11 },
        color: (ctx) => (ctx.dataIndex === 0 ? "#d4a12a" : "#0f2240"),
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: {
          font: { family: "Inter", weight: 600, size: 11 },
          color: "#475569",
        },
      },
      y: {
        grid: { color: "rgba(226, 232, 240, 0.5)", drawBorder: false },
        ticks: {
          font: { family: "Inter", size: 11 },
          color: "#94a3b8",
          callback: (v) => `${v}x`,
        },
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function MarginChart() {
  const labels = tradingMultiples.map((d) => d.company);
  const ebitdaMargins = tradingMultiples.map((d) => (d.ebitdaMargin * 100).toFixed(1));
  const patMargins = tradingMultiples.map((d) => (d.patMargin * 100).toFixed(1));

  const data = {
    labels,
    datasets: [
      {
        label: "EBITDA Margin",
        data: ebitdaMargins,
        backgroundColor: labels.map((l, i) =>
          i === 0 ? "rgba(212, 161, 42, 0.8)" : "rgba(30, 77, 142, 0.6)"
        ),
        borderRadius: 6,
        borderSkipped: false,
      },
      {
        label: "PAT Margin",
        data: patMargins,
        backgroundColor: labels.map((l, i) =>
          i === 0 ? "rgba(212, 161, 42, 0.45)" : "rgba(30, 77, 142, 0.3)"
        ),
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 800, easing: "easeOutQuart" },
    plugins: {
      legend: {
        position: "top",
        labels: {
          font: { family: "Inter", weight: 600, size: 11 },
          usePointStyle: true,
          pointStyle: "rectRounded",
          padding: 16,
        },
      },
      tooltip: {
        backgroundColor: "#0f2240",
        padding: 12,
        cornerRadius: 8,
        callbacks: { label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}%` },
      },
      datalabels: {
        anchor: "end",
        align: "top",
        formatter: (v) => `${v}%`,
        font: { family: "Inter", weight: 600, size: 10 },
        color: "#475569",
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 11 }, color: "#475569" },
      },
      y: {
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        ticks: {
          font: { family: "Inter", size: 11 },
          color: "#94a3b8",
          callback: (v) => `${v}%`,
        },
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function RevenueChart() {
  const data = {
    labels: ["CY2022", "FY2025", "FY2026"],
    datasets: [
      {
        label: "Revenue (₹ Cr)",
        data: [16897, 20260, 23155],
        backgroundColor: [
          "rgba(30, 77, 142, 0.5)",
          "rgba(30, 77, 142, 0.7)",
          "rgba(212, 161, 42, 0.85)",
        ],
        borderColor: ["#1e4d8e", "#1e4d8e", "#d4a12a"],
        borderWidth: 1.5,
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 1000, easing: "easeOutQuart" },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#0f2240",
        padding: 12,
        cornerRadius: 8,
        callbacks: { label: (ctx) => `Revenue: ₹${ctx.parsed.y.toLocaleString()} Cr` },
      },
      datalabels: {
        anchor: "end",
        align: "top",
        formatter: (v) => `₹${v.toLocaleString()}`,
        font: { family: "Inter", weight: 700, size: 12 },
        color: "#0f2240",
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 12 }, color: "#475569" },
      },
      y: {
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        ticks: {
          font: { family: "Inter", size: 11 },
          color: "#94a3b8",
          callback: (v) => `₹${(v / 1000).toFixed(0)}K`,
        },
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function PeerRevenueChart() {
  const peers = ["HUL", "Britannia", "Marico", "Dabur", "Tata Consumer"];
  const revFy23 = [59549, 15618, 9764, 11530, 13783];
  const revFy25 = [60573, 17296, 10831, 12563, 17618];

  const data = {
    labels: peers,
    datasets: [
      {
        label: "FY2023",
        data: revFy23,
        backgroundColor: "rgba(30, 77, 142, 0.4)",
        borderRadius: 4,
        borderSkipped: false,
      },
      {
        label: "FY2025",
        data: revFy25,
        backgroundColor: "rgba(30, 77, 142, 0.75)",
        borderRadius: 4,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 800 },
    plugins: {
      legend: {
        position: "top",
        labels: { font: { family: "Inter", weight: 600, size: 11 }, usePointStyle: true, padding: 16 },
      },
      tooltip: { backgroundColor: "#0f2240", padding: 12, cornerRadius: 8 },
      datalabels: { display: false },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 10 }, color: "#475569" },
      },
      y: {
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        ticks: {
          font: { family: "Inter", size: 10 },
          color: "#94a3b8",
          callback: (v) => `₹${(v / 1000).toFixed(0)}K`,
        },
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function EVWaterfallChart() {
  const labels = ["Market Cap", "Total Debt", "(-) Cash", "= Ent. Value"];
  const values = [262752, 753, -76, 263429];

  // Waterfall: use floating bars
  const bottoms = [0, 262752, 262752 + 753, 0];
  const tops = [262752, 262752 + 753, 262752 + 753 - 76, 263429];

  const data = {
    labels,
    datasets: [
      {
        label: "EV Bridge",
        data: tops.map((t, i) => [bottoms[i], t]),
        backgroundColor: [
          "rgba(30, 77, 142, 0.75)",
          "rgba(239, 68, 68, 0.6)",
          "rgba(16, 185, 129, 0.6)",
          "rgba(212, 161, 42, 0.85)",
        ],
        borderColor: ["#1e4d8e", "#ef4444", "#10b981", "#d4a12a"],
        borderWidth: 1.5,
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 1000, easing: "easeOutQuart" },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#0f2240",
        padding: 12,
        cornerRadius: 8,
        callbacks: {
          label: (ctx) => {
            const val = values[ctx.dataIndex];
            return `₹${Math.abs(val).toLocaleString()} Cr`;
          },
        },
      },
      datalabels: {
        anchor: "end",
        align: "top",
        formatter: (v, ctx) => {
          const val = values[ctx.dataIndex];
          return `₹${Math.abs(val).toLocaleString()}`;
        },
        font: { family: "Inter", weight: 700, size: 11 },
        color: "#0f2240",
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 11 }, color: "#475569" },
      },
      y: {
        display: false,
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function GrowthCAGRChart() {
  const peers = ["HUL", "Britannia", "Marico", "Dabur", "T. Consumer"];
  const revCagr = [0.9, 5.2, 5.3, 4.4, 13.1];
  const ebitdaCagr = [0.1, 4.4, 8.6, 3.5, 15.6];

  const data = {
    labels: peers,
    datasets: [
      {
        label: "Rev CAGR (2yr)",
        data: revCagr,
        backgroundColor: "rgba(30, 77, 142, 0.7)",
        borderRadius: 4,
        borderSkipped: false,
      },
      {
        label: "EBITDA CAGR (2yr)",
        data: ebitdaCagr,
        backgroundColor: "rgba(212, 161, 42, 0.7)",
        borderRadius: 4,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 800 },
    plugins: {
      legend: {
        position: "top",
        labels: { font: { family: "Inter", weight: 600, size: 11 }, usePointStyle: true, padding: 16 },
      },
      tooltip: {
        backgroundColor: "#0f2240",
        padding: 12,
        cornerRadius: 8,
        callbacks: { label: (ctx) => `${ctx.dataset.label}: ${ctx.parsed.y}%` },
      },
      datalabels: {
        anchor: "end",
        align: "top",
        formatter: (v) => `${v}%`,
        font: { family: "Inter", weight: 600, size: 10 },
        color: "#475569",
      },
    },
    scales: {
      x: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 11 }, color: "#475569" },
      },
      y: {
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        ticks: {
          font: { family: "Inter", size: 10 },
          color: "#94a3b8",
          callback: (v) => `${v}%`,
        },
        beginAtZero: true,
      },
    },
  };

  return (
    <div className="chart-container">
      <Bar data={data} options={options} />
    </div>
  );
}

export function DCFCompositionChart() {
  const data = {
    labels: ["PV of FCFFs", "PV of Terminal Value"],
    datasets: [
      {
        label: "DCF Composition",
        data: [24254, 36208],
        backgroundColor: ["rgba(30, 77, 142, 0.75)", "rgba(212, 161, 42, 0.75)"],
        borderColor: ["#1e4d8e", "#d4a12a"],
        borderWidth: 1.5,
        borderRadius: 6,
        borderSkipped: false,
      },
    ],
  };

  const options = {
    indexAxis: "y",
    responsive: true,
    maintainAspectRatio: false,
    animation: { duration: 1000, easing: "easeOutQuart" },
    plugins: {
      legend: { display: false },
      tooltip: {
        backgroundColor: "#0f2240",
        padding: 12,
        cornerRadius: 8,
        callbacks: { label: (ctx) => `₹${ctx.parsed.x.toLocaleString()} Cr` },
      },
      datalabels: {
        anchor: "end",
        align: "right",
        formatter: (v) => `₹${v.toLocaleString()} Cr`,
        font: { family: "Inter", weight: 700, size: 12 },
        color: "#0f2240",
      },
    },
    scales: {
      x: {
        grid: { color: "rgba(226, 232, 240, 0.5)" },
        ticks: {
          font: { family: "Inter", size: 10 },
          color: "#94a3b8",
          callback: (v) => `₹${(v / 1000).toFixed(0)}K`,
        },
      },
      y: {
        grid: { display: false },
        ticks: { font: { family: "Inter", weight: 600, size: 12 }, color: "#475569" },
      },
    },
  };

  return (
    <div className="chart-container" style={{ height: 180 }}>
      <Bar data={data} options={options} />
    </div>
  );
}
