"use client";

import React from "react";
import { dcfSensitivity } from "@/data/atlas";

export default function SensitivityGrid() {
  const { waccs, tgrs, grid, baseCase } = dcfSensitivity;

  return (
    <div className="sensitivity-grid">
      {/* Header row */}
      <div className="sens-header">WACC \ TGR</div>
      {tgrs.map((t) => (
        <div className="sens-header" key={t}>
          TGR = {(t * 100).toFixed(1)}%
        </div>
      ))}

      {/* Data rows */}
      {waccs.map((w) => (
        <React.Fragment key={w}>
          <div className="sens-row-label">
            WACC = {(w * 100).toFixed(0)}%
          </div>
          {tgrs.map((t) => {
            const key = `${(w * 100).toFixed(0)}-${(t * 100).toFixed(1)}`;
            const val = grid[key];
            const isBase = w === baseCase.wacc && t === baseCase.tgr;
            return (
              <div
                className={`sens-cell ${isBase ? "base" : ""}`}
                key={`${w}-${t}`}
              >
                ₹{val}
                {isBase && (
                  <div
                    style={{
                      fontSize: 9,
                      fontWeight: 600,
                      color: "#d4a12a",
                      marginTop: 2,
                    }}
                  >
                    BASE CASE
                  </div>
                )}
              </div>
            );
          })}
        </React.Fragment>
      ))}
    </div>
  );
}
