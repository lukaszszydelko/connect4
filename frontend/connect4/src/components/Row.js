import Cell from "./Cell";

// Row component
const Row = ({ row, makeMove, rowIndex }) => {
  return (
    <tr>
      <td>
        <div
          className="button"
          onClick={() => {
            makeMove(rowIndex, "L");
          }}
        >
          Push left
        </div>
      </td>
      {row.map((cell, i) => (
        <Cell key={i} value={cell} />
      ))}
      <td>
        <div
          className="button"
          onClick={() => {
            makeMove(rowIndex, "R");
          }}
        >
          Push right
        </div>
      </td>
    </tr>
  );
};

export default Row;
