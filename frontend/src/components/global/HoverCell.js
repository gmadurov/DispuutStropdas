import React from "react";
import PropTypes from "prop-types";

const HoverCell = ({ dropText, items }) => {
  return (
    <td className="dropdown is-hoverable" style={{ display: "table-cell" }}>
      <div aria-haspopup="true" aria-controls="dropdown-menu">
        <p>{dropText} </p>
      </div>
      <div className="dropdown-menu" id="dropdown-menu" role="menu">
        <div className="dropdown-items" style={{ textAlign: "center" }}>
          {items}
        </div>
      </div>
    </td>
  );
};
HoverCell.propTypes = {
  dropText: PropTypes.any.isRequired,
  items: PropTypes.any,
};
export default HoverCell;
