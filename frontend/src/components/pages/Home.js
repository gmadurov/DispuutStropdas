export const Home = ({}) => {
  return (
    <>
      <body background="images/blazoen_small.jpg">
        <br />
        <br />
        <div style={{ textAlign: "center" }}>
          <img src="images/blazoen.png" usemap="#blazoen" />
          <map name="blazoen">
            <area
              shape="circle"
              coords="102,170,9"
              href="login"
              alt="Ga verder..."
            />
            <area
              shape="rect"
              coords="0,0,300,432"
              href="{% url 'fakePage'%}"
              alt="Ga verder..."
            />
          </map>

          <br />
          <br />
          <img src="images/dumspiro.gif" />

          <div id="block">
            Krabbendampad 16 <br />
            5611GW Eindhoven <br />
            <a href="tel: +31 (0) 40 308 01 55"> +31 (0) 40 308 01 55</a>
          </div>
        </div>
      </body>
    </>
  );
};
export default Home;
