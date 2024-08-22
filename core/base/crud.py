from sqlalchemy import select, and_
from fastapi import HTTPException
from sqlalchemy.orm import Session, Query


class BaseCRUD:

    @staticmethod
    async def _delete(db: Session, data) -> None:

        try:
            db.delete(data)
            db.commit()
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=404,
                detail=e,
            )

    @staticmethod
    async def _save(db: Session, data) -> None:
        try:
            db.add(data)
            db.commit()
            db.refresh(data)
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=404,
                detail=e,
            )

    @staticmethod
    async def _update(db: Session, data) -> None:
        try:
            db.commit()
            db.refresh(data)
        except Exception as e:
            db.rollback()
            raise HTTPException(
                status_code=404,
                detail=e,
            )

    @classmethod
    async def _exist(cls, db: Session, table, this_id: str) -> bool:

        data = db.query(table).where(
            getattr(table, 'id') == this_id
        )

        return True if data.first() is not None else False

    @staticmethod
    async def _filter_by(db: Session, model, filters: dict) -> Query:
        valid_keys = model.__mapper__.c.keys()
        invalid_keys = [key for key in filters.keys() if key not in valid_keys]
        if invalid_keys:
            raise HTTPException(
                status_code=404,
                detail=f"Invalid keys '{invalid_keys}' for table '{model.name}'"
            )
        conditions = [getattr(model, key) == value for key, value in filters.items()]
        query = db.query(model).filter(and_(*conditions))
        return query

    @classmethod
    async def _get_by_id(cls, db: Session, model, this_id: str):

        filters: dict = {'id': this_id}

        data: Query = await cls._filter_by(
            db=db,
            model=model,
            filters=filters
        )

        data = data.first()
        if data is None:
            raise HTTPException(
                status_code=404,
                detail=f"Id {this_id} found"
            )

        return data

    @staticmethod
    async def _get_all(db: Session, table, page: int = 1, page_size: int = 10):

        offset = (page - 1) * page_size

        query = select(table).offset(offset).limit(page_size)
        result = db.execute(query)
        data = result.scalars().all()

        return data
