import Navdisplay from "./Navdisplay";
import { useState } from "react";
import styles from "../styles/NavContainer.module.css";
import { data } from "./Data";

import Image from "next/image";

import TeamCard from "@/components/TeamCard";
type props = {
  clubs: any;
  setClub: any;
  clicked: any;
  setClicked: any;
  club: any;
};

export default function Navbar({
  clubs,
  setClub,
  clicked,
  setClicked,
  club,
}: props) {
  return (
    <>
      {clicked && (
        <Navdisplay clubs={clubs} setClick={setClicked} setClub={setClub} />
      )}

      <TeamCard club={club} clicked={clicked} />
    </>
  );
}
