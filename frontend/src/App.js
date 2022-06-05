import "./App.css";
import NavBar from "./components/NavBar";
import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Events from "./components/Events/Events";
import EventForm from "./components/Events/EventForm";
import Test from "./components/Test";
import Dsani from "./components/Events/Dsani";

function App() {
  const [events, setEvents] = useState([]);
  const [dsaniEvents, setDsani] = useState([]);
  const [leden, setLeden] = useState([]);
  useEffect(() => {
    const getEvent = async () => {
      let eventsFromServer = await fetchEvents();
      setEvents(eventsFromServer);
    };
    const startDsani = async () => {
      const DsaniFromServer = await fetchDsani();
      setDsani(DsaniFromServer);
    };
    const getLeden = async () => {
      var ledenFromServer = await fetchLeden();
      setLeden(ledenFromServer);
    };

    getLeden();
    getEvent();
    startDsani();
  }, []);

  const fetchLeden = async () => {
    const res = await fetch("http://localhost:8000/api/leden/");
    const data = await res.json();
    return data;
  };
  const fetchEvents = async () => {
    const res = await fetch("http://localhost:8000/api/events/");
    const data = await res.json();
    return data;
  };
  const fetchDsani = async () => {
    const res = await fetch("http://localhost:8000/api/dsani/");
    const data = await res.json();
    return data;
  };

  // editing events
  const addEvent = async (event) => {
    console.log("done", event);
    const res = await fetch("http://localhost:8000/api/create-event/", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(event),
    });
    const data = await res.json();
    setEvents([...events, data]);
  };

  const toggleEvent = async (event1) => {
    const res = await fetch(
      `http://localhost:8000/api/edit-event/${event1.id}`,
      {
        method: "PUT",
        headers: {
          "Content-type": "application/json",
        },
        body: JSON.stringify(event1),
      }
    );
    const data = await res.json();
    setEvents(events.map((event) => (event.id === event1.id ? data : event)));
    // useEffect()
  };
  // Delete events given an event
  const deleteEvent = async (event1) => {
    const res = await fetch(
      `http://localhost:8000/api/delete-event/${event1.id}`,
      {
        method: "DELETE",
        headers: {
          "Content-type": "application/json",
        },
      }
    );
    setEvents(events.map((event) => event.id !== event1.id && event));
  };

  const editDsani = async (NI) => {
    const res = await fetch(`http://localhost:8000/api/edit-event/${NI.id}`, {
      method: "PUT",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(NI),
    });
    const data = await res.json();
    setDsani(dsaniEvents.map((event) => (event.id === NI.id ? data : event)));
    // useEffect()
  };

  const deleteDsani = async (NI) => {
    const res = await fetch(`http://localhost:8000/api/delete-dsani/${NI.id}`, {
      method: "DELETE",
      headers: {
        "Content-type": "application/json",
      },
    });
    setDsani(dsaniEvents.map((event) => event.id !== NI.id && event));
  };

  return (
    <Router>
      <div className="cointainer">
        <NavBar />
        <hr />
        <Routes>
          <Route
            path="/agenda"
            element={
              <Events
                allEvents={events}
                onAdd={addEvent}
                onEdit={toggleEvent}
                onDelete={deleteEvent}
              />
            }
          />
          <Route
            path="/dsani"
            element={
              <Dsani
                allEvents={dsaniEvents}
                onEdit={editDsani}
                onDelete={deleteDsani}
                leden={leden}
              />
            }
          />
          <Route path="/addevent" element={<EventForm onAdd={addEvent} />} />
          <Route path="/test" element={<Test />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
