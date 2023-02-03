import Navdisplay from "./Navdisplay";
import { useState } from "react";
import styles from "../styles/NavContainer.module.css";
import { data } from "./Data";
import Image from "next/image";
type props = {
  clubs: any;
  setClub: any;
};

export default function Navbar({ clubs, setClub }: props) {
  const [clicked, setClicked] = useState(false);
  return (
    <>
      <nav className="navbar navbar-dark bg-dark">
        <div className="container-fluid">
          <button
            className="navbar-toggler"
            type="button"
            style={{ height: "50px" }}
            aria-label="Toggle navigation"
            onClick={() => setClicked((prev: boolean) => !prev)}
          >
            <span className="navbar-toggler-icon"></span>
          </button>
          <span className={styles.Home}>
            <Image
              src={data.logo}
              alt="Picture of the author"
              width={40}
              height={60}
              priority
              onClick={() => setClub("England")}
            />
          </span>
        </div>
      </nav>
      {clicked && (
        <Navdisplay clubs={clubs} setClick={setClicked} setClub={setClub} />
      )}
    </>
  );
}
