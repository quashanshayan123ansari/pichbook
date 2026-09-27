"use client";

import { useEffect, useRef, useState } from "react";
import { valuationRange, currentPrice } from "@/data/atlas";

const BAR_COLORS = [
  "linear-gradient(90deg, #1e4d8e, #2d6cc0)",
  "linear-gradient(90deg, #0f766e, #14b8a6)",
  "linear-gradient(90deg, #7c3aed, #a78bfa)",
];

export default function FootballField() {
  const [animated, setAnimated] = useState(false);
  const ref = useRef(null);

  useEffect(() => {
    const observer = new IntersectionObserver(
      ([entry]) => {
        if (entry.isIntersecting) {
          setAnimated(true);
          observer.disconnect();
        }
      },
      { threshold: 0.3 }
    );
    if (ref.current) observer.observe(ref.current);
    return () => observer.disconnect();
  }, []);

  // Calculate scale
  const allValues = valuationRange.flatMap((v) => [v.low, v.high]);
  allValues.push(currentPrice);
  const minVal = Math.min(...allValues) * 0.85;
  const maxVal = Math.max(...allValues) * 1.1;
  const range = maxVal - minVal;

  const pctOf = (v) => ((v - minVal) / range) * 100;
  const currentPct = pctOf(currentPrice);

  return (
    <div className="football-field" ref={ref}>
      {/* Scale labels */}
      <div style={{ display: "flex", justifyContent: "space-between", marginBottom: 8, padding: "0 156px 0 156px" }}>
        <span style={{ fontSize: 10, color: "#94a3b8", fontWeight: 600 }}>₹0</span>
        <span style={{ fontSize: 10, color: "#94a3b8", fontWeight: 600 }}>₹750</span>
        <span style={{ fontSize: 10, color: "#94a3b8", fontWeight: 600 }}>₹1,500</span>
      </div>

      {valuationRange.map((row, i) => {
        const leftPct = pctOf(row.low);
        const widthPct = pctOf(row.high) - leftPct;
        const midpoint = Math.round((row.low + row.high) / 2);

        return (
          <div className="ff-row" key={row.method}>
            <div className="ff-label">{row.method}</div>
            <div className="ff-bar-container">
              <div className="ff-track" />
              {/* Current price line */}
              <div
                className="ff-current-line"
                style={{ left: `${currentPct}%` }}
              >
                {i === 0 && (
                  <div className="ff-current-label">
                    Current ₹{currentPrice.toLocaleString()}
                  </div>
                )}
              </div>
              {/* Bar */}
              <div
                className="ff-bar"
                style={{
                  left: animated ? `${leftPct}%` : "50%",
                  width: animated ? `${widthPct}%` : "0%",
                  background: BAR_COLORS[i],
                  opacity: animated ? 1 : 0,
                  transition: `all 0.8s cubic-bezier(0.33, 1, 0.68, 1) ${i * 0.15}s`,
                }}
              >
                <span>₹{row.low}</span>
                <span style={{ fontSize: 9, opacity: 0.8 }}>Mid: ₹{midpoint}</span>
                <span>₹{row.high}</span>
              </div>
            </div>
            <div className="ff-values">
              ₹{row.low} – ₹{row.high}
            </div>
          </div>
        );
      })}

      <div style={{ marginTop: 16, textAlign: "center" }}>
        <span className="tag tag-red" style={{ fontSize: 11, padding: "4px 12px" }}>
          Current market price ₹{currentPrice.toLocaleString()} vs DCF base ₹310 → +339% premium
        </span>
      </div>
    </div>
  );
}
