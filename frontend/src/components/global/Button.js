import React from "react";

const Button = ({ text, action, value, type, color, onClick }) => {
  return (
    <button
      type={type}
      className={"button "+color}
      value={value}
      onClick={onClick}
    >
      {text}
    </button>
  );
};

export default Button;
