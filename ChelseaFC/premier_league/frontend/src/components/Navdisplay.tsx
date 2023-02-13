import Navteam from "./Navteam";
import styles from "../styles/Navbar.module.css";
import { useState } from "react";
import React from "react";
type props = {
  clubs: any;
  setClub: any;
  setClick: any;
};
export default function Navdisplay({ clubs, setClub, setClick }: props) {
  function GetNavDisplay(clubs: any): any {
    let res: any[] = [];
    clubs.forEach((element: any) => {
      res.push(
        <Navteam club={element} setClick={setClick} setClub={setClub} />
      );
    });
    return res;
  }
  return (
    <>
      <div className={`${styles.Container} bg-dark`}>
        {...GetNavDisplay(clubs)}
      </div>
    </>
  );
}
