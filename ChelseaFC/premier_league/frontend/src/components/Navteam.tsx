type props = {
  setClub: any;
  setClick: any;
  club: any;
};

export default function Navteam({ club, setClub, setClick }: props) {
  return (
    <>
      <div>
        <img
          src={club.logo}
          alt={club.name}
          onClick={() => {
            setClub(club);
            setClick((prev: any) => !prev);
          }}
        />
      </div>
    </>
  );
}
