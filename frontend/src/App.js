import "./App.css";
import NavBar from "./components/NavBar";
import { useState, useEffect } from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import { default as EventsBrowser } from "./components/pages/Events/Events";
import { default as EventFormBrowser } from "./components/pages/Events/EventForm";
import { default as EventsMobile } from "./components/pages/Events mobile/Events";
import { default as EventFromMobile } from "./components/pages/Events mobile/EventForm";
import Test from "./components/Test";
import Dsani from "./components/pages/Dsani/Dsani";
import Footer from "./components/Footer";
import PrivacyPolicy from "./PrivacyPolicy";
// import Home from "./components/pages/Home";
import { BrowserView, MobileView } from "react-device-detect";

function App() {
  let API_URL = "http://localhost:8000/api/";
  let numberDSANIEvents = 25;
  const [paginator, setPaginator] = useState(1);
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

  const changePage = (page) => {
    setPaginator(page);
  };
  const maxPages = Math.ceil(dsaniEvents.length / numberDSANIEvents);
  const CurrentPosts = dsaniEvents.slice(
    (paginator - 1) * numberDSANIEvents,
    paginator * numberDSANIEvents
  );
  const fetchLeden = async () => {
    const res = await fetch(API_URL + "leden/");
    const data = await res.json();
    return data;
  };
  const fetchEvents = async () => {
    const res = await fetch(API_URL + "events/");
    const data = await res.json();
    return data;
  };
  const fetchDsani = async () => {
    const res = await fetch(API_URL + `dsani/`);
    const data = await res.json();
    return data;
  };

  // editing events
  const addEvent = async (event) => {
    console.log("done", event);
    const res = await fetch(API_URL + "create-event/", {
      method: "POST",
      headers: { "Content-type": "application/json" },
      body: JSON.stringify(event),
    });
    const data = await res.json();
    setEvents([...events, data]);
  };

  const toggleEvent = async (event1) => {
    const res = await fetch(API_URL + `edit-event/${event1.id}`, {
      method: "PUT",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(event1),
    });
    const data = await res.json();
    setEvents(events.map((event) => (event.id === event1.id ? data : event)));
  };
  // Delete events given an event
  const deleteEvent = async (event1) => {
    const res = await fetch(API_URL + `delete-event/${event1.id}`, {
      method: "DELETE",
      headers: {
        "Content-type": "application/json",
      },
    });
    const data = await res.json();
    console.log(data);
    setEvents(events.map((event) => event.id !== event1.id && event));
  };

  const editDsani = async (NI) => {
    const res = await fetch(API_URL + `edit-dsani/${NI.id}`, {
      method: "PUT",
      headers: {
        "Content-type": "application/json",
      },
      body: JSON.stringify(NI),
    });
    const data = await res.json();
    setDsani(
      // console.log(
      dsaniEvents.map((event) =>
        event.dsani_ev.map((point) => point.id === NI.id)
          ? {
              ...event,
              dsani_ev: event.dsani_ev.map((point) =>
                point.id === NI.id ? data : point
              ),
            }
          : event
      )
    );
  };

  // const deleteDsani = async (NI) => {
  //   const res = await fetch(API_URL+`delete-dsani/${NI.id}`, {
  //     method: "DELETE",
  //     headers: {
  //       "Content-type": "application/json",
  //     },
  //   });
  //   const data = await res.json();
  //   console.log(data);
  //   setDsani(dsaniEvents.map((event) => event.id !== NI.id && event));
  // };
  return (
    <Router>
      <div className="cointainer">
        <NavBar />
        {/* <Home/> */}
        <hr />
        <Routes>
          <Route
            path="/agenda"
            element={
              <>
                <BrowserView>
                  <EventsBrowser
                    allEvents={events}
                    onAdd={addEvent}
                    onEdit={toggleEvent}
                    onDelete={deleteEvent}
                  />
                </BrowserView>
                <MobileView>
                  <EventsMobile
                    allEvents={events}
                    onAdd={addEvent}
                    onEdit={toggleEvent}
                    onDelete={deleteEvent}
                  />
                </MobileView>
              </>
            }
          />
          <Route
            path="/dsani"
            element={
              <Dsani
                allEvents={CurrentPosts}
                onEdit={editDsani}
                leden={leden}
                paginate={changePage}
                current={paginator}
                maxPages={maxPages}
              />
            }
          />
          <Route path="/addevent" element={<EventFormBrowser onAdd={addEvent} />} />
          <Route path="/test" element={<Test />} />
          <Route path="/privacy" element={<PrivacyPolicy />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
