import { useEffect, useState } from "react";
import { fetchTop10_1YrETFsReturn, ETFs } from "../../api/fetchApi";
import "./top10ETFsDisplay.css";
import { stripETFsAcronym } from "../../utils/cleanResponse";

export interface Top10ETFsProps {
  riskLevel: string;
  expenseRatio: string;
  returnRatio: string;
}

/**
 * Display 20 ETFs based on return wanted (Currently hard-coded to 1 year).
 * @param { riskLevel } Risk level wanted to take.
 * @param { expenseRatio } Willingness to pay for expenses.
 * @param { returnRatio } Returns hoping for.
 * @returns { component } <FC>
 */
export const Top10ETFs = ({
  riskLevel,
  expenseRatio,
  returnRatio,
}: Top10ETFsProps) => {
  const [ETFs, setETFs] = useState<ETFs>({});

  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const lastLikes = async () => {
      try {
        const response = await fetchTop10_1YrETFsReturn({
          riskLevel,
          expenseRatio,
          returnRatio,
        });

        if (response.data) {
          const responseCleaned = stripETFsAcronym(response.data);
          console.log("Cleaned response is", responseCleaned);
          setETFs(responseCleaned);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    lastLikes();
  }, [riskLevel, expenseRatio, returnRatio]);

  const handleCardClick = (etfName: string) => {
    const searchQuery = encodeURIComponent(etfName);
    window.open(`https://www.google.com/search?q=${searchQuery}`, "_blank");
  };

  if (loading) return <div className="loading-buffer">Loading...</div>;
  if (error) return <div className="error-box">Error: {error}</div>;

  return (
    <div className="songs-container">
      <h2>Results</h2>
      <div className="songs-grid">
        {Object.entries(ETFs).map(([name, value]) => (
          <div
            key={name}
            className="songs-card"
            onClick={() => handleCardClick(name)}
          >
            <h5>
              <h3>{name}</h3>
              Return: {value.return}% <br />
              Risk: {value.alpha}%<br />
              Expense: {value.expense}% <br />
            </h5>
          </div>
        ))}
      </div>
    </div>
  );
};
