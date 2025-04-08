interface AssetTypeProps {
  assetType: string;
  handleInputChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

/**
 *
 * @param { assetType } string; Passed down to maintain disabled info selection.
 *        |-- Holds values "ETFs" or "Mutual Funds".
 * @param { handleInputChange } function; Maintains state of form data.
 * @returns <FC>;
 */
const AssetTypeSelect = ({ assetType, handleInputChange }: AssetTypeProps) => {
  return (
    <>
      <h3 className="risk-form-asset-title">ETFs or Mutual Funds?</h3>
      <select
        name="assetType"
        className="risk-select-input"
        value={assetType}
        onChange={handleInputChange}
        required
      >
        <option value="" disabled>
          Select Asset Type
        </option>
        <option value="ETFs">ETFs</option>
        <option value="Mutual Funds">Mutual Funds</option>
      </select>
    </>
  );
};

export default AssetTypeSelect;
