import PropTypes from "prop-types";
import React from "react";
const HoverDropdown = ({ dropText, items }) => {
  return (
    <div className="dropdown is-hoverable">
      <div aria-haspopup="true" aria-controls="dropdown-menu4">
        {dropText}
      </div>
      <div className="dropdown-menu" id="dropdown-menu4" role="menu">
        <div className="dropdown-items" style={{ textAlign: "center" }}>
          {items}
        </div>
      </div>
    </div>
  );
};
HoverDropdown.propTypes = {
  dropText: PropTypes.any.isRequired,
  items: PropTypes.any,
};
export default HoverDropdown;
