import Table from "react-bootstrap/Table";

function ResponsiveExample({ standing, clubName }: any) {
  standing = {
    team_id: 4066,
    position: 1,
    points: 78,
    status: "Promotion",
    result: "Champions League",
    overall: {
      games_played: 34,
      won: 24,
      draw: 6,
      lost: 4,
      goals_diff: 55,
      goals_scored: 99,
      goals_against: 44,
    },
    home: {
      games_played: 17,
      won: 13,
      draw: 4,
      lost: 0,
      goals_diff: 43,
      goals_scored: 64,
      goals_against: 21,
    },
    away: {
      games_played: 17,
      won: 11,
      draw: 2,
      lost: 4,
      goals_diff: 12,
      goals_scored: 35,
      goals_against: 23,
    },
  };
  return (
    <Table responsive className="text-light">
      <thead>
        <tr>
          <th>#</th>
          <th key={1}>Team</th>
          <th key={2}>Pts</th>
          <th key={2}>Games</th>
          <th key={3}>W</th>
          <th key={4}>D</th>
          <th key={5}>L</th>
          <th key={6}>GD</th>
          <th key={7}>GS</th>
          <th key={8}>GA</th>
        </tr>
      </thead>
      <tbody>
        <tr>
          <td>{standing.position}</td>
          <td key={1}>{clubName}</td>
          <td key={2}>{standing.points}</td>
          <td key={2}>{standing.overall.games_played}</td>
          <td key={3}>{standing.overall.won}</td>
          <td key={4}>{standing.overall.draw}</td>
          <td key={5}>{standing.overall.lost}</td>
          <td key={6}>{standing.overall.goals_diff}</td>
          <td key={7}>{standing.overall.goals_scored}</td>
          <td key={8}>{standing.overall.goals_against}</td>
        </tr>
      </tbody>
    </Table>
  );
}

export default ResponsiveExample;
