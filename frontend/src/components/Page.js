import React from "react";

const Page = ({ element }) => {
  return (
    <div className="columns is-centered">
      <div className="column is-8">{element}</div>
    </div>
  );
};

export default Page;
