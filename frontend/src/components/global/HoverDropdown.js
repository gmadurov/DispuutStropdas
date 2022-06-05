import PropTypes from "prop-types";

const HoverDropdown = ({ dropText, items }) => {
  return (
    <div className="dropdown is-hoverable">
      <div aria-haspopup="true" aria-controls="dropdown-menu4">
        <div>{dropText}</div>
      </div>
      <div className="dropdown-menu" id="dropdown-menu4" role="menu">
            <div className="dropdown-items" style={{textAlign:'center'}}>{items}</div>
        </div>
    </div>
  );
};
HoverDropdown.propTypes = {
  dropText: PropTypes.string.isRequired,
  items: PropTypes.any,
};
export default HoverDropdown;
