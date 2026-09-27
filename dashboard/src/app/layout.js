import "./globals.css";

export const metadata = {
  title: "ATLAS — Nestlé India Investment Banking Board Deck",
  description:
    "Comprehensive financial analysis dashboard for Nestlé India (ATLAS) including trading multiples, DCF valuation, peer benchmarking, and capitalisation data. Market data as of 25 September 2026.",
  keywords: [
    "Nestlé India",
    "ATLAS",
    "NESTLEIND",
    "investment banking",
    "pitchbook",
    "board deck",
    "DCF",
    "valuation",
    "FMCG",
  ],
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link
          rel="preconnect"
          href="https://fonts.gstatic.com"
          crossOrigin="anonymous"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=JetBrains+Mono:wght@400;500;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body>{children}</body>
    </html>
  );
}
