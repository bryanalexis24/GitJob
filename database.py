from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker, declarative_base

# Creating database engine
engine = create_engine('sqlite:///jobs.db')
Base = declarative_base()

# Defining the job model
class Job(Base):
    __tablename__ = 'jobs'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    agency = Column(String)
    location = Column(String)
    url = Column(String)
    summary = Column(String)
    score = Column(Integer)
    tier = Column(String)

# Creating table
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Example of getting top-ranked job from resume match output
def save_top_job_to_db(top_job):
    job_entry = Job(
        title=top_job['title'],
        agency=top_job['agency'],
        location=top_job['location'],
        url=top_job['url'],
        summary=top_job['summary'],
        score=top_job['score'],
        tier=top_job['tier']
    )
    session.add(job_entry)
    session.commit()
    print("Top job saved to database")