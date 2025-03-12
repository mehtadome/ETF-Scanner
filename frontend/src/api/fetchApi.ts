import { FetchApiResponse } from "./apiUtils";

// INFO: BASE_URL= http://localhost:5000/api

// TYPES
export interface MutualFunds {
  [key: string]: string;
}
// differentiating for readability
export interface ETFs {
  [key: string]: string;
}

// TODO: Split up API functions by ETF / Mutual Fund

// API Functions
/**
 * GET: Grab top 10 ETFs based on risk portolio (currently hard-coded to 1 yr return).
 * PATH: http://localhost:5000/api/favorites/<username>
 * @param { riskPortolio } <string> (currently unimplemented and hard-coded to 1 yr return outside of function).
 * @returns { ETFs } <JSON>
*  Example Response:
    {
        'FIRST TRUST SKYBRIDGE CRYPTO INDUSTRY & DIGITAL ECONOMY ETF (CRPT)': 147.36, 
        'SIMPLIFY VOLT TSLA REVOLUTION ETF (TESL)': 145.48
    }
 */
export async function fetchTop10_1YrETFsReturn<ETFs>(): Promise<
  FetchApiResponse<ETFs>
> {
  const response = await fetch(`/api/etfs/1year`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    credentials: "same-origin",
  });

  if (!response.ok) {
    console.log("Top 20 ETF choices for 1 year return: ", response);
    throw new Error(
      `Top 20 ETFs for 1 year | HTTP error! status: ${response.status}`
    );
  }

  const data = await response.json();
  return {
    data,
    status: response.status,
  };
}

/**
 * GET: Grab Top 10 Mutual Funds (currently hard-coded for 10 Yr Return).
 * PATH: http://localhost:5000/api/favorites/playlists/<username>
 * @param { riskPortfolio } <string> (currently unimplemented and hard-coded to 10 yr return outside of function)
 * @returns { MutualFunds } <JSON>
 *    
 * Example Response:
    {
        
    }
 */
export async function fetchTop10_10YrMFsReturn<MutualFunds>(): Promise<
  FetchApiResponse<MutualFunds>
> {
  const response = await fetch(`/api/mutualfunds/10year`, {
    method: "GET",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
    },
    credentials: "same-origin",
  });

  if (!response.ok) {
    console.log("Top 20 Mutual Funds for 10 years: ", response);
    throw new Error(
      `Top 20 Mutual Funds for 10 years | HTTP error! status: ${response.status}`
    );
  }

  const data = await response.json();
  return {
    data,
    status: response.status,
  };
}

/** Another way to fetch
 * *
 * return fetch(`${BASE_URL}/favorites/${username}`)
  .then((response) => response.json())
  .then((data) => {
    return {
      data,
      status: response.status,
    };
  })
  .catch(handleError);} // dev-defined function handleError()
 * 
 */
