import { useEffect, useState } from "react";
import { fetchTop10_1YrETFsReturn, ETFs } from "../../api/fetchApi";
import "./top10ETFsDisplay.css";
import { stripETFsAcronym } from "../../utils/cleanResponse";
/**
 * Display 20 ETFs based on return wanted (Currently hard-coded to 1 year).
 * @param { returnParam } <string> (Currently hard-coded to 1 year in Main.tsx)
 * @returns { component } <FC>
 */
export const Top10ETFs = () => {
  /**
   * Uncomment and use the following line if the below error breaks your code:
   *  Argument of type '{}' is not assignable to parameter of type 'SetStateAction<Playlists>'.ts(2345)
   *
   * // const [songs, setSongs] = useState<unknown>({});
   *
   * Description: TypeScript will not be able to determine what "type" of data will be passed back down from your backend.
   *  * We assign it an empty dict knowing that is its base state.
   */
  const [ETFs, setETFs] = useState<ETFs>({});

  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    /** Similar syntax
     * fetch(`/api/${username}/library/top20`)
      .then((response) => response.json())
      .then((data) => {
        setSongs(data);
        setLoading(false);
      })
      .catch((error) => {
        setError(error);
        console.log("Error fetching test from API: ", error);
      });
     */

    const lastLikes = async () => {
      try {
        const response = await fetchTop10_1YrETFsReturn();

        if (response.data) {
          console.log(response.data);
          const responseCleaned = stripETFsAcronym(response.data);
          setETFs(responseCleaned);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    lastLikes();
  }, []);

  const handleCardClick = (etfName: string) => {
    const searchQuery = encodeURIComponent(etfName);
    window.open(`https://www.google.com/search?q=${searchQuery}`, "_blank");
  };

  if (loading) return <div className="loading-buffer">Loading...</div>;
  if (error) return <div className="error-box">Error: {error}</div>;

  return (
    <div className="songs-container">
      <h3>Top 10 ETFs for 1 yr return</h3>
      <div className="songs-grid">
        {Object.entries(ETFs).map(([name, value]) => (
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
