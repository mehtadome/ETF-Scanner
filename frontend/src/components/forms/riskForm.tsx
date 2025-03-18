import { useNavigate } from "react-router-dom";
import "./IDForm.css";
import { useState } from "react";

/**
 * Ingests the entered riskLevel, expenseRatio, returnExpectation and loads two components showing some data about matching ETFs / MFs.
 * @param { riskLevel } Risk level wanted to take.
 * @param { expenseRatio } Willingness to pay for expenses.
 * @param { returnExpectation } Returns hoping for.
 * @param { onInputChange } Functionality for submiting form.
 * @returns <FC>
 */
const RiskForm = () => {
  const navigate = useNavigate();

  // Local state management
  const [formData, setFormData] = useState({
    assetType: "",
    riskLevel: "",
    expenseRatio: "",
    returnExpectation: "",
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    // Save to localStorage
    Object.entries(formData).forEach(([key, value]) => {
      localStorage.setItem(key, JSON.stringify(value)); // Parse with JSON.parse(localStorage.getItem('riskLevel') || 'null');
    });

    navigate(
      `/scanner/${formData.assetType}/riskLevel=${formData.riskLevel}&expenseRatio=${formData.expenseRatio}&returnExpectation=${formData.returnExpectation}`
    );
  };

  return (
    <>
      <form className="risk-form" onSubmit={handleSubmit}>
        {/* Select for ETF / Asset Type **/}
        <h3 className="risk-form-asset-title">ETFs or Mutual Funds?</h3>
        <select
          name="assetType"
          className="risk-select-input"
          value={formData.assetType}
          onChange={handleInputChange}
          required
        >
          <option value="" disabled>
            Select Asset Type
          </option>
          <option value="ETFs">ETFs</option>
          <option value="Mutual Funds">Mutual Funds</option>
        </select>

        {/* Select for Risk Level **/}
        <h3 className="risk-form-risk-level-title">Risk Level</h3>
        <select
          name="riskLevel"
          className="risk-select-input"
          value={formData.riskLevel}
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

        {/* Select for Expense Ratio **/}
        <h3 className="risk-form-expense-ratio-title">Expense Ratio</h3>
        <select
          name="expenseRatio"
          className="risk-select-input"
          value={formData.expenseRatio}
          onChange={handleInputChange}
          required
        >
          <option value="" disabled>
            Select Expense Ratio
          </option>
          <option value="Low">Low (0 - .25)</option>
          <option value="Medium">Medium (.25 - .50)</option>
          <option value="High">High (.50 - .75)</option>
          <option value="Very High">Very High (.75 - 1.00)</option>
          <option value="Expensive">Expensive (1.0+)</option>
        </select>

        {/* Select for Returns wanted **/}
        <h3 className="risk-form-return-expectation-title">Return Wanted</h3>
        <select
          name="returnExpectation"
          className="risk-select-input"
          value={formData.returnExpectation}
          onChange={handleInputChange}
          required
        >
          <option value="" disabled>
            Select Returns Wanted
          </option>
          <option value="Low">Low (0% - 5%)</option>
          <option value="Medium">Medium (5% - 10%)</option>
          <option value="High">High (10% - 15%)</option>
          <option value="Very High">Very High (15%+)</option>
        </select>

        {/* Button for Submission **/}
        <br />
        <br />
        <button
          className="risk-form-submit-button"
          type="submit"
          disabled={
            !Object.values(formData).every(
              (value) => value !== "Select Asset Type" || ""
            )
          }
        >
          Submit
        </button>
      </form>
    </>
  );
};

export default RiskForm;
