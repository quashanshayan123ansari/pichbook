"use client";

import { useState, useEffect } from "react";

const sections = [
  { id: "overview", label: "Overview", icon: "◈", num: "0" },
  { id: "checks", label: "Verification Checks", icon: "✓", num: "1" },
  { id: "capitalisation", label: "Capitalisation", icon: "◆", num: "2" },
  { id: "multiples", label: "Trading Multiples", icon: "⬡", num: "3" },
  { id: "income", label: "Income Statement", icon: "▤", num: "4" },
  { id: "balance", label: "Balance Sheet", icon: "▥", num: "5" },
  { id: "growth", label: "Growth Rates", icon: "△", num: "6" },
  { id: "dcf", label: "DCF Analysis", icon: "◎", num: "7" },
  { id: "valuation", label: "Valuation Summary", icon: "★", num: "8" },
];

export default function Sidebar() {
  const [active, setActive] = useState("overview");

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        const visible = entries
          .filter((e) => e.isIntersecting)
          .sort((a, b) => a.boundingClientRect.top - b.boundingClientRect.top);
        if (visible.length > 0) {
          setActive(visible[0].target.id);
        }
      },
      { rootMargin: "-80px 0px -60% 0px", threshold: 0.1 }
    );

    sections.forEach((s) => {
      const el = document.getElementById(s.id);
      if (el) observer.observe(el);
    });

    return () => observer.disconnect();
  }, []);

  const scrollTo = (id) => {
    const el = document.getElementById(id);
    if (el) {
      el.scrollIntoView({ behavior: "smooth", block: "start" });
      setActive(id);
    }
  };

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <h1>A T L A S</h1>
        <p>Nestlé India Limited • Board Deck</p>
      </div>

      <nav className="sidebar-nav">
        {sections.map((s) => (
          <button
            key={s.id}
            className={`nav-item ${active === s.id ? "active" : ""}`}
            onClick={() => scrollTo(s.id)}
            style={{ background: "none", border: "none", width: "100%", textAlign: "left" }}
          >
            <span className="nav-icon">{s.icon}</span>
            <span>{s.label}</span>
            <span className="nav-number">{s.num}</span>
          </button>
        ))}
      </nav>

      <div className="sidebar-footer">
        <p>
          For Illustrative Purposes Only
          <br />
          Market Data: 25 September 2026
          <br />
          All figures INR Crore unless stated
        </p>
      </div>
    </aside>
  );
}
