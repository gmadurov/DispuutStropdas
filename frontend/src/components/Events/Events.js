import PropTypes from "prop-types";
import Event from "./Event";
import Page from "../Page";
import EventForm from "./EventForm";
import ClickDropdown from "../global/ClickDropdown";

const Events = ({ allEvents, onAdd, onEdit, onDelete }) => {
  return (
    <Page
      element={
        <>
          <div className="table is-bordered is-striped is-narrow is-hoverable is-centered is-three-forths">
            <table style={{ width: "100%", border: "1px solid black" }}>
              <tbody>
                <tr>
                  <th>Datum</th>
                  <th>Activiteit</th>
                  <th>Omschrijving</th>
                  <th>Kokers</th>
                  <th>Kartrekkers</th>
                  <th>Bijzonderheden</th>
                  <th>Budget</th>
                  <th>
                    <ClickDropdown
                      dropText="Event Toevogen"
                      items={<EventForm onDelete={onDelete} onAdd={onAdd} onEdit={()=>(alert('Event cannot be changed if it hasnt been created first'))}/>}
                    />
                  </th>
                </tr>
                {allEvents?.map((event) => (
                  <Event
                    key={event.id}
                    event={event}
                    onAdd={onAdd}
                    onEdit={onEdit}
                    onDelete={onDelete}
                  />
                ))}
              </tbody>
            </table>
          </div>
        </>
      }
    />
  );
};

Events.propTypes = {
  allEvents: PropTypes.any,
};

export default Events;
