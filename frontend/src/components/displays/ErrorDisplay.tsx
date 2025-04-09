import "./ErrorDisplay.css";

export interface ErrorDisplayProps {
  message: string;
}

const ErrorDisplay = ({ message }: ErrorDisplayProps) => (
  <div
    role="alert"
    className="error-container"
    style={{
      padding: "20px",
      margin: "20px",
      border: "1px solid #ff0000",
      borderRadius: "4px",
      backgroundColor: "#fff5f5",
      color: "#dc2626",
    }}
  >
    <h2>Error</h2>
    <p>{message}</p>
  </div>
);

export default ErrorDisplay;
