// import LINKS from "./LINKS"
import React, { useState } from "react";

import { Link } from "react-router-dom";
// import HoverDropdown from "./global/HoverDropdown";

const NavBar = () => {
  // <div className="columns is-centered">
  //   <div className="text">
  //     <div>
  //       <div>
  //         <img
  //           src="/images/blazoen.png"
  //           alt="Home"
  //           style={{ width: "50px", height: "100px" }}
  //         />
  //       </div>
  //     </div>
  //     <div className="column">
  //       <HoverDropdown
  //         dropText="Evenementen"
  //         items={
  //           <>
  //             <li>
  //               <Link to="/agenda">Agenda</Link>
  //             </li>
  //             <li>
  //               <Link to="/dsani">DSANI</Link>
  //             </li>
  //             <li>
  //               <Link to="/addevent">New Event</Link>
  //             </li>
  //             <li>
  //               <Link to="/test">Test</Link>
  //             </li>
  //           </>
  //         }
  //       />
  //     </div>
  //   </div>
  // </div>
  const [burger, setBurger] = useState(false);
  return (
    <nav
      className="navbar"
      role="navigation"
      aria-label="main navigation"
      style={{
        flexGrow: "1",
        flexDirection: "column",
        justifyContent: "center",
      }}
    >
      <div className="navbar-brand">
        <img
          src="/images/blazoen_1.gif"
          alt="Home"
          style={{ width: "50px", height: "40px" }}
        />
        <a className="navbar-item" href="">
          <img
            src="/images/dumspiro.gif"
            alt="DumSpiroSpero"
            style={{ width: "231px", height: "39px" }}
          />
        </a>

        <a
          role="button"
          className={burger ? "navbar-burger is-active" : "navbar-burger"}
          aria-label="menu"
          aria-expanded="false"
          onClick={() => setBurger(!burger)}
        >
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
          <span aria-hidden="true"></span>
        </a>
      </div>

      <div className={burger ? "navbar-menu is-active" : "navbar-menu"}>
        <div className="navbar-start">
          <div className="navbar-item"></div>
          <Link to="/agenda">
            <p className="navbar-item ">Agenda</p>
          </Link>
          <Link to="/dsani">
            <a className="navbar-item">DSANI</a>
          </Link>
        </div>
        <div className="navbar-end">
          <div className="navbar-item has-dropdown is-hoverable">
            <a className="navbar-link">Evenementen</a>
            <div className="navbar-dropdown">
              <li className="navbar-item">
                <Link to="/agenda">Agenda</Link>
              </li>
              <li className="navbar-item">
                <Link to="/dsani">DSANI</Link>
              </li>
              <li className="navbar-item">
                <Link to="/addevent">New Event</Link>
              </li>
              <hr className="navbar-divider" />
              <li className="navbar-item">
                <Link to="/test">Test</Link>
              </li>
            </div>
          </div>
        </div>
      </div>
    </nav>
  );
};
export default NavBar;
// <img src="%PUBLIC_URL%/images/blazoen.png" alt="Home" style={{width: '50px', height: '100px'}} />
//         hello
//       </span>

//     </div>
// <div className="column">

//   <div className="dropdown is-hoverable">
//     <span aria-haspopup="true" aria-controls="dropdown-menu4">
//       <span><a>Evenementen</a></span>
//     </span>
//     <div className="dropdown-menu" id="dropdown-menu4" role="menu">
//       <div className="dropdown-content">
//         <div className="dropdown-item">
//           <li>
//             {/* <a href="{%  url 'agenda'  %}">Agenda</a> */}
//           </li>
//           <li>
//             {/* <a href="{%  url 'DSANI'  %}">DSANI</a> */}
//           </li>
//         </div>
//       </div>
//     </div>
//   </div>
// </div>
//     <div className="column">

//       <div className="dropdown is-hoverable">
//         <span aria-haspopup="true" aria-controls="dropdown-menu4">
//           <span><a>Declas en Documenten</a></span>
//         </span>
//         <div className="dropdown-menu" id="dropdown-menu4" role="menu">
//           <div className="dropdown-content">
//             <div className="dropdown-item">
//               <li>
//                 {/* <a href="{%  url 'documents'  %}">Documents</a> */}
//               </li>
//               <li>
//                 {/* <a href="{%  url 'fileDecla'  %}">Decla</a> */}
//               </li>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//     <div className="column">

//       <div className="dropdown is-hoverable">
//         <span aria-haspopup="true" aria-controls="dropdown-menu4">
//           <span><a>Account</a></span>
//         </span>
//         <div className="dropdown-menu" id="dropdown-menu4" role="menu">
//           <div className="dropdown-content">
//             <div className="dropdown-item">
//               <li>
//                 {/* <a href="{%  url 'account'  %}">My Account (€{{ stand }})</a> */}
//               </li>
//               {/* {%if request.user|has_group:"Fiscus" %} */}
//               <li>
//                 {/* <a href="{% url 'verwerkenDecla'%}">Verwerkt Declas</a> */}
//               </li>
//               <li>
//                 {/* <a href="{% url 'exportDeclas'%}">Export Declas</a> */}
//               </li>
//               <li>
//                 {/* {%if request.user.is_superuser %} */}
//                 <Link to={`/admin`}>Admin</Link>
//                 {/* {% endif %} */}
//               </li>
//               <li>
//                 {/* <a href="{% url 'logout' %}">Logout</a> */}
//               </li>
//             </div>
//           </div>
//         </div>
//       </div>
//     </div>
//   </div>
//   {/* {% if messages %} {% for message in messages %}
//   <article id="alert" className="message is-{{message.tags}}">
//     <div className="message-header">
//       <p>{{ message }}</p>
//       <button className="delete" id="alert__close" aria-label="delete"></button>
//     </div>
//   </article>
//   {% endfor %} {% endif %} */}
// </div>
// <div className="columns">
//   <div className="column is-2">
//   </div>
// </div>
// </div>
// <hr />
// </> */}
