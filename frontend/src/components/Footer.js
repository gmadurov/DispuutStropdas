import { Link } from "react-router-dom";

const Footer = () => {
  return (
    <footer class="footer">
      <div className="columns is-centered">
        <div className="column is-one-forth"></div>
        <div class="column is-two-forth content has-text-centered">
          <h6>Copyright @ 2022</h6>
          <p>Version 20.4.0</p>
        </div>
        <div className="column is-one-forth">
          <p href="https://bulma.io/documentation/">
            <b>Legal</b>
          </p>
          <Link to="/privacy">
            <p>Privacy</p>
          </Link>
        </div>
      </div>
    </footer>
  );
};
console.log("");

export default Footer;
