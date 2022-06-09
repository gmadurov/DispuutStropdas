import PropTypes from "prop-types";
import React from "react";
import DsaniRow from "./DsaniRow";
import Paginator from "../../global/Paginator";
const Dsani = ({ leden, allEvents, onEdit, paginate, current, maxPages }) => {
  return (
    <>
      <div className="columns is-centered">
        <div className="column is-two-thirds">
          <div className="table is-bordered is-striped is-narrow is-fullwidth">
            <table style={{ width: "100%", border: "1px solid black" }}>
              <thead>
                <tr>
                  <th>Datum</th>
                  <th>Omschrijving</th>
                  {leden?.map((lid) => (
                    <th key={lid.id}>{lid.initials}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {allEvents?.map((event) => (
                  <DsaniRow
                    key={"row" + event.id}
                    event={event}
                    onEdit={onEdit}
                  />
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
      <Paginator
        numberOfPages={maxPages}
        current={current}
        paginate={paginate}
      />
    </>
  );
};

Dsani.propTypes = {
  leden: PropTypes.any,
};

export default Dsani;
