interface RiskLevelProps {
  riskLevel: string;
  handleInputChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

/**
 *
 * @param { riskLevel } string; Passed down to maintain disabled info selection.
 *        |-- Holds values "Low", "Medium", "High", "Very High".
 * @param { handleInputChange } function; Maintains state of form data.
 * @returns <FC>
 */
const RiskLevelSelect = ({ riskLevel, handleInputChange }: RiskLevelProps) => {
  return (
    <>
      <h3 className="risk-form-risk-level-title">Risk Level</h3>
      <select
        name="riskLevel"
        className="risk-select-input"
        value={riskLevel}
        onChange={handleInputChange}
        required
      >
        <option value="" disabled>
          Select Risk Level
        </option>
        <option value="Low">Low (0 - 25)</option>
        <option value="Medium">Medium (25 - 50)</option>
        <option value="High">High (50 - 75)</option>
        <option value="Very High">Very High (75 - 100)</option>
      </select>
    </>
  );
};

export default RiskLevelSelect;
