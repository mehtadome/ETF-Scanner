import { useEffect, useState } from "react";
import { fetchTop20_1YrReturn, ETFs } from "../../api/fetchApi";
import "./last20likesDisplay.css";
import { FavoritesProps } from "../../pages/Favorites";

/**
 * Display user's last 20 recently liked songs.
 * @param { username } <string>
 * @returns { component } <FC>
 */
export const Last20Likes: React.FC<FavoritesProps> = ({ username }) => {
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
        const response = await fetchTop20_1YrReturn();

        if (response.data) {
          console.log(response.data);
          setETFs(response.data);
        }
      } catch (err) {
        setError(err instanceof Error ? err.message : "An error occurred");
      } finally {
        setLoading(false);
      }
    };

    lastLikes();
  }, [username]);

  if (loading) return <div className="loading-buffer">Loading...</div>;
  if (error) return <div className="error-box">Error: {error}</div>;

  return (
    <div className="songs-container">
      <h3>Top 20 ETFs for 1 yr return</h3>
      <div className="songs-grid">
        {Object.entries(ETFs).map(([id, name]) => (
          <div key={id} className="songs-card">
            <h5>{name}</h5>
          </div>
        ))}
      </div>
    </div>
  );
};
