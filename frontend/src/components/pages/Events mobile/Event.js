import PropTypes from "prop-types";
import React from "react";
// import { format } from "date-fns";
import moment from "moment";
import ClickDropdown from "../../global/ClickDropdown";
import EventForm from "./EventForm";

const Event = ({ event, onAdd, onEdit, onDelete }) => {
  let styleSummary;
  event.summary === "Wedstrijd"
    ? (styleSummary = { textAlign: "center", backgroundColor: "red" })
    : event.summary === "Dispuutsactiviteit"
    ? (styleSummary = {
        textAlign: "center",
        backgroundColor: "green",
        color: "white",
      })
    : event.summary === "Borrel"
    ? (styleSummary = {
        textAlign: "center",
        backgroundColor: "pink",
        color: "black",
      })
    : event.summary === "Dispuutsverjaardag"
    ? (styleSummary = { textAlign: "center", backgroundColor: "#bbd334" })
    : event.summary === "Clubactiviteit"
    ? (styleSummary = { textAlign: "center", backgroundColor: "yellow" })
    : event.summary === "Activiteit"
    ? (styleSummary = {
        textAlign: "center",
        backgroundColor: "rgba(35, 32, 209, 0.685)",
      })
    : (styleSummary = { textAlign: "center" });
  return (
    <div className="card columns">
      <div
        className="column is-2"
        style={{ textAlign: "center", paddingBottom: "10" }}
      >
        <b>start_date:</b>
        {event.start_date
          ? moment(event.start_date + "T" + event.start_time).format(
              "ddd Do MMM, hh:mmA"
            )
          : " "}{" "}
        {/* "{ event.start_date+'T'+event.start_time}" */}
      </div>

      <div className="column is-2" style={styleSummary}>
        <b>summary:</b>
        {event.summary ? event.summary : ""}
      </div>

      <div className="column is-2" style={{ textAlign: "center" }}>
        <b>description:</b>
        {event.description}
      </div>
      <div className="column is-2" style={{ textAlign: "center" }}>
        {event.kokers && (<b>kokers:</b> ,event.kokers.map((koker) => (koker.initials ? koker.initials : " ")))}
      </div>
      <div className="column is-2" style={{ textAlign: "center" }}>
        <b>kartrekkers:</b>
        {event.kartrekkers ? event.kartrekkers : ""}
      </div>
      <div className="column is-2" style={{ textAlign: "center" }}>
        <b>bijzonderheden:</b>
        {event.bijzonderheden ? event.bijzonderheden : ""}
      </div>
      <div className="column is-2" style={{ textAlign: "center" }}>
        <b>budget:</b>
        {event.budget ? event.budget : ""}
      </div>
      <div className="column is-2" style={{ textAlign: "center" }}>
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
      </div>
    </div>
  );
};

Event.propTypes = {
  event: PropTypes.any,
};

export default Event;

//{" "}
// {/* <div className="column is-2"style={{ textAlign: "center" }}> */}
// <a href="{% url 'editEvent' event.id %}">Edit</a>
// <a href="{% url 'deleteEvent' event.id %}">Delete</a>
//{" "}
