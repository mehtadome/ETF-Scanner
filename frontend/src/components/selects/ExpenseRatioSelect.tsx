interface ExpenseRatioProps {
  expenseRatio: string;
  handleInputChange: (event: React.ChangeEvent<HTMLSelectElement>) => void;
}

/**
 *
 * @param { expenseRatio } string; Passed down to maintain disabled info selection.
 *        |-- Holds values "Low", "Medium", "High", "Very High", "Expensive".
 * @param { handleInputChange } function; Maintains state of form data.
 * @returns <FC>
 */
const ExpenseRatioSelect = ({
  expenseRatio,
  handleInputChange,
}: ExpenseRatioProps) => {
  return (
    <>
      <h3 className="risk-form-expense-ratio-title">Expense Ratio</h3>
      <select
        name="expenseRatio"
        className="risk-select-input"
        value={expenseRatio}
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
    </>
  );
};

export default ExpenseRatioSelect;
