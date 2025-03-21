import { Top10ETFs } from "../components/displays/top10ETFsDisplay";
import { Top10MutualFunds } from "../components/displays/top10MFsDisplay";
import "./HomePage.css";
import { ConnTest } from "../components/displays/connectionDisplay";
import RiskForm from "../components/forms/riskForm";
import { useNavigate } from "react-router-dom";
import { useState } from "react";

export interface ScannerProps {
  returnParam?: string;
}

const returnParam = "1 Yr Return";

/**
 *
 */
const HomePage = () => {
  //const navigate = useNavigate();

  // Local state management
  const [formData, setFormData] = useState({
    assetType: "",
    riskLevel: "",
    expenseRatio: "",
    returnRatio: "",
  });

  const handleInputChange = (event: React.ChangeEvent<HTMLSelectElement>) => {
    const { name, value } = event.target;
    setFormData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  return (
    <>
      <RiskForm formData={formData} handleInputChange={handleInputChange} />

      <ConnTest />
    </>
  );
};

export default HomePage;
