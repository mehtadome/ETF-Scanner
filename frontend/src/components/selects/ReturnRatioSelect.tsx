interface ReturnRatioProps {
  returnRatio: string;
  handleInputChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

/**
 *
 * @param { returnRatio } string; Passed down to maintain disabled info selection.
 *        |-- Holds values "Low", "Medium", "High", "Very High".
 * @param { handleInputChange } function; Maintains state of form data.
 * @returns <FC>
 */
const ReturnRatioSelect = ({
  returnRatio,
  handleInputChange,
}: ReturnRatioProps) => {
  return (
    <>
      <h3 className="risk-form-return-ratio-title">Return Wanted</h3>
      <select
        name="returnRatio"
        className="risk-select-input"
        value={returnRatio}
        onChange={handleInputChange}
        required
      >
        <option value="" disabled>
          Select Returns Wanted
        </option>
        <option value="Low">Low (0% - 5%)</option>
        <option value="Medium">Medium (5% - 10%)</option>
        <option value="High">High (10% - 15%)</option>
        <option value="Very High">Very High (15% +)</option>
      </select>
    </>
  );
};

export default ReturnRatioSelect;
