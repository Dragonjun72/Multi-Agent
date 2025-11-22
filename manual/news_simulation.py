
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.database.session import Base
from news.application.usecase.news_usecase import NewsUseCase
from news.infrastructure.orm.news_orm import NewsORM  # noqa: F401 - ensure metadata is loaded
from news.infrastructure.repository.news_repository_impl import NewsRepositoryImpl



def run_simulation():
    engine = create_engine("sqlite:///:memory:")
    SessionLocal = sessionmaker(bind=engine)
    Base.metadata.create_all(bind=engine)

    session = SessionLocal()
    try:
        usecase = NewsUseCase(FakeNaverNewsClient(), NewsRepositoryImpl(session))
        inserted = usecase.fetch_and_store("테스트")
        print(f"저장된 뉴스 건수: {len(inserted)}")

        for news in usecase.get_latest():
            print(f"[{news.id}] {news.title} | {news.link} | {news.pub_date}")
    finally:
        session.close()


if __name__ == "__main__":
    run_simulation()
