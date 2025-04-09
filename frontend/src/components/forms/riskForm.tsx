import { useNavigate } from "react-router-dom";
import "./RiskForm.css";
import AssetTypeSelect from "../selects/AssetTypeSelect.tsx";
import RiskLevelSelect from "../selects/RiskLevelSelect";
import ExpenseRatioSelect from "../selects/ExpenseRatioSelect";
import ReturnRatioSelect from "../selects/ReturnRatioSelect";

export interface RiskFormProps {
  formData: {
    assetType: string;
    riskLevel: string;
    expenseRatio: string;
    returnRatio: string;
  };
  handleInputChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

/**
 * Ingests the entered riskLevel, expenseRatio, returnRatio and loads two components showing some data about matching ETFs / MFs.
 * @param { riskLevel } Risk level wanted to take.
 * @param { expenseRatio } Willingness to pay for expenses.
 * @param { returnRatio } Returns hoping for.
 * @param { onInputChange } Functionality for submiting form.
 * @returns <FC>
 */
const RiskForm = ({ formData, handleInputChange }: RiskFormProps) => {
  console.log("formData", formData);

  const navigate = useNavigate();

  const handleSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      // Create URLSearchParams object
      const queryParams = new URLSearchParams({
        riskLevel: formData.riskLevel,
        expenseRatio: formData.expenseRatio,
        returnRatio: formData.returnRatio || "", // Handle undefined
      }).toString();

      navigate(`/scanner/insights/${formData.assetType}?${queryParams}`);
      //   navigate(
      //     `/scanner/${formData.assetType}/riskLevel=${formData.riskLevel}&expenseRatio=${formData.expenseRatio}&returnRatio=${formData.returnRatio}`
      //   );
    } catch (error) {
      console.error("Error saving asset type:", error);
    }
  };

  return (
    <>
      <form className="risk-form" onSubmit={handleSubmit}>
        <AssetTypeSelect
          assetType={formData.assetType}
          handleInputChange={handleInputChange}
        />

        <RiskLevelSelect
          riskLevel={formData.riskLevel}
          handleInputChange={handleInputChange}
        />

        <ExpenseRatioSelect
          expenseRatio={formData.expenseRatio}
          handleInputChange={handleInputChange}
        />

        <ReturnRatioSelect
          returnRatio={formData.returnRatio}
          handleInputChange={handleInputChange}
        />

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
