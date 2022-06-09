import PropTypes from "prop-types";
import React from "react";
// import { format } from "date-fns";
import moment from "moment";
import ClickDropdown from "../../global/ClickDropdown";
import EventForm from "./EventForm";

const Event = ({ event, onAdd, onEdit, onDelete }) => {
  let styleSummary;
  event.summary === "Wedstrijd"
    ? (styleSummary = { textAline: "center", backgroundColor: "red" })
    : event.summary === "Dispuutsactiviteit"
    ? (styleSummary = {
        textAline: "center",
        backgroundColor: "green",
        color: "white",
      })
    : event.summary === "Borrel"
    ? (styleSummary = {
        textAline: "center",
        backgroundColor: "pink",
        color: "black",
      })
    : event.summary === "Dispuutsverjaardag"
    ? (styleSummary = { textAline: "center", backgroundColor: "#bbd334" })
    : event.summary === "Clubactiviteit"
    ? (styleSummary = { textAline: "center", backgroundColor: "yellow" })
    : event.summary === "Activiteit"
    ? (styleSummary = {
        textAlign: "center",
        backgroundColor: "rgba(35, 32, 209, 0.685)",
      })
    : (styleSummary = { textAline: "center" });
  return (
    <tr>
      <td style={{ textAline: "center" }}>
        {event.start_date
          ? moment(event.start_date + "T" + event.start_time).format(
              "ddd Do MMM, hh:mmA"
            )
          : " "}{" "}
        {/* "{ event.start_date+'T'+event.start_time}" */}
      </td>

      <td style={styleSummary}>{event.summary ? event.summary : ""}</td>

      <td style={{ textAline: "center" }}>{event.description}</td>
      <td style={{ textAline: "center" }}>
        {event.kokers.map((koker) => (koker.initials ? koker.initials : " "))}
      </td>
      <td style={{ textAline: "center" }}>
        {event.kartrekkers ? event.kartrekkers : ""}
      </td>
      <td style={{ textAline: "center" }}>
        {event.bijzonderheden ? event.bijzonderheden : ""}
      </td>
      <td style={{ textAline: "center" }}>
        {event.budget ? event.budget : ""}
      </td>
      <td style={{ textAline: "center" }}>
        <ClickDropdown
          key={event.id}
          dropText="Edit"
          items={
            <>
              <EventForm
                key={event.id}
                id={event.id}
                pastevent={event}
                onAdd={onAdd}
                onEdit={onEdit}
                onDelete={onDelete}
              />
            </>
          }
        />
      </td>
    </tr>
  );
};

Event.propTypes = {
  event: PropTypes.any,
};

export default Event;

//{" "}
// {/* <td style={{ textAline: "center" }}> */}
// <a href="{% url 'editEvent' event.id %}">Edit</a>
// <a href="{% url 'deleteEvent' event.id %}">Delete</a>
//{" "}
