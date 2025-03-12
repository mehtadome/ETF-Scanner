import { Top10ETFs } from "../components/displays/top10ETFsDisplay";
import { Top10MutualFunds } from "../components/displays/top10MFsDisplay";
import "./Main.css";
import { ConnTest } from "../components/displays/connectionDisplay";

export interface ScannerProps {
  username: string;
  returnParam?: string;
}

const returnParam = "1 Yr Return";

/**
 * Displays two FCs by passing down username as a property.
 * @param { username } Spotify username.
 * @returns <FC>
 */
const Favorites: React.FC<ScannerProps> = ({ username }) => {
  return (
    <>
      <div className="library-insights">
        <h1>ETF Scanner Insights</h1>
        <Top10ETFs username={returnParam} />
        <Top10MutualFunds username={returnParam} />
        <ConnTest username={username} />
      </div>
    </>
  );
};

export default Favorites;
