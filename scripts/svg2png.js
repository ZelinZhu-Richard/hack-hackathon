#!/usr/bin/env node
// Render an SVG to a 2x PNG (for Devpost, slides, README). Uses Playwright's Chromium.
// Usage: node svg2png.js architecture.svg [architecture.png]
const fs = require('fs');
const { chromium } = require('playwright');

(async () => {
  const [src, out = src.replace(/\.svg$/, '.png')] = process.argv.slice(2);
  const svg = fs.readFileSync(src, 'utf8');
  const w = +svg.match(/width="(\d+(?:\.\d+)?)"/)[1];
  const h = +svg.match(/height="(\d+(?:\.\d+)?)"/)[1];
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: Math.ceil(w), height: Math.ceil(h) }, deviceScaleFactor: 2 });
  await page.setContent(`<html><body style="margin:0;background:#070b19">${svg}</body></html>`);
  await page.waitForTimeout(400); // let the flow animation start so dashes are visible
  await page.locator('svg').screenshot({ path: out });
  await browser.close();
  console.log(`wrote ${out}`);
})();
