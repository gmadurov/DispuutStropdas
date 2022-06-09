import React, { useState } from "react";
import Button from "../../global/Button";
// import Page from "../Page";
// import App from '../../App'

const EventForm = ({ id, pastevent, onAdd, onEdit, onDelete }) => {
  const [deleted, setDeleted] = useState(false);
  const [summary, setSummary] = useState(
    pastevent ? pastevent.summary : "Activiteit"
  );
  const [description, setDescription] = useState(
    pastevent ? pastevent.description : ""
  );
  const [start_date, setStart_date] = useState(
    pastevent ? pastevent.start_date : ""
  );
  const [start_time, setStart_time] = useState(
    pastevent ? pastevent.start_time : "17:00"
  );
  const [end_date, setEnd_date] = useState(pastevent ? pastevent.end_date : "");
  const [end_time, setEnd_time] = useState(
    pastevent ? pastevent.end_time : "23:59"
  );
  const [recuring, setRecuring] = useState(pastevent ? pastevent.recuring : "");
  const [location, setLocation] = useState(pastevent ? pastevent.location : "");
  const [kokers, setKokers] = useState(pastevent ? pastevent.kokers : []);
  const [kartrekkers, setKartrekkers] = useState(
    pastevent ? pastevent.kartrekkers : ""
  );
  const [info, setInfo] = useState(pastevent ? pastevent.info : "");
  const [budget, setBudget] = useState(pastevent ? pastevent.budget : "");
  const [bijzonderheden, setBijzonderheden] = useState(
    pastevent ? pastevent.bijzonderheden : "Op Afmelding"
  );
  const onSubmit = (e) => {
    // console.log("id =", pastevent.id, key);

    e.preventDefault();
    if (!summary) {
      alert("Prease add summary");
      return;
    }
    if (deleted | !pastevent) {
      onAdd({
        summary,
        description,
        start_date,
        start_time,
        end_date,
        end_time,
        recuring,
        location,
        kokers,
        kartrekkers,
        info,
        budget,
        bijzonderheden,
      });
    } else {
      onEdit({
        id,
        summary,
        description,
        start_date,
        start_time,
        end_date,
        end_time,
        recuring,
        location,
        kokers,
        kartrekkers,
        info,
        budget,
        bijzonderheden,
      });
    }
    setDeleted(false);
    setSummary(summary ? summary : "");
    setDescription(description ? description : "");
    setStart_date(start_date ? start_date : "");
    setStart_time(start_time ? start_time : "");
    setEnd_date(end_date ? end_date : "");
    setEnd_time(end_time ? end_time : "");
    setRecuring(recuring ? recuring : "");
    setLocation(location ? location : "");
    setKokers(kokers ? kokers : []);
    setKartrekkers(kartrekkers ? kartrekkers : "");
    setInfo(info ? info : "");
    setBudget(budget ? budget : "");
    setBijzonderheden(bijzonderheden ? bijzonderheden : "");
  };
  const Delete = (e) => {
    onDelete({
      id,
    });
    setDeleted(!deleted);
    setSummary(summary ? summary : "");
    setDescription(description ? description : "");
    setStart_date(start_date ? start_date : "");
    setStart_time(start_time ? start_time : "");
    setEnd_date(end_date ? end_date : "");
    setEnd_time(end_time ? end_time : "");
    setRecuring(recuring ? recuring : "");
    setLocation(location ? location : "");
    setKokers(kokers ? kokers : []);
    setKartrekkers(kartrekkers ? kartrekkers : "");
    setInfo(info ? info : "");
    setBudget(budget ? budget : "");
    setBijzonderheden(bijzonderheden ? bijzonderheden : "");
  };
  return (
    <div className="column is-8">
      <form className="add-form" onSubmit={onSubmit}>
        <table>
          <tbody>
            <tr>
              <th>Edit event</th>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_summary">Summary:</label>
              </th>
              <td>
                <select
                  className="input"
                  name="summary"
                  id="id_summary"
                  onChange={(e) => setSummary(e.target.value)}
                  value={summary}
                  required
                >
                  <option value="Activiteit">Activiteit</option>
                  <option value="Borrel">Borrel</option>
                  <option value="Clubactiviteit">Clubactiviteit</option>
                  <option value="Wedstrijd">Wedstrijd</option>
                  <option value="Dispuutsactiviteit">Dispuutsactiviteit</option>
                  <option value="Dispuutsverjaardag">Dispuutsverjaardag</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_description">Description:</label>
              </th>
              <td>
                <input
                  type="text"
                  name="description"
                  value={description}
                  maxLength="50"
                  className="input"
                  id="id_description"
                  onChange={(e) => setDescription(e.target.value)}
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_start_date">Start date:</label>
              </th>
              <td>
                <input
                  type="date"
                  name="start_date"
                  value={start_date}
                  className="input"
                  required
                  id="id_start_date"
                  onChange={(e) => setStart_date(e.target.value)}
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_start_time">Start time:</label>
              </th>
              <td>
                <input
                  type="time"
                  name="start_time"
                  value={start_time}
                  className="input"
                  onChange={(e) => setStart_time(e.target.value)}
                  id="id_start_time"
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_end_date">End date:</label>
              </th>
              <td>
                <input
                  type="date"
                  name="end_date"
                  value={end_date}
                  className="input"
                  id="id_end_date"
                  onChange={(e) => setEnd_date(e.target.value)}
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_end_time">End time:</label>
              </th>
              <td>
                <input
                  type="time"
                  name="end_time"
                  value={end_time}
                  className="input"
                  id="id_end_time"
                  onChange={(e) => setEnd_time(e.target.value)}
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_recuring">Recuring:</label>
              </th>
              <td>
                <select
                  name="recuring"
                  value={recuring}
                  className="input"
                  id="id_recuring"
                  onChange={(e) => setRecuring(e.target.value)}
                >
                  <option value="0">None</option>
                  <option value="1">Weekly</option>
                  <option value="2">Monthly</option>
                  <option value="3">Yearly</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_location">Location:</label>
              </th>
              <td>
                <input
                  type="text"
                  name="location"
                  value={location}
                  maxLength="50"
                  className="input"
                  onChange={(e) => setLocation(e.target.value)}
                  id="id_location"
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_kokers">Kokers:</label>
              </th>
              <td>
                <select
                  name="kokers"
                  value={kokers}
                  className="input"
                  id="id_kokers"
                  multiple
                  onChange={(e) => setKokers(e.target.value)}
                >
                  <option value="1">KAST</option>
                  <option value="2">Bank</option>
                  <option value="19900">STROPDAS</option>
                  <option value="3">Reunisten</option>
                  <option value="20161">EHopman</option>
                  <option value="20162">LRijn</option>
                  <option value="20163">RWerf</option>
                  <option value="20171">RSikkema</option>
                  <option value="20172">JKlei</option>
                  <option value="20173">MHulsen</option>
                  <option value="20174">SVijverberg</option>
                  <option value="20181">VNanne</option>
                  <option value="20182">HWeersink</option>
                  <option value="20183">JRaap</option>
                  <option value="20184">DGalen</option>
                  <option value="20191">CZantvoort</option>
                  <option value="20201">OMark</option>
                  <option value="20202">LWöstemeier</option>
                  <option value="20203">MBosman</option>
                  <option value="20204">GMaduro</option>
                </select>
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_kartrekkers">Kartrekkers:</label>
              </th>
              <td>
                <input
                  type="text"
                  name="kartrekkers"
                  value={kartrekkers}
                  maxLength="50"
                  className="input"
                  onChange={(e) => setKartrekkers(e.target.value)}
                  id="id_kartrekkers"
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_info">Info:</label>
              </th>
              <td>
                <textarea
                  name="info"
                  value={info}
                  cols="40"
                  rows="10"
                  onChange={(e) => setInfo(e.target.value)}
                  className="input"
                  id="id_info"
                ></textarea>
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_budget">Budget:</label>
              </th>
              <td>
                <input
                  type="text"
                  name="budget"
                  value={budget}
                  onChange={(e) => setBudget(e.target.value)}
                  maxLength="50"
                  className="input"
                  id="id_budget"
                />
              </td>
            </tr>
            <tr>
              <th>
                <label htmlFor="id_bijzonderheden">Bijzonderheden:</label>
              </th>
              <td>
                <select
                  name="bijzonderheden"
                  value={bijzonderheden}
                  className="input"
                  id="id_bijzonderheden"
                  onChange={(e) => setBijzonderheden(e.target.value)}
                >
                  <option value="Op Afmelding">Op Afmelding</option>
                  <option value="Op Aanmelding">Op Aanmelding</option>
                  <option value=" "> </option>
                </select>
              </td>
            </tr>
          </tbody>
        </table>
      </form>
      <Button
        value="Submit"
        text={deleted ? "undo" : "Submit"}
        type="Submit"
        color="is-success"
        onClick={onSubmit}
      />
      {pastevent && (
        <Button
          type="delete"
          text="Delete"
          color="is-danger"
          onClick={Delete}
        />
      )}
    </div>
  );
};

export default EventForm;
