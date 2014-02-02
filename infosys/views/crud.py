# -*- coding: utf-8 -*-

from pyramid.response import Response
from pyramid.view import view_config
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import class_mapper
from sqlalchemy import func
import datetime
import ast
import infosys.models
import json
import traceback, sys
import inspect


from ..models import DBSession
import infosys.models as models
from ..models.base import Base

import logging
logger = logging.getLogger(__name__)


def addFilterToQuery(query, attr, filterVal):
  logger.debug('ADDFILTERTOQUER !!!\n')
  if filterVal[0] == 'likeci':
    query = query.filter(func.lower(attr).like(func.lower(filterVal[1])))
  if filterVal[0] == 'like':
    query = query.filter(attr.like(filterVal[1]))
  if filterVal[0] == 'eq':
    query = query.filter(attr == filterVal[1])
  if filterVal[0] == 'null':
    query = query.filter(attr == None)
  if filterVal[0] == 'notnull':
    query = query.filter(attr != None)
  return query

@view_config(route_name='jsonp_crud_model', renderer='jsonp')
@view_config(route_name='jsonp_crud_model:command', renderer='jsonp')
@view_config(route_name='json_crud_model', renderer='json')
@view_config(route_name='json_crud_model:command', renderer='json')
def crud_model(request):
  """
    /{model}/{command}

    command: Get, Update, Destroy, Create
  """
  model=request.matchdict.get('model')
  try: 
    targetClass = rec_getattr( models, model)
    pk_name = class_mapper(targetClass).primary_key[0].name
  except:
    logger.error("can't find model by name %s", model)
    return { 'success' : False }


  command = request.matchdict.get('command', 'Get')
  
  if not command in ['Get', 'Update', 'Destroy', 'Create']:
    logger.error("wrong command %s", command)
    return { 'success' : False }

  logger.info("command: %s", command)

  if command == 'Get':
    logger.info(request)
    limit = request.params.get('limit',100)
    page = request.params.get('page', None)
    sort = request.params.get('sort', None)
    # Может быть передан PK в виде фильтра
    pk_value = request.params.get(pk_name, None)
    if sort:
      try:
        sort = ast.literal_eval(sort)
        propName = sort[0].get('property',None)
        direction = sort[0].get('direction',None)
      except:
        traceback.print_exc(file=sys.stdout)
        return { 'success' : False }
    
    query = DBSession.query(targetClass)
    if pk_value:
      query = query.filter_by(**{pk_name : pk_value})

    # Добавляем фильтры, если они были в запросе
    logger.debug(request.params.keys())
    for param_name in request.params.keys():
      if not param_name == pk_name and \
          hasattr( targetClass, param_name):
        param_value  = request.params[param_name]
        filterVal = ast.literal_eval(param_value)
        query = addFilterToQuery(query, getattr(targetClass,param_name), filterVal)
    if page and limit:
      try:
        page = int(page)
        limit = int(limit)
        query = query.limit(limit)
        query = query.offset((page-1)*limit)
      except:
        return { 'success' : False }


    #.filter(targetClass.id.in_(idList)).all()
    queryList=query.all()
    #return json.dumps(items, cls=AlchemyEncoder)
    rlist = []
    for item in queryList:
      rlist.append(obj_to_dict(item))
    totalQuery = DBSession.query(targetClass)
    # Добавляем фильтры, если они были в запросе
    for param_name in request.params.keys():
      if not param_name == pk_name and \
          hasattr( targetClass, param_name):
        param_value  = request.params[param_name]
        filterVal = ast.literal_eval(param_value)
        op = filterVal[0]
        if op == 'like':
          totalQuery = addFilterToQuery(totalQuery, getattr(targetClass,param_name), filterVal)        

    total=totalQuery.count()
    msg = {
      'success' : True,
             'total' : total,
                  'identifier' : pk_name,
      'items' : rlist,
    }

    return msg

  if command == 'Update':
    try:
      # Пока не понятно может ли реально передаваться список,
      # делаем код на все случаи жизни:
      # Если словарь - добавляем в массив
      updateList = ast.literal_eval(request.params.get('data'))
      if isinstance(updateList, dict):
        updateList = [updateList]

      rlist = []
      # обновляем каждую переданную запись
      for updateRec in updateList:
        # формируем список значений полей
        value_dict = dict()
        for param_name in updateRec.keys():
          if not param_name == pk_name and hasattr( targetClass, param_name):
            param_value  = updateRec[param_name]
            # Пропускаем параметры
            if not isinstance (param_value, dict):
              value_dict[param_name] = param_value
              logger.debug("param_name %s",param_name)
              logger.debug("param_value %s ", param_value)
        pk_value =   updateRec.get(pk_name, None)
        logger.info("pk_value %s", pk_value)
        
        # собственно делаем обновление
        if (len(value_dict)>1):
          res = DBSession.query(targetClass).filter_by(**{pk_name : pk_value}).\
            update(value_dict, synchronize_session=False)
          if res <> 1:
            DBSession.rollback()
            return { 'success' : False }
          # Добавляем результат выполнения запроса
          model = DBSession.query(targetClass).get(pk_value)
          rlist.append(obj_to_dict(model))
          # будет ли работать?
          #DBSession.rollback()
    except:
      traceback.print_exc(file=sys.stdout)
      logger.error("can't update model %s",model)
      return { 'success' : False }
    return {'success': True,
      'items' : rlist,
      'identifier' : pk_name}

  if command == 'Create':
    logger.info(request.params)
    #return { 'success' : False }

    logger.info(request.params.get('data'))
    insertList = ast.literal_eval(request.params.get('data'))
    
    # Проверяем что получено - массив или словарь
    # Если словарь - добавляем в массив
    if isinstance(insertList, dict):
      insertList = [insertList]

    rlist = []
    # Передается массив записей на запись
    for insertRec in insertList:
      value_dict = dict()
      for param_name in insertRec.keys():
        if not param_name == pk_name and hasattr( targetClass, param_name):
          param_value = insertRec[param_name]
          if not param_value is None:
            value_dict[param_name] = param_value  
            logger.debug("param_name %s",param_name)
            logger.debug("param_value %s ", param_value)
            logger.debug("type(param_value) %s ", type(param_value))

          
      try:
        model = targetClass(**value_dict)
        DBSession.add(model)
        # Для получения pk
        DBSession.flush()
        DBSession.refresh(model)
        rlist.append(obj_to_dict(model))
      except:
        logger.error("can't insert model %s",model)
        return { 'success' : False }
    msg = {
      'success' : True,
       'identifier' : pk_name,
      'items' : rlist,
    }
    return msg

  if command == 'Destroy':
    try:
      logger.info("request.body %s", request.body)
      pk_value = ast.literal_eval(request.params.get('data')).get(pk_name, None)
      #pk_value = request.params[pk_name]
      if pk_value :
        logger.info("pk_value %s", pk_value)
        # make delete

        res = DBSession.query(targetClass).filter_by(**{pk_name : pk_value}).\
          delete(synchronize_session=False)
      else :
        return { 'success': False}
    except:
      logger.error("can't destroy model %s",model)
      return { 'success' : False }
    if res <> 1:
      return { 'success' : False }  
  return {'success' : True}
    


def obj_to_dict(obj, depth=True):
  if depth == False:
    logger.debug(obj)
  fields = {}
  if isinstance(obj.__class__, DeclarativeMeta):
    for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
      data = obj.__getattribute__(field)
      if isinstance(data, datetime.date) or \
        isinstance(data, datetime.time) or \
        isinstance(data, datetime.datetime) :
        data = str(data)
      if hasattr(data, '__tablename__'):
        data = obj_to_dict(data,False)
        
      if isinstance( data, list):
        rlist = []
        for record in data:
          if isinstance(record.__class__, DeclarativeMeta):
            if depth==True:
              # Залезаем внутрь объекта
              rlist.append(obj_to_dict(record,False))
            else:
              # Не делаем ничего
              # TODO возможно потребуется записывать PK
              pass
          else:
            rlist.append(record)
        data = rlist
      fields[field]=data
  return fields



def rec_getattr(obj, attr):
    """Get object's attribute. May use dot notation.

    >>> class C(object): pass
    >>> a = C()
    >>> a.b = C()
    >>> a.b.c = 4
    >>> rec_getattr(a, 'b.c')
    4
    """
    if '.' not in attr:
        return getattr(obj, attr)
    else:
        L = attr.split('.')
        return rec_getattr(getattr(obj, L[0]), '.'.join(L[1:]))


