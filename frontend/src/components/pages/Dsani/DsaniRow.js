import React from "react";
import DsaniPoint from "./DsaniPoint";

const DsaniRow = ({ event, onEdit }) => {
  return (
    <tr>
      <td>{event.start_date}</td>
      <td>{event.description}</td>
      {event.dsani_ev?.map((point) => (
        <DsaniPoint
          key={"DsaniPoint" + point.id}
          point={point}
          onEdit={onEdit}
        />
      ))}
    </tr>
  );
};

export default DsaniRow;
