import { Top10ETFs } from "../components/displays/top10ETFsDisplay";
import "./HomePage.css";
import { ConnTest } from "../components/displays/connectionDisplay";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";
import { ErrorDisplayProps } from "../components/displays/ErrorDisplay";
import ErrorDisplay from "../components/displays/ErrorDisplay";

/**
 * Display the insights page.
 * @returns { component } <FC>
 */
const InsightsPage = () => {
  //const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const [error, setError] = useState<ErrorDisplayProps | null>(null);

  /**
   * This effect is used to check if the required query parameters are present in the URL.
   * If any of the required parameters are missing, it sets an error state.
   * @param { searchParams } The query parameters from the URL
   */
  useEffect(() => {
    try {
      // Access query parameters
      const requiredParams = {
        riskLevel: searchParams.get("riskLevel"),
        expenseRatio: searchParams.get("expenseRatio"),
        returnRatio: searchParams.get("returnRatio"),
      };

      const missingParams = Object.entries(requiredParams)
        .filter(([_, value]) => value === null)
        .map(([key]) => key);

      if (missingParams.length > 0) {
        throw new Error(
          `Missing required parameters: ${missingParams.join(", ")}`
        );
      }
      setError(null);
    } catch (err) {
      setError(err instanceof Error ? err : new Error("An error occurred"));
    }
  }, [searchParams]);

  if (error) {
    return <ErrorDisplay message={error.message} />;
  }

  const riskLevel = searchParams.get("riskLevel")!;
  const expenseRatio = searchParams.get("expenseRatio")!;
  const returnRatio = searchParams.get("returnRatio")!;

  return (
    <>
      <div>
        <h2>ETFs Results</h2>
        <p>Risk Level: {riskLevel}</p>
        <p>Expense Ratio: {expenseRatio}</p>
        <p>Return Ratio: {returnRatio}</p>
        {/* Rest of your component */}
      </div>
      <Top10ETFs
        riskLevel={riskLevel}
        expenseRatio={expenseRatio}
        returnRatio={returnRatio}
      />

      <ConnTest />
    </>
  );
};

export default InsightsPage;

/** DESIGN NOTE
 * Search parameters are more appropriate than using local storage because:
 *    1. Users can share their ETF search results
 *    2. Results are bookmarkable
 *    3. Browser history navigation works naturally
 *    4. It's more RESTful
 */
