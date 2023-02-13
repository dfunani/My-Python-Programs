import Image from "next/image";
import styles from "../styles/TeamCard.module.css";
import { useEffect, useState } from "react";
import Carousel from "./Carousel";
type props = {
  club: {};
  clicked: boolean;
};

export default function TeamCard({ club, clicked }: props) {
  const [fixtures, setFixtures] = useState([]);
  const [results, setResults] = useState([]);
  const [standing, setStanding] = useState({});

  useEffect(() => {
    Fixtures_API();
    Results_API();
    Standing_API();
  }, [club]);

  function Fixtures_API() {
    if (!club.id) return;
    fetch("http://127.0.0.1:8000/api-data/club/fixtures/" + club.id + "/")
      .then((res: any) => res.json())
      .then((rest: any) => setFixtures(() => rest))
      .catch((err) => console.log(err));
  }

  function Results_API() {
    if (!club.id) return;
    fetch("http://127.0.0.1:8000/api-data/club/results/" + club.id + "/")
      .then((res: any) => res.json())
      .then((rest: any) => setResults(() => rest))
      .catch((err) => console.log(err));
  }
  function Standing_API() {
    fetch("http://127.0.0.1:8000/api-data/club/standings/" + club.id + "/")
      .then((res: any) => res.json())
      .then((rest: any) => setStanding(() => rest))
      .catch((err) => console.log(err));
  }
  return (
    <>
      <div className={`${styles.Container} card bg-dark text-white`}>
        <Image
          src={club.logo}
          className={`${styles.Image} card-img`}
          fill
          alt="..."
        />

        <div className={`${styles.Bio} card bg-white text-white`}>
          <p>{club.biography}</p>
        </div>
        {fixtures[0] && (
          <Carousel
            fixtures={fixtures}
            results={results}
            standing={standing}
            clubName={club.name}
          />
        )}
      </div>
    </>
  );
}
