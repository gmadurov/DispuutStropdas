import PropTypes from "prop-types";

const Dsani = ({ leden }) => {
  return (
    <>
      <div class="columns is-centered">
        <div class="column is-two-thirds">
          <div class="table is-bordered is-striped is-narrow is-fullwidth">
            <table style={{ width: "100%", border: "1px solid black" }}>
              <th>Datum</th>
              <th>Omschrijving</th>
              {leden.map((lid) => (
                <th>{lid.initials}</th>
              ))}
              {/* <th>{lid.initials}</th> */}
              {/* {% endfor %} */}
              {/* {% for event in events %} */}
              <tr>
                {/* <td style="text-align: center">{event.start_date|date:"l j F"}</td> */}
                {/* <td style="text-align: center">{event.description}</td> */}
                {/* {% for point in event.dsani_ev.all %} */}
                <span>
                  {/* {% if request.user.lid == point.lid or request.user|has_group:"Senate"%} */}
                  {/* <a href="{% url 'edit-dsani' point.id %}">{point.points}</a> */}
                  {/* {% else %} */}
                  {/* <p>{point.points}</p> */}
                  {/* {%endif%} */}
                </span>
                {/* </td> */}
                {/* {%endif%} */}
                {/* {%endfor%} */}
              </tr>
              {/* {% endfor %} */}
            </table>
          </div>
        </div>
      </div>
    </>
  );
};

Dsani.propTypes = {
  leden: PropTypes.any,
};

export default Dsani;
