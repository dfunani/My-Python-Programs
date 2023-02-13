import { useState } from "react";
import Carousel2 from "react-bootstrap/Carousel";
import Table from "./Table";
type props = {
  fixtures: any;
  results: any;
  standing: any;
  clubName: any;
};

export default function Carousel({
  fixtures,
  results,
  standing,
  clubName,
}: props) {
  function GetFixtures() {
    return fixtures.map((a: any, i: number) => {
      return (
        <Carousel2.Item>
          <div style={{ display: "flex", justifyContent: "space-evenly" }}>
            <img src={a.home_team.logo} alt="First slide" />
            <div
              style={{
                display: "flex",
                justifyContent: "flex-start",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <p style={{ textAlign: "center" }}>
                {a.venue?.name}
                <br></br>
                {parseInt(a.venue?.capacity).toLocaleString("en-GB")} Seats
                <br></br>
                <div style={{ fontSize: "30px" }}>VS</div>
                {a.match_start}
              </p>
            </div>
            <img src={a.away_team.logo} alt="First slide" />
          </div>
        </Carousel2.Item>
      );
    });
  }

  function GetResults() {
    return results.map((a: any, i: number) => {
      return (
        <Carousel2.Item>
          <div style={{ display: "flex", justifyContent: "space-evenly" }}>
            <img src={a.home_team.logo} alt="First slide" />
            <div
              style={{
                display: "flex",
                justifyContent: "flex-start",
                flexDirection: "column",
                alignItems: "center",
              }}
            >
              <p style={{ textAlign: "center" }}>
                {a.venue?.name}
                <br></br>
                {parseInt(a.venue?.capacity).toLocaleString("en-GB")} Seats
                <br></br>
                <div style={{ fontSize: "30px" }}>0 - 0</div>
                {a.match_start}
              </p>
            </div>
            <img src={a.away_team.logo} alt="First slide" />
          </div>
        </Carousel2.Item>
      );
    });
  }
  return (
    <>
      <div
        style={{
          display: "flex",
          flexDirection: "column",
          justifyContent: "center",
          alignItems: "left",
          minWidth: "75%",
          paddingRight: "40px",
        }}
      >
        <Carousel2
          style={{
            marginBlock: "20px",
            height: "10em",
          }}
        >
          {GetFixtures()}
        </Carousel2>
        <Carousel2
          style={{
            marginBlock: "20px",
            height: "10em",
          }}
        >
          {GetResults()}
        </Carousel2>
        <div
          style={{
            color: "white",
            overflow: "scroll",
            backgroundColor: "transparent",
            zIndex: 2,
          }}
        >
          <Table standing={standing} clubName={clubName} />
        </div>
      </div>
    </>
  );
}
