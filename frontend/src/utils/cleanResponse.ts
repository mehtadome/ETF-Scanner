import { ETFs } from "../api/fetchApi";
/**
 * {
 * 'FIRST TRUST SKYBRIDGE CRYPTO INDUSTRY & DIGITAL ECONOMY ETF (CRPT)': 147.36,
 * 'SIMPLIFY VOLT TSLA REVOLUTION ETF (TESL)': 145.48, 'INVESCO GALAXY BITCOIN ETF (BTCO)': 138.64,
 * 'FRANKLIN BITCOIN ETF (EZBC)': 138.57, 'WISDOMTREE BITCOIN FUND (BTCW)': 138.42,
 * 'VANECK BITCOIN ETF (HODL)': 138.36, 'COINSHARES VALKYRIE BITCOIN FUND (BRRR)': 138.31,
 * 'ARK 21SHARES BITCOIN ETF BEN OF INT (ARKB)': 138.14, 'FIDELITY WISE ORIGIN BITCOIN FUND (FBTC)': 138.02,
 * 'BITWISE BITCOIN ETF TRUST (BITB)': 137.98
 * }
 */

export function stripAcronym(response: ETFs): ETFs {
  const parsedResponse: ETFs = {};
  // Loop through response JSON and keep only the acronym
  for (const [key, value] of Object.entries(response)) {
    // Extract text between parentheses using regex
    const match = key.match(/\(([^)]+)\)/);
    if (match) {
      // match[1] contains the text between parentheses
      parsedResponse[match[1]] = value;
    }
  }
  return parsedResponse;
}
