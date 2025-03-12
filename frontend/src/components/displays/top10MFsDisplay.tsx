import { useEffect, useState } from "react";
import { fetchTop10_10YrMFsReturn, MutualFunds } from "../../api/fetchApi";
import "./top10ETFsDisplay.css";
import { ScannerProps } from "../../pages/Main";
import { stripMutualFundsAcronym } from "../../utils/cleanResponse";

/**
 * Display user's created playlists.
 * @param { username } <string>
 * @returns { component } <FC>
 */
export const Top10MutualFunds: React.FC<ScannerProps> = ({ returnParam }) => {
  returnParam = "10 Yr Return";
  /**
   * Uncomment and use the following line if the below error breaks your code:
   *  Argument of type '{}' is not assignable to parameter of type 'SetStateAction<Playlists>'.ts(2345)
   *
   * // const [playlists, setPlaylists] = useState<unknown>({});
   *
   * Description: TypeScript will not be able to determine what "type" of data will be passed back down from your backend.
   *  * We assign it an empty dict knowing that is its base state.
   */
  // const [playlists, setPlaylists] = useState<Playlists>({});
  const [funds, setFunds] = useState<MutualFunds>({});

  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchPlaylists = async () => {
      try {
        const response = await fetchTop10_10YrMFsReturn();

        if (response.data) {
          console.log(response.data);
          const responseCleaned = stripMutualFundsAcronym(response.data);
          setFunds(responseCleaned);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    fetchPlaylists();
  }, [returnParam]);

  const handleCardClick = (fundName: string) => {
    const searchQuery = encodeURIComponent(fundName);
    window.open(`https://www.google.com/search?q=${searchQuery}`, "_blank");
  };

  if (loading) return <div className="loading-buffer">Loading...</div>;
  if (error) return <div className="error-box">Error: {error}</div>;

  if (Object.keys(funds).length === 0) {
    return <div className="empty-state">No mutual funds found</div>;
  }

  return (
    <div className="songs-container">
      <h3>Top 10 Mutual Funds for 10 yr return</h3>
      <div className="songs-grid">
        {Object.entries(funds).map(([name, value]) => (
          <div
            key={name}
            className="songs-card"
            onClick={() => handleCardClick(name)}
          >
            <h5>
              {name}: {value}%
            </h5>
          </div>
        ))}
      </div>
    </div>
  );
};
