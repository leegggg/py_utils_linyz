from datetime import datetime
from threading import Thread
from .dao import Base, DzCommonMember, DzForum, DzForumPost, DzForumThread, DzLinkDict
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
from sqlalchemy.sql import func


class DzService():
    def __init__(self, dbUrl) -> None:
        self.dbUrl = dbUrl
        self.engine = create_engine(self.dbUrl)
        Base.metadata.create_all(self.engine)
        self.Session = sessionmaker(bind=self.engine)

    def insertOrUpdate(self, obj, merge=False) -> bool:
        if not obj:
            return False
        obj.mod_date = datetime.now()
        session = self.Session()
        try:
            if not merge:
                session.add(obj)
            else:
                session.merge(obj)
            session.commit()
        except IntegrityError:
            session.close()
            return False
        return True

    def postDzForum(self, siteId, forum: DzForum, siteIdMatch=None) -> int:
        """postDzForum object.
        :param siteId: siteId for the object unique in whole system.
        :param forum: forum obj.

        return: int : fid
                      Could be negitave if fid siteId existes.
                      None if failed.

        """
        session = self.Session()
        dzId = None
        try:
            with session.begin():
                session.add(forum)
                session.flush()
                link = DzLinkDict()
                link.dzId = forum.fid
                if not siteIdMatch:
                    siteIdMatch = siteId
                link.siteIdMatch = siteIdMatch
                link.siteId = siteId
                session.add(link)
                dzId = link.dzId
        except IntegrityError:
            link: DzLinkDict = session.query(DzLinkDict).filter(DzLinkDict.siteId == siteId).one_or_none()
            if link:
                dzId = -1 * link.dzId
        return dzId

    def postDzThread(self, siteId, thread: DzForumThread, siteIdMatch=None) -> int:
        """postDzThread object.
        :param siteId: siteId for the object unique in whole system.
        :param thread: forum obj.

        return: int : tid
                      Could be negitave if fid siteId existes.
                      None if failed.

        """
        session = self.Session()
        dzId = None
        try:
            with session.begin():
                session.add(thread)
                session.flush()
                link = DzLinkDict()
                link.dzId = thread.tid
                if not siteIdMatch:
                    siteIdMatch = siteId
                link.siteIdMatch = siteIdMatch
                link.siteId = siteId
                session.add(link)
                dzId = link.dzId
        except IntegrityError:
            link: DzLinkDict = session.query(DzLinkDict).filter(DzLinkDict.siteId == siteId).one_or_none()
            if link:
                dzId = -1 * link.dzId
        return dzId

    def postDzPost(self, siteId, post: DzForumPost, siteIdMatch=None) -> int:
        """postDzPost object.
        :param siteId: siteId for the object unique in whole system.
        :param post: forum obj.

        return: int : pid
                      Could be negitave if fid siteId existes.
                      None if failed.

        """
        session = self.Session()
        dzId = None
        try:
            with session.begin():
                maxPosition = session.query(func.max(DzForumPost.position)).filter(DzForumPost.tid == post.tid).scalar()
                if not maxPosition:
                    maxPosition = 0
                post.position = maxPosition + 1
                maxPid = session.query(func.max(DzForumPost.pid)).scalar()
                if not maxPid:
                    maxPid = 0
                post.pid = maxPid + 1
                session.add(post)
                link = DzLinkDict()
                link.dzId = post.pid
                if not siteIdMatch:
                    siteIdMatch = siteId
                link.siteIdMatch = siteIdMatch
                link.siteId = siteId
                session.add(link)
                dzId = link.dzId
        except IntegrityError as e:
            e
            link: DzLinkDict = session.query(DzLinkDict).filter(DzLinkDict.siteId == siteId).one_or_none()
            if link:
                dzId = -1 * link.dzId
        return dzId

    def postDzMember(self, siteId, member: DzCommonMember, siteIdMatch=None) -> int:
        """postDzMember object.
        :param siteId: siteId for the object unique in whole system.
        :param member: forum obj.

        return: int : uid
                      Could be negitave if fid siteId existes.
                      None if failed.

        """
        session = self.Session()
        dzId = None
        try:
            with session.begin():
                session.add(member)
                session.flush()
                link = DzLinkDict()
                link.dzId = member.uid
                if not siteIdMatch:
                    siteIdMatch = siteId
                link.siteIdMatch = siteIdMatch
                link.siteId = siteId
                session.add(link)
                dzId = link.dzId
        except IntegrityError as e:
            e
            link: DzLinkDict = session.query(DzLinkDict).filter(DzLinkDict.siteId == siteId).one_or_none()
            if link:
                dzId = -1 * link.dzId
            else:
                pass
        return dzId

    def getDzIdBySiteId(self, siteId) -> int:
        session = self.Session()
        return session.query(DzLinkDict.dzId).filter(DzLinkDict.siteId == siteId).scalar()
