from sqlalchemy.schema import Column
from sqlalchemy import create_engine, select, delete, update
from sqlalchemy.orm import declarative_base, Session
from settings import dbConnectionString
from sqlalchemy.types import String, Integer, JSON

engine = create_engine(dbConnectionString)

base = declarative_base()


class Club(base):
    __tablename__ = "Clubs"

    id = Column(Integer, primary_key=True)
    team_id = Column(Integer)
    name = Column(String(30))
    short_code = Column(String(5), nullable=True)
    common_name = Column(String(30), nullable=True)
    logo = Column(String(255))
    country_id = Column(Integer, default=42)
    country_name = Column(String(125), default="England")
    country_code = Column(String(5), default="en")
    continent = Column(String(30), default="Europe")
    country_flag = Column(String(
        255), default="https://cdn.britannica.com/44/344-004-494CC2E8/Flag-England.jpg")
    league_id = Column(Integer, default=237)
    season = Column(JSON, default={})
    standing = Column(JSON, nullable=True)
    matches = Column(JSON, default={})
    biography = Column(String(65651), default="Biography goes here")
    trophies = Column(JSON, default={})

    def Add(self):
        id = self.id
        team_id = self.team_id
        name = self.name
        with Session(engine) as session:
            session.add(self)
            session.commit()
        return {'status': 'added', 'code': 'DB_200', 'result': {'id': id, 'team_id': team_id, 'name': name}}

    def Delete(self, id):
        with Session(engine) as session:
            session.execute(delete(Club).where(Club.team_id == id))
            session.commit()
        return {'status': 'deleted', 'code': 'DB_200', 'result': id}

    def Update(self, id, matches, season, standing=None):
        with Session(engine) as session:
            if matches:
                session.execute(update(Club).where(
                    Club.team_id == id).values(matches=matches, season=season))
            if standing:
                session.execute(update(Club).where(
                    Club.team_id == id).values(standing=standing))
            session.commit()
        return {'status': 'updated', 'code': 'DB_200', 'result': id}

    def FetchAll(self):
        with Session(engine) as session:
            result = session.scalars(select(Club.team_id)).all()
        return {'status': 'success', 'code': 'DB_200', 'result': result}

    def FetchNames(self):
        with Session(engine) as session:
            result = session.scalars(select(Club.name)).all()
        return {'status': 'success', 'code': 'DB_200', 'result': result}

    def UpdateBio(self, bio, club):
        with Session(engine) as session:
            session.execute(update(Club).where(
                Club.name == club).values(biography=bio))
            session.commit()
        return {'status': 'updated', 'code': 'DB_200', 'result': club}
