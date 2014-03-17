# package
#-*- coding: UTF-8 -*-


from sqlalchemy.orm import (
    scoped_session,
    sessionmaker,
    )

from zope.sqlalchemy import ZopeTransactionExtension

DBSession = scoped_session(sessionmaker(extension=ZopeTransactionExtension()))

import infosys.models.base

#import .fias

import infosys.models.organization

#import .classifiers




