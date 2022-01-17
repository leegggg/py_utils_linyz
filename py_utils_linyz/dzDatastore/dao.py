
# from sqlalchemy import create_engine
from datetime import datetime
import enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Enum, TEXT
from sqlalchemy import PrimaryKeyConstraint
import logging
import uuid

# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import IntegrityError
# from datetime import datetime

Base = declarative_base()


class DzLinkDict(Base):
    __tablename__ = 'dzlnk_dict'
    siteId = Column(String(255), primary_key=True, name="site_id")
    siteIdMatch = Column(String(255), name="site_id_match")
    dzId = Column(Integer, name="dz_id")
    comment = Column(String(255))
    mod_date = Column(DateTime, default=datetime.now())
    create_date = Column(DateTime, default=datetime.now())

    __table_args__ = (
        PrimaryKeyConstraint('site_id'),
        {},
    )


class ForumTypeEnum(enum.Enum):
    group = 1
    forum = 2
    sub = 3


class DzForum(Base):
    __tablename__ = 'dz35_forum_forum'
    fid = Column(name="fid", type_=Integer, autoincrement=True)
    fup = Column(name="fup", type_=Integer, default=1)
    type = Column(name="type", type_=Enum(ForumTypeEnum), default='forum')
    name = Column(name="name", type_=String(50), default='')
    status = Column(name="status", type_=Integer, default=1)
    displayorder = Column(name="displayorder", type_=Integer, default=0)
    styleid = Column(name="styleid", type_=Integer, default=0)
    threads = Column(name="threads", type_=Integer, default=0)
    posts = Column(name="posts", type_=Integer, default=0)
    todayposts = Column(name="todayposts", type_=Integer, default=0)
    yesterdayposts = Column(name="yesterdayposts", type_=Integer, default=0)
    rank = Column(name="rank", type_=Integer, default=0)
    oldrank = Column(name="oldrank", type_=Integer, default=0)
    lastpost = Column(name="lastpost", type_=String(110), default='')
    domain = Column(name="domain", type_=String(15), default='')
    allowsmilies = Column(name="allowsmilies", type_=Integer, default=1)
    allowhtml = Column(name="allowhtml", type_=Integer, default=0)
    allowbbcode = Column(name="allowbbcode", type_=Integer, default=1)
    allowimgcode = Column(name="allowimgcode", type_=Integer, default=1)
    allowmediacode = Column(name="allowmediacode", type_=Integer, default=1)
    allowanonymous = Column(name="allowanonymous", type_=Integer, default=0)
    allowpostspecial = Column(name="allowpostspecial",
                              type_=Integer, default=1)
    allowspecialonly = Column(name="allowspecialonly",
                              type_=Integer, default=0)
    allowappend = Column(name="allowappend", type_=Integer, default=0)
    alloweditrules = Column(name="alloweditrules", type_=Integer, default=0)
    allowfeed = Column(name="allowfeed", type_=Integer, default=1)
    allowside = Column(name="allowside", type_=Integer, default=0)
    recyclebin = Column(name="recyclebin", type_=Integer, default=1)
    modnewposts = Column(name="modnewposts", type_=Integer, default=0)
    jammer = Column(name="jammer", type_=Integer, default=0)
    disablewatermark = Column(name="disablewatermark",
                              type_=Integer, default=0)
    inheritedmod = Column(name="inheritedmod", type_=Integer, default=0)
    autoclose = Column(name="autoclose", type_=Integer, default=0)
    forumcolumns = Column(name="forumcolumns", type_=Integer, default=0)
    catforumcolumns = Column(name="catforumcolumns", type_=Integer, default=0)
    threadcaches = Column(name="threadcaches", type_=Integer, default=0)
    alloweditpost = Column(name="alloweditpost", type_=Integer, default=1)
    simple = Column(name="simple", type_=Integer, default=0)
    modworks = Column(name="modworks", type_=Integer, default=0)
    allowglobalstick = Column(name="allowglobalstick",
                              type_=Integer, default=1)
    level = Column(name="level", type_=Integer, default=0)
    commoncredits = Column(name="commoncredits", type_=Integer, default=0)
    archive = Column(name="archive", type_=Integer, default=0)
    recommend = Column(name="recommend", type_=Integer, default=0)
    favtimes = Column(name="favtimes", type_=Integer, default=0)
    sharetimes = Column(name="sharetimes", type_=Integer, default=0)
    disablethumb = Column(name="disablethumb", type_=Integer, default=0)
    disablecollect = Column(name="disablecollect", type_=Integer, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('fid'),
        {},
    )


class DzForumField(Base):
    __tablename__ = 'dz35_forum_forumfield'
    fid = Column(name="fid", type_=Integer, default=0)
    description = Column(name="description", type_=TEXT)
    password = Column(name="password", type_=String(12), default='')
    icon = Column(name="icon", type_=String(255), default='')
    redirect = Column(name="redirect", type_=String(255), default='')
    attachextensions = Column(name="attachextensions",
                              type_=String(255), default='')
    creditspolicy = Column(name="creditspolicy", type_=TEXT)
    formulaperm = Column(name="formulaperm", type_=TEXT)
    moderators = Column(name="moderators", type_=TEXT)
    rules = Column(name="rules", type_=TEXT)
    threadtypes = Column(name="threadtypes", type_=TEXT)
    threadsorts = Column(name="threadsorts", type_=TEXT)
    viewperm = Column(name="viewperm", type_=TEXT)
    postperm = Column(name="postperm", type_=TEXT)
    replyperm = Column(name="replyperm", type_=TEXT)
    getattachperm = Column(name="getattachperm", type_=TEXT)
    postattachperm = Column(name="postattachperm", type_=TEXT)
    postimageperm = Column(name="postimageperm", type_=TEXT)
    spviewperm = Column(name="spviewperm", type_=TEXT)
    seotitle = Column(name="seotitle", type_=TEXT)
    keywords = Column(name="keywords", type_=TEXT)
    seodescription = Column(name="seodescription", type_=TEXT)
    supe_pushsetting = Column(name="supe_pushsetting", type_=TEXT)
    modrecommend = Column(name="modrecommend", type_=TEXT)
    threadplugin = Column(name="threadplugin", type_=TEXT)
    replybg = Column(name="replybg", type_=TEXT)
    extra = Column(name="extra", type_=TEXT)
    jointype = Column(name="jointype", type_=Integer, default=0)
    gviewperm = Column(name="gviewperm", type_=Integer, default=0)
    membernum = Column(name="membernum", type_=Integer, default=0)
    dateline = Column(name="dateline", type_=Integer, default=0)
    lastupdate = Column(name="lastupdate", type_=Integer, default=0)
    activity = Column(name="activity", type_=Integer, default=0)
    founderuid = Column(name="founderuid", type_=Integer, default=0)
    foundername = Column(name="foundername", type_=String(255), default='')
    banner = Column(name="banner", type_=String(255), default='')
    groupnum = Column(name="groupnum", type_=Integer, default=0)
    commentitem = Column(name="commentitem", type_=TEXT)
    relatedgroup = Column(name="relatedgroup", type_=TEXT)
    picstyle = Column(name="picstyle", type_=Integer, default=0)
    widthauto = Column(name="widthauto", type_=Integer, default=0)
    noantitheft = Column(name="noantitheft", type_=Integer, default=0)
    noforumhidewater = Column(name="noforumhidewater",
                              type_=Integer, default=0)
    noforumrecommend = Column(name="noforumrecommend",
                              type_=Integer, default=0)
    livetid = Column(name="livetid", type_=Integer, default=0)
    price = Column(name="price", type_=Integer, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('fid'),
        {},
    )


class DzForumThread(Base):
    __tablename__ = 'dz35_forum_thread'

    def __init__(self) -> None:
        super().__init__()
        self.dateline = int(datetime.now().timestamp())
        self.lastpost = int(datetime.now().timestamp())

    tid = Column(name="tid", type_=Integer, autoincrement=True)
    fid = Column(name="fid", type_=Integer, default=0)
    posttableid = Column(name="posttableid", type_=Integer, default=0)
    typeid = Column(name="typeid", type_=Integer, default=0)
    sortid = Column(name="sortid", type_=Integer, default=0)
    readperm = Column(name="readperm", type_=Integer, default=0)
    price = Column(name="price", type_=Integer, default=0)
    author = Column(name="author", type_=String(15), default='')
    authorid = Column(name="authorid", type_=Integer, default=1)
    subject = Column(name="subject", type_=String(255), default='')
    dateline = Column(name="dateline", type_=Integer, default=0)
    lastpost = Column(name="lastpost", type_=Integer, default=0)
    lastposter = Column(name="lastposter", type_=String(15), default='admin')
    views = Column(name="views", type_=Integer, default=0)
    replies = Column(name="replies", type_=Integer, default=0)
    displayorder = Column(name="displayorder", type_=Integer, default=0)
    highlight = Column(name="highlight", type_=Integer, default=0)
    digest = Column(name="digest", type_=Integer, default=0)
    rate = Column(name="rate", type_=Integer, default=0)
    special = Column(name="special", type_=Integer, default=0)
    attachment = Column(name="attachment", type_=Integer, default=0)
    moderated = Column(name="moderated", type_=Integer, default=0)
    closed = Column(name="closed", type_=Integer, default=0)
    stickreply = Column(name="stickreply", type_=Integer, default=0)
    recommends = Column(name="recommends", type_=Integer, default=0)
    recommend_add = Column(name="recommend_add", type_=Integer, default=0)
    recommend_sub = Column(name="recommend_sub", type_=Integer, default=0)
    heats = Column(name="heats", type_=Integer, default=0)
    status = Column(name="status", type_=Integer, default=32)
    isgroup = Column(name="isgroup", type_=Integer, default=0)
    favtimes = Column(name="favtimes", type_=Integer, default=0)
    sharetimes = Column(name="sharetimes", type_=Integer, default=0)
    stamp = Column(name="stamp", type_=Integer, default=-1)
    icon = Column(name="icon", type_=Integer, default=-1)
    pushedaid = Column(name="pushedaid", type_=Integer, default=0)
    cover = Column(name="cover", type_=Integer, default=0)
    replycredit = Column(name="replycredit", type_=Integer, default=0)
    relatebytag = Column(name="relatebytag", type_=String(255), default='0')
    maxposition = Column(name="maxposition", type_=Integer, default=0)
    bgcolor = Column(name="bgcolor", type_=String(8), default='')
    comments = Column(name="comments", type_=Integer, default=0)
    hidden = Column(name="hidden", type_=Integer, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('tid'),
        {},
    )


class DzForumPost(Base):
    __tablename__ = 'dz35_forum_post'

    def __init__(self) -> None:
        super().__init__()
        self.dateline = int(datetime.now().timestamp())
        self.lastpost = int(datetime.now().timestamp())

    pid = Column(name="pid", type_=Integer)
    fid = Column(name="fid", type_=Integer, default=0)
    tid = Column(name="tid", type_=Integer, default=0)
    repid = Column(name="repid", type_=Integer, default=0)
    first = Column(name="first", type_=Integer, default=0)
    author = Column(name="author", type_=String(15), default='')
    authorid = Column(name="authorid", type_=Integer, default=0)
    subject = Column(name="subject", type_=String(255), default='')
    dateline = Column(name="dateline", type_=Integer, default=0)
    lastupdate = Column(name="lastupdate", type_=Integer, default=0)
    updateuid = Column(name="updateuid", type_=Integer, default=0)
    premsg = Column(name="premsg", type_=TEXT, default='')
    message = Column(name="message", type_=TEXT)
    useip = Column(name="useip", type_=String(45), default='')
    port = Column(name="port", type_=Integer, default=0)
    invisible = Column(name="invisible", type_=Integer, default=0)
    anonymous = Column(name="anonymous", type_=Integer, default=0)
    usesig = Column(name="usesig", type_=Integer, default=0)
    htmlon = Column(name="htmlon", type_=Integer, default=0)
    bbcodeoff = Column(name="bbcodeoff", type_=Integer, default=0)
    smileyoff = Column(name="smileyoff", type_=Integer, default=0)
    parseurloff = Column(name="parseurloff", type_=Integer, default=0)
    attachment = Column(name="attachment", type_=Integer, default=0)
    rate = Column(name="rate", type_=Integer, default=0)
    ratetimes = Column(name="ratetimes", type_=Integer, default=0)
    status = Column(name="status", type_=Integer, default=0)
    tags = Column(name="tags", type_=String(255), default='0')
    comment = Column(name="comment", type_=Integer, default=0)
    replycredit = Column(name="replycredit", type_=Integer, default=0)
    position = Column(name="position", type_=Integer,)
    __table_args__ = (
        PrimaryKeyConstraint('tid', 'position'),
        {},
    )


class DzCommonMember(Base):
    __tablename__ = 'dz35_common_member'
    uid = Column(name="uid", type_=Integer)
    email = Column(name="email", type_=String(255), default='')
    username = Column(name="username", type_=String(15), default='')
    password = Column(name="password", type_=String(32), default='')
    secmobicc = Column(name="secmobicc", type_=String(3), default='')
    secmobile = Column(name="secmobile", type_=String(12), default='')
    status = Column(name="status", type_=Integer, default=0)
    emailstatus = Column(name="emailstatus", type_=Integer, default=0)
    avatarstatus = Column(name="avatarstatus", type_=Integer, default=0)
    secmobilestatus = Column(name="secmobilestatus", type_=Integer, default=0)
    adminid = Column(name="adminid", type_=Integer, default=0)
    groupid = Column(name="groupid", type_=Integer, default=0)
    groupexpiry = Column(name="groupexpiry", type_=Integer, default=0)
    extgroupids = Column(name="extgroupids", type_=String(20), default='')
    regdate = Column(name="regdate", type_=Integer, default=0)
    credits = Column(name="credits", type_=Integer, default=0)
    notifysound = Column(name="notifysound", type_=Integer, default=0)
    timeoffset = Column(name="timeoffset", type_=String(4), default='')
    newpm = Column(name="newpm", type_=Integer, default=0)
    newprompt = Column(name="newprompt", type_=Integer, default=0)
    accessmasks = Column(name="accessmasks", type_=Integer, default=0)
    allowadmincp = Column(name="allowadmincp", type_=Integer, default=0)
    onlyacceptfriendpm = Column(name="onlyacceptfriendpm", type_=Integer, default=0)
    conisbind = Column(name="conisbind", type_=Integer, default=0)
    freeze = Column(name="freeze", type_=Integer, default=0)
    __table_args__ = (
        PrimaryKeyConstraint('uid'),
        {},
    )
