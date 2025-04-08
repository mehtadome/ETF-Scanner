import { Top10ETFs } from "../components/displays/top10ETFsDisplay";
import "./HomePage.css";
import { ConnTest } from "../components/displays/connectionDisplay";
import { useEffect, useState } from "react";
import { useSearchParams } from "react-router-dom";

// Consider renaming to InsightsPage

/**
 *
 */
const InsightsPage = () => {
  //const navigate = useNavigate();
  const [searchParams] = useSearchParams();

  // Access query parameters
  const riskLevel = searchParams.get("riskLevel");
  const expenseRatio = searchParams.get("expenseRatio");
  const returnRatio = searchParams.get("returnRatio");

  useEffect(() => {
    // Use the parameters as needed
    console.log({
      riskLevel,
      expenseRatio,
      returnRatio,
    });
  }, [riskLevel, expenseRatio, returnRatio]);

  return (
    <>
      <div>
        <h2>ETFs Results</h2>
        <p>Risk Level: {riskLevel}</p>
        <p>Expense Ratio: {expenseRatio}</p>
        <p>Return Ratio: {returnRatio}</p>
        {/* Rest of your component */}
      </div>
      <Top10ETFs />

      <ConnTest />
    </>
  );
};

export default InsightsPage;
