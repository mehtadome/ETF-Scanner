import { ETFData } from "../api/fetchApi";

export function logFirst10ETFs(data: ETFData) {
  // Print the first 10 entries of response
  const first10Entries = Object.fromEntries(
    Object.entries(data as ETFData).slice(0, 10)
  ) as ETFData;

  console.log("Total ETFs:", Object.keys(data).length, "/ ETFs returned are:");
  Object.entries(first10Entries).forEach(([key, value], index) => {
    console.log(`${index + 1}. ${key}:`, value);
  });
}
