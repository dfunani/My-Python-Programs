type props = {
  logo: string;
  name: string;
  setClub: any;
  setClick: any;
};

export default function Navteam({ logo, name, setClub, setClick }: props) {
  return (
    <>
      <div>
        <img
          src={logo}
          alt={name}
          onClick={() => {
            setClub(name);
            setClick((prev: any) => !prev);
          }}
        />
      </div>
    </>
  );
}
