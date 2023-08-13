const Cell = ({ value }) => {
  let color = "white";
  if (value === "o") {
    color = "red";
  } else if (value === "x") {
    color = "yellow";
  }

  return (
    <td>
      <div className="cell">
        <div className={color}>
          <p>{value}</p>
        </div>
      </div>
    </td>
  );
};

export default Cell;
